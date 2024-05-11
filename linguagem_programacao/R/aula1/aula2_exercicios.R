# ex 1
horario_compra = 20
valor_compra = 110

saudacao = ''
if (horario_compra < 12) {
  saudacao = 'Bom dia!'
} else if (horario_compra < 18) {
  saudacao = 'Boa tarde!'
} else {
  saudacao = 'Boa noite!'
}

cupom_num = 0
if (valor_compra > 100) {
  cupom_num = 10
} else {
  cupom_num = 5
}
cat(paste0(saudacao,' Você ganhou um cupom de ',cupom_num,'% de desconto :)'))

# ex 2
x = 1
y = 1

quadrante = 0
if ((x > 0) & (y > 0)) {
  quadrante = 1
} else if ((x < 0) & (y > 0)) {
  quadrante = 2
} else if ((x < 0) & (y < 0)) {
      quadrante = 3
} else if ((x > 0) & (y < 0)) {
        quadrante = 4
        }
cat(paste0('O ponto (',x,',',y,') está no quadrante ',quadrante))

# ex 3
n_desejado = 50
n_desejado = n_desejado -2
fibo = numeric(n_desejado)
fibo[1] = 1
fibo[2] = 1
for (i in 3:(n_desejado)) {
  fibo[i] = fibo[i-1] + fibo[i-2]
}
cat(paste0('Sequência de fibonatti com ',n_desejado,' numeros:'))
fibo

# ex 4
tentativas = 100000
res_tentativas = numeric(tentativas)
for (i in 1:tentativas) {
  soma <- 0
  n <- 0
  while (soma <= 5) {
    dado1 <- sample(1:6, 1, replace = FALSE)
    dado2 <- sample(1:6, 1, replace = FALSE)
    soma <- dado1 + dado2
    n <- n + 1
  }
  res_tentativas[i] = n
}
table(res_tentativas)

# ex 5
classifica_combustivel <- function(auto) {
  combustivel = switch(auto,
         'Carro' = c('Gasolina','Diesel','Eletrecidade','Gás Natural'),
         'Moto' = 'Gasolina',
         'Bicicleta' = 'Humana (sem cobutível)',
         'Ônibus' = c('Diesel','Gás Natural'),
         'Trem' = c('Eletricidade','Diesel'),
         'Avião' = 'Querosene',
         'Barco' = c('Diesel','Gasolina')
         )
  return(combustivel)
}
classifica_combustivel('Carro')
