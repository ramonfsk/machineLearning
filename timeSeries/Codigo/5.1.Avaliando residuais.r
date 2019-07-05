#Series temporais e analises preditivas - Fernando Amaral
library(forecast)
library(ggplot2)

autoplot(presidents)

prev = auto.arima(presidents)
print(prev$residuals)

#analisando os residuais
prev$residuals
autoplot(prev$residuals)
hist(prev$residuals)
var(prev$residuals,na.rm = T)
mean(as.vector(prev$residuals),na.rm = T)

#acf e pacf
acf(prev$residuals, na.action = na.pass )

#funcao especial para checar residuais
checkresiduals(prev)

#teste de normalidade
shapiro.test(prev$residuals)









