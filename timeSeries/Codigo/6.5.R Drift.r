#Series temporais e analises preditivas - Fernando Amaral
library(forecast)
library(ggplot2)

autoplot(austres)

prev = rwf(austres, h=12, drift = F)
autoplot(prev)

prev = rwf(austres, h=12, drift = T)
autoplot(prev)




