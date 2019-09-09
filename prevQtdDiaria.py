# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:37:25 2019

@author: Ramon.Nascimento
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import date, datetime, timezone
from workalendar.america import Brazil
cal = Brazil()

dados = pd.read_csv('./transactions.csv')

#transformando a data
dados.data = pd.to_datetime(dados.data, format='%d/%m/%Y')

dados.dia = (dados['data']).dt.day
dados.mes = (dados['data']).dt.month
dados.ano = (dados['data']).dt.year
dados.diaAno = (dados['data']).dt.dayofyear

dados.dtypes

dados.corr().round(4)
