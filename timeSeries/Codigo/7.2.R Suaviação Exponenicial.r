#Series temporais e analises preditivas - Fernando Amaral
library(forecast)
library(ggplot2)

#tendencia linear hold
autoplot(austres)
mdl1 = holt(austres, h=16)
autoplot(mdl1)
mdl1$model

mdl2 = holt(austres,alpha = 0.2,   h=16)
autoplot(mdl2)

#compara as duas previs?es
plot(mdl1)
lines(mdl2$mean, col="red")

#tendencia amortecida
mdl3 = holt(austres,damped = T, phi = 0.9,  h=16)
autoplot(mdl3)

#mudamos phi 
mdl4 = holt(austres,damped = T, phi = 0.8,  h=16)
autoplot(mdl4)

#comparar os modelos
plot(mdl3)
lines(mdl4$mean, col="red")

#compara as duas previsoes
print(mdl3$mean)
print(mdl4$mean)

#holt winter - sazonal
#aditivo
mdl5 = hw(JohnsonJohnson,seasonal = "additive", h=16)
autoplot(mdl5)

#multiplicativo
mdl6 = hw(JohnsonJohnson,seasonal = "multiplicative", h=16)
autoplot(mdl6)

#comparar os modelos
plot(mdl5)
lines(mdl6$mean, col="red")

#comparando textual
print(mdl5$mean)
print(mdl6$mean)

#multiplicativo amortecido
mdl7 = hw(JohnsonJohnson,seasonal = "multiplicative", damped = T, phi = 0.9,h=16)
autoplot(mdl7)

#ets 
mdl8 = ets(JohnsonJohnson)
print(mdl8)

autoplot(mdl8$residuals)
autoplot(mdl8$fitted)

prev = forecast(mdl8, h=16,levels=c(85,90))
print(prev$mean)
autoplot(prev)

autoplot(decompose(JohnsonJohnson))

mdl9 = ets(JohnsonJohnson, model = "ZAA", damped = T)
print(mdl9)

mdl10 = ets(JohnsonJohnson, model = "ZZZ", damped = T)
print(mdl10)




