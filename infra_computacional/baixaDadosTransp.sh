#!/bin/bash

# Este script baixa os dados do intervalo de dias indicado de um determinado mês e ano,
# que são passados como parâmetros para o script.
# Um exemplo de execução do script é: ./baixaDadosTransp.sh 01 10 05 2015

# set -x
#  Indicando qual o endereço do site - Link Novo
siteDownload="https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/despesas"

#Variáveis indicando o mês e o ano que irá buscar
diaIni=$1
diaFim=$2
mes=$3
ano=$4

# Diretórios que serão utilizados para baixar os dados e processá-los
dataDir="./dados"
tmpDir="./tmp"

# Verifica se o diretório já existe antes de criar
if [ ! -d "$dataDir" ]; then
    mkdir "$dataDir"
fi

# Executa o for para cada dia (inicio e fim) do período
for dia in $(seq -f "%02g" $diaIni $diaFim); do
  zipFile=$ano$mes$dia'_Despesas.zip'

  # O comando wget vai baixar o arquivo zip com os dados do site 
  echo -n "Baixando arquivo $zipFile ... "
  wget $siteDownload/$zipFile 2> /dev/null
  echo OK

  # Aqui os dados são descompactados no diretório temporário
  echo -n "Descompactando arquivos de $zipFile ... "
  unzip -o $zipFile '*_Despesas_Empenho.csv'  -d $tmpDir > /dev/null
  unzip -o $zipFile '*_Despesas_Pagamento.csv'  -d $tmpDir > /dev/null
  echo OK

  # Apagando a primeira linha dos arquivos para nao repetir o cabecalho
  if [ "$dia" -gt "$diaIni" ]; then
    echo -n "Removendo cabecalho extra de $zipFile... "
    sed -i '1d' "${tmpDir}/${ano}${mes}${dia}_Despesas_Empenho.csv"
    sed -i '1d' "${tmpDir}/${ano}${mes}${dia}_Despesas_Pagamento.csv"
    echo OK
  fi

  # Arquivo zip é removido
  echo -n "Removendo arquivo $zipFile ... "
  rm -f $zipFile
  echo OK
  
done

# Dados são copiados do diretório temporário para o diretório dados
cat $tmpDir/*Empenho.csv > $dataDir/$ano$mes$diaIni-$diaFim'_Despesas_Empenho.csv'
cat $tmpDir/*Pagamento.csv > $dataDir/$ano$mes$diaIni-$diaFim'_Despesas_Pagamento.csv'

# Diretório temporário é apagado
rm -f $tmpDir/*.csv
echo "Arquivos consolidados gerados"