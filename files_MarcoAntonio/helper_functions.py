from collections import deque
from bisect import insort, bisect_left
from itertools import islice
import numpy as np
import pandas as pd
import re

def add_datepart(df, fldname, drop=True, time=False):
    fld = df[fldname]
    fld_dtype = fld.dtype
    if isinstance(fld_dtype, pd.core.dtypes.dtypes.DatetimeTZDtype):
        fld_dtype = np.datetime64

    if not np.issubdtype(fld_dtype, np.datetime64):
        df[fldname] = fld = pd.to_datetime(fld, infer_datetime_format=True)
    targ_pre = re.sub('[Dd]ate$', '', fldname)
    attr = ['Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear',
            'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start', 'Is_year_end', 'Is_year_start']
    if time: attr = attr + ['Hour', 'Minute', 'Second']
    for n in attr: df[targ_pre + n] = getattr(fld.dt, n.lower())
    df[targ_pre + 'Elapsed'] = fld.astype(np.int64) // 10 ** 9
    if drop: df.drop(fldname, axis=1, inplace=True)


def is_outlier(points, thresh=3.5):
    '''
    Returns a boolean array with True if points are outliers and False
    otherwise.

    Parameters:
    -----------
        points : An numobservations by numdimensions array of observations
        thresh : The modified z-score to use as a threshold. Observations with
            a modified z-score (based on the median absolute deviation) greater
            than this value will be classified as outliers.

    Returns:
    --------
        mask : A numobservations-length boolean array.

    References:
    ----------
        Boris Iglewicz and David Hoaglin (1993), 'Volume 16: How to Detect and
        Handle Outliers', The ASQC Basic References in Quality Control:
        Statistical Techniques, Edward F. Mykytka, Ph.D., Editor.
    '''
    if len(points.shape) == 1:
        points = points[:,None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return (modified_z_score, (modified_z_score > thresh))


def mad_based_outlier(point, med, thresh=3.5):
    '''
    Median Absolute Deviation (MAD) Statistic
    Outliers are computed as follows:
    * Let X be all data points
    * Let x_i be a data point in X
    * Let MAD be the median absolute deviation, defined as
            MAD = median( for all x in X, | x - median(X)| )
    * Let M_i be the modified z-score for payment x_i, defined as
            0.6745*(x_i - median(X))/MAD
    As per the recommendations by the literature, a data point is
    considered an outlier if the modified z-score, M_i > thresh, which
    is 3.5 by default.
    NOTE: regular MAD test evaluates on all points.
    My modification compares the out-of-bag points with a pre-built univariate distribution
    '''    
    #med_abs_deviation = profile.mad
    med = float(med)
    med_abs_deviation = med # med is the median of each training point's difference from their median
    diff = np.abs(point - med)
    if med_abs_deviation !=0:
        modified_z_score = 0.6745 * diff / med_abs_deviation
        "outlier" if modified_z_score > thresh else "normal"
        return modified_z_score > thresh
    else:
        return False


def plotMovingAverage(series, window, plot_intervals=False, scale=1.96, plot_anomalies=False):

    """
        series - dataframe with timeseries
        window - rolling window size 
        plot_intervals - show confidence intervals
        plot_anomalies - show anomalies 
    """
    rolling_mean = series.rolling(window=window).mean()

    plt.figure(figsize=(15,5))
    plt.title("Moving average\n window size = {}".format(window))
    plt.plot(rolling_mean, "g", label="Rolling mean trend")

    # Plot confidence intervals for smoothed values
    if plot_intervals:
        mae = mean_absolute_error(series[window:], rolling_mean[window:])
        deviation = np.std(series[window:] - rolling_mean[window:])
        lower_bond = rolling_mean - (mae + scale * deviation)
        upper_bond = rolling_mean + (mae + scale * deviation)
        plt.plot(upper_bond, "r--", label="Upper Bond / Lower Bond")
        plt.plot(lower_bond, "r--")
        
        # Having the intervals, find abnormal values
        if plot_anomalies:
            anomalies = pd.DataFrame(index=series.index, columns=series.columns)
            anomalies[series<lower_bond] = series[series<lower_bond]
            anomalies[series>upper_bond] = series[series>upper_bond]
            plt.plot(anomalies, "ro", markersize=10)
        
    plt.plot(series[window:], label="Actual values")
    plt.legend(loc="upper left")
    plt.grid(True)
    

def running_median_insort(seq, window_size):
    """Contributed by Peter Otten"""
    seq = iter(seq)
    d = deque()
    s = []
    result = []
    for item in islice(seq, window_size):
        d.append(item)
        insort(s, item)
        result.append(s[len(d)//2])
    m = window_size // 2
    for item in seq:
        old = d.popleft()
        d.append(item)
        del s[bisect_left(s, old)]
        insort(s, item)
        result.append(s[m])
    return result


# Creating sales lag features
def create_sales_lag_feats(df, gpby_cols, target_col, lags):
    gpby = df.groupby(gpby_cols)
    for i in lags:
        df['_'.join([target_col, 'lag', str(i)])] = \
                gpby[target_col].shift(i).values + np.random.normal(scale=1.6, size=(len(df),))
    return df


# Creating sales rolling mean features
def create_sales_rmean_feats(df, gpby_cols, target_col, windows, min_periods=2, 
                             shift=1, win_type=None):
    gpby = df.groupby(gpby_cols)
    for w in windows:
        df['_'.join([target_col, 'rmean', str(w)])] = \
            gpby[target_col].shift(shift).rolling(window=w, 
                                                  min_periods=min_periods,
                                                  win_type=win_type).mean().values +\
            np.random.normal(scale=1.6, size=(len(df),))
    return df


# Creating sales rolling median features
def create_sales_rmed_feats(df, gpby_cols, target_col, windows, min_periods=2, 
                            shift=1, win_type=None):
    gpby = df.groupby(gpby_cols)
    for w in windows:
        df['_'.join([target_col, 'rmed', str(w)])] = \
            gpby[target_col].shift(shift).rolling(window=w, 
                                                  min_periods=min_periods,
                                                  win_type=win_type).median().values +\
            np.random.normal(scale=1.6, size=(len(df),))
    return df


# Creating sales exponentially weighted mean features
def create_sales_ewm_feats(df, gpby_cols, target_col, alpha=[0.9], shift=[1]):
    gpby = df.groupby(gpby_cols)
    for a in alpha:
        for s in shift:
            df['_'.join([target_col, 'lag', str(s), 'ewm', str(a)])] = \
                gpby[target_col].shift(s).ewm(alpha=a).mean().values
    return df


def get_mapa_de_eventos():
    from sklearn.preprocessing import MultiLabelBinarizer
    mlb = MultiLabelBinarizer()

    # Importar mapa de eventos para dataframe
    df = pd.read_csv('mapa_eventos.csv')

    # Transformar a coluna 5_dia_util em boolean
    df['5_dia_util'] = df['5_dia_util'].fillna(0).astype(np.int)

    # Remover coluna transacoes_negocio
    df.drop('transacoes_negocio', axis=1, inplace=True)

    # Transformar items da coluna`detalhes` em one hot encoded
    detalhes = df.detalhes.str.split(';').apply(lambda x: pd.Series(x)).stack().str.strip().replace('', np.nan).dropna()

    detalhes_idx = detalhes.index.get_level_values(0).unique()
    detalhes_list = detalhes.groupby(level=0).apply(list).tolist()
    df.loc[detalhes_idx, 'detalhes'] = detalhes_list

    for row in df.loc[df.detalhes.isnull(), 'detalhes'].index: df.at[row, 'detalhes'] = []

    df = df.join(pd.DataFrame(mlb.fit_transform(df.pop('detalhes')), columns=mlb.classes_, index=df.index))
    
    return df 