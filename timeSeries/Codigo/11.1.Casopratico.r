#Series temporais e analises preditivas - Fernando Amaral

library(forecast)
library(ggplot2)
library(seasonal)
library(seasonalview)
library(urca)

#importar dados do hotel
dados = read.csv(file.choose(),header = F)
print(dados)
ocupacao = ts(dados, start = c(2003,1), end = c(2017,12), frequency=12)

#resumo
summary(ocupacao)

#visualizar
autoplot(ocupacao)
hist(ocupacao)
boxplot(ocupacao)

#decompor
dec =   decompose(ocupacao)
autoplot(dec)

#analisar a tendência com mais cuidado
autoplot(dec$trend)
autoplot(window(dec$trend, start=c(2015,9)))

#efeito sazonal por ano
ggseasonplot(ocupacao)  
ggseasonplot(window(ocupacao, start=c(2016))) 

#teste de estacionariedade
est = ur.kpss(ocupacao)
print(est)
ndiffs(ocupacao)

tsdisplay(ocupacao)

modelo = auto.arima(ocupacao, trace = T,stepwise = F, approximation = F )
print(modelo)

checkresiduals(modelo)

shapiro.test(modelo$residuals)

#previsao para 2 anos
previsao = forecast(modelo,h=24)

autoplot(previsao)




















