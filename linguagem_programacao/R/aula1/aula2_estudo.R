library(dplyr)
library(forcats)
library(lubridate)
library(readr)
library(tibble)
library(tidyr)
library(magrittr)
library(data.table)

dados = readr::read_csv('../../dbs/Mental Health Dataset.csv')
glimpse(dados)
head(dados)

dados %<>%
  mutate(mercosul = ifelse(dados$Country %in%
                             c("Argentina", "Brazil", "Paraguay", "Uruguay"),
                           "Mercosul", "Não Mercosul"),
         eh_brasil = ifelse(dados$Country == 'Brazil',
                            'Eh Brasil', 'Nao eh Brasil'))

dados %>%
  select(2:6)

dados %>%
  select(Occupation:family_history)

car_crash = fread('../../dbs/Brazil Total highway crashes 2010 - 2023.csv.gz')
glimpse(car_crash)

car_crash %>%
  filter(tipo_de_ocorrencia == 'sem vítima')

car_crash %>%
  filter(tipo_de_ocorrencia == 'sem vítima'&
           automovel >= 3)

car_crash %>%
  filter(between(automovel, 3, 5))

car_crash %>%
  filter(tipo_de_ocorrencia %in%
           c('sem vítima', 'com vítima'))

`%ni%` <- Negate(`%in%`)
car_crash %>%
  filter(tipo_de_ocorrencia %ni%
           c('sem vítima', 'com vítima'))

car_crash %>%
  filter(tipo_de_ocorrencia
         %like% 'vítima')

