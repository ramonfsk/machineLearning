#Series temporais e analises preditivas - Fernando Amaral
library(ggplot2)

#graficos do R core
plot(sunspots)
hist(sunspots)
boxplot(sunspots)

#ggplot
autoplot(AirPassengers)

#explorando parte da serie
sun2 = window(sunspots,1749,c(1763,12))
plot(sun2)
hist(sun2)
boxplot(sun2)

#agregar valores
plot(aggregate(AirPassengers, FUN=mean))


