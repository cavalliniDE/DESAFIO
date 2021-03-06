# -*- coding: utf-8 -*-
"""desafio_funcionalcorp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WOe4pF3hDdBhkUmr-OW59-CGurVX2zx-
"""

## Gostaria de deixar alguns adendos , sobre a tratativa do desafio técnico:
## Toda estrutura foi criada na Nuvem pela ferramenta Google Colab , a extensão de arquivos é .IPYNB
## Onde alguns imports são da própria ferramenta. Não iram executar diretamente no Python.
## O google solicita o authorization code , para montar a partição do Google Drive , para acesso aos arquivos
## Exemplo de chave criado pelo google para acesso e validação ao Google Drive: 4/1gEyw_8bqORDulwdq6fgG4F2d-zaqnehD137OdQEQOyuDHS3oN9HTPg
## O usuario deverá logar no Google / Google drive
## O comando spark-subit não irá se aplicar neste caso, para execução do código.
## Qualquer dúvida , fico a disposição.
## Att. Bruno Milhati Cavallini

# instalação 
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q https://archive.apache.org/dist/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz
!tar xf spark-2.4.4-bin-hadoop2.7.tgz
!pip install -q findspark

#Instalação Java-8 , instalação Spark , pacotes findsaprk , collections
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!tar xf spark-2.4.4-bin-hadoop2.7.tgz
!pip install -q findspark
!pip install collections-extended

## Setando variaveis de ambiente 
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.4.4-bin-hadoop2.7"

# imports
import findspark
findspark.init()
import pandas as pd
import datetime as dt
import collections
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql.functions import regexp_extract
from pyspark.sql.functions import col
from pyspark.sql.functions import sum as spark_sum
from pyspark.sql.functions import unix_timestamp, from_unixtime
from pyspark.sql import Row
from six.moves import urllib

# SparkContext
spark = SparkSession.builder.master("local[*]").getOrCreate()
sc = SparkContext.getOrCreate()

# Leitura de arquivos do Google Drive
# Ao executar o codigo o google solicita o authorization code , para montar a partição do Google Drive 
# Exemplo: 4/tQFvkBi4HJjeLRJMCwMOAkXIGBeMeqmpA15ir6t2i-trbmeMLYZ-lxc 

from google.colab import drive 
from google.colab import files
drive.mount('/content/gdrive')

# carregando CSV
file_local = 'gdrive/My Drive/2018_Yellow_Taxi_Trip_Data.csv'

# Carregando CSV em Fomato Pandas
data = pd.read_csv('gdrive/My Drive/2018_Yellow_Taxi_Trip_Data.csv')

# Visualização das primeira linhas 
data.head()

# Conversão de String para Datetime
data['tpep_pickup_datetime'] = pd.to_datetime(data['tpep_pickup_datetime'])
data['tpep_dropoff_datetime'] = pd.to_datetime(data['tpep_dropoff_datetime'])

# Visualização das primeira linhas 
data.head()

# Aplicando Novas Colunas com dias da semana
data['day_pickup'] = data['tpep_pickup_datetime'].dt.day_name()
data['day_dropoff'] = data['tpep_dropoff_datetime'].dt.day_name()

# Validando coluna 
data['day_pickup'].head()

# Validando coluna 
data['day_dropoff']

# inserindo um ID único no modelo
data["id"] = data.index + 1

# Rdd Texto
##linesj = sc.textFile(file_loc1)

# Convertendoum modelo pandas para DataFrame Spark
df = spark.createDataFrame(data)

##df_orders = spark.read.parquet('/dbfs/FileStore/refinado/orders')



##df = spark.read.csv(file_loc1,header=True)
# verificando a Tipagem de dados
df.printSchema()

# Criando Tabela temporária 
df.createOrReplaceTempView("TABELA")

# Média de Distancia entre viagens, com no maximo 2 passageiros
query1 = spark.sql("""
select  AVG(trip_distance) trip_distance from TABELA
where passenger_count <= '2'
""").show()

# query para verificação dos dias da semana 
spark.sql("""
select  
day_pickup
FROM TABELA
GROUP BY day_pickup
ORDER BY 1
""").show()

# Média de Corridas iniciadas nos finals de semana levando em consideração o campo VendorID
query2= spark.sql("""
select  
AVG(VendorID) MEDIA , day_pickup
FROM TABELA
WHERE day_pickup BETWEEN "Saturday" and "Sunday"
GROUP BY day_pickup
""").show()

# Notei que o VendorID não é um ID único
spark.sql("""
select  
count(VendorID) QTD, VendorID
FROM TABELA
WHERE day_pickup BETWEEN "Saturday" and "Sunday"
GROUP BY VendorID
""").show()

# Média de Corridas iniciadas nos finals de semana por ID Único
query3 = spark.sql("""
select  
AVG(id) MEDIA , day_pickup
FROM TABELA
WHERE day_pickup BETWEEN "Saturday" and "Sunday"
GROUP BY day_pickup
""").show()