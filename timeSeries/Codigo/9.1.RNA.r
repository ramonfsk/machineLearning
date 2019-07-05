#Series temporais e analises preditivas - Fernando Amaral
library(forecast)
library(ggplot2)

modelo = nnetar(co2)
print(modelo)

prev= forecast(modelo, h=24)
print(prev)
autoplot(prev)
