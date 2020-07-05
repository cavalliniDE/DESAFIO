Teste teórico de analista de Business Intelligence


Nome do Candidato (a):  Bruno Milhati Cavallini
Data 	05/06/2020	


Crie um repositório no github e ponha os resultados e os código lá. Envie o link de acesso ao seu repositório criado.

Questão 4 – Uma tabela de clientes possui uma coluna sexo com dois valores possíveis (M – Masculino e F – Feminino). Grande parte das consultas considera o sexo como critério de pesquisa na cláusula WHERE juntamente com outros campos. Que tipo de índice que deve ser utilizado nessa coluna?

( ) Clustered Index.
(  ) Nonclustered Index. ( ) Bitmap Index.
( X) Não deve ser utilizado um índice nessa coluna por sua alta densidade.
( ) Não deve ser utilizado um índice nessa coluna por sua alta seletividade.




Questão 5 – De acordo com o T-SQL, quais são as cláusulas obrigatórias em uma query de SELECT?

( ) As cláusulas FROM E SELECT.
(  ) As cláusulas SELECT E WHERE. 
( X) A cláusula SELECT.
( ) As cláusulas SELECT, FROM E WHERE.


Questão 7 - O que acontece após a execução do comando: SELECT TRY_CAST(‘abc’ AS INT).


(  ) Um erro é gerado Um valor. 
(X ) null é retornado.
( ) Um valor inteiro é retornado. 
( ) Uma string é retornada.

Questão 8 - Em relação à clausula Where e Having podemos afirmar?

(  ) Ambas tem a mesma função. 
( ) São funções diferentes.
( X) Ambas tem a mesma função mas o filtro da clausula where linha por linha e o Having após o agrupamento.
( ) Ambas acontecem durante o agrupamento.


Questão 9– Você está criando um pacote SSIS na sua máquina que aponta para uma base SQL Server com uma conta SQL e é executado via Job agendado. Após concluir o pacote remete para produção e no outro dia quando verifica o JobHistory tem o seguinte erro
DTS_E_OLEDBERROR. An OLE DB error has occurred. Error code: 0x80040E4D. An OLE DB record is available. Source: "Microsoft SQL Native Client" Hresult: 0x80040E4D Description: "Login failed for user '<User_Name>'."
O que você deve fazer para que o pacote execute corretamente a noite?

( ) Mude todas as conexões para usar SQL Authentication.
( ) Mude todas as conexões para usar Windows Authentication 
( X) Encriptar o pacote com "EncryptSensitiveWithPassword" ou
"EncryptAllWithPassword" e forneça a senha cada vez que o usuário precisar executar. 
( ) Crie um DTSConfig para fornecer informações de conexão para o pacote em tempo de execução.

Questão 11 – Quais componentes são do MS-SQL Server Integration Services:
(  ) Designer SSIS, Cubos OLAP, Tarefas e Elementos de Fluxo de dados. 
(X ) Designer SSIS, Contêineres, Tarefas e Elementos de Fluxo de dados.
(  ) Data Mart, Designer SSIS, Contêineres e Elementos de Fluxo de Dados. 
( ) Data Mart, Designer SSIS, Tarefas e Elementos de Fluxo de Dados.
( ) Data Mart, Cubos OLAP, Contêineres e Tarefas.


Questão 12 - Em um comando SQL, o operador LIKE é usado em uma cláusula WHERE para buscar um determinado padrão em uma coluna.
( X) Certo.
( ) Errado.


Questão 14 - Muitos autores consideram a tecnologia de Data Warehousing (o processo de fazer Data Warehouse) como sendo uma evolução natural do ambiente de apoio à decisão. As empresas utilizam Data Warehouse com mais frequência, pois há a necessidade de domínios de informações estratégicas que podem garantir respostas rápidas, assegurando, dessa forma, a competitividade no mercado concorrente e em constantes mudanças. O DW possui diversas características. “A arquitetura do Data Warehouse   inclui,   além   de   estrutura   de   dados,   mecanismos    de comunicação, processamento da informação para o usuário. ” Assinale, a seguir, a característica correspondente.

(  ) Não volátil. ( ) Integração.
( ) Variação de tempo.
( ) Orientado por assunto.
( X) Arquitetura do ambiente.


Questão 15 - O objetivo dessa área é criar um ambiente intermediário de armazenamento e processamento dos dados oriundos de aplicações OLTP (Online Transaction Processing) e outras fontes, para o processo ETL (Extract Tranform Load), possibilitando seu tratamento, e permitindo sua posterior integração em formato e no tempo, evitando problemas após a criação do Data Warehouse e a concorrência com o ambiente transacional no consumo de recursos. A área citada é conhecida como:

( ) Transaction area.
(  )  Warehouse. 
(  ) Backup area. 
(  ) Staging area. 
( X) Cube area.

Questão 19 - VIEW é uma tabela virtual cujo conteúdo está definido por uma instrução SELECT

( X) Certo.
( ) Errado.
Questão 20 - No MS SQL Server, as tabelas criadas por meio do comando CREATE TABLE são temporárias se:

(  ) A opção TEMP é especificada logo após o termo CREATE. 
(   ) O comando é executado dentro de uma stored procedure. 
( ) O usuário não possui privilégio para criação de tabelas.
(X) O nome da tabela é iniciado por #.
( ) A opção ON refere-se ao filegroup TEMP.


Questão 21 – Descreva os modelos Start Schema (Ralph Kimball) e SnowFlake (Bill Inmon).

Esquema estrela é composto no centro por uma tabela fato, rodeada por tabelas de dimensão, ficando parecido com a forma de uma estrela. A ideia é propor uma visão para modelagem de base de dados para sistemas de apoio à decisão, que é o caso do Data Warehouse. O Snowflake também é projetado para suportar tomada de decisão, mas economizando espaço em disco. Embora o Star Schema ocupe mais espaço em disco, ele é mais fácil de implementar e acabou sendo mais utilizado porque além de hoje em dia o espaço ser muito barato, ele permite entregar projetos por pedaços.
Questão 23 – O que podemos entender por “Granularidade do dado”?

Refere-se  a como os dados estão sub-divididos. Quanto mais subdivididos e granulares são os dados, mais detalhados eles serão.A vantagem dos dados granulares é que estes podem ser moldados em diferentes formatos, de acordo com as necessidades. Podem ser mescladas com fontes externas de dados, o que facilita e amplia as possibilidades de análise. 


Teste Big Data (Daqui para baixo está em inglês)

	•	You work on a start-up that developed a bracelet to track down data about the health of inpatients. Each bracelet sends the data in JSON every 6 seconds to be analyzed and stored.These data will be used to generate a daily report on the Health Portal and

you need to come up with a real-time solution for analytics that is durable, scalable and parallel to support the whole operation.

Describe and justify the possible choices for the following architecture components:

My suggestions would be two at first,:

AWS Kinesis: Streams enable real-time processing of streaming data at massive scale , Data such as clickstreams, application logs, social media etc can be added from multiple sources and within seconds is available for processing to the Kinesis Applications.

Elasticsearch:  gives you plenty of options for grabbing data wherever it lives and getting it indexed. From there, tools like Kibana give you the ability to create rich dashboards and analysis, while Curator allows you to put the retention period on autopilot.


	•	Explain the difference between Amazon Athena and Redshift Spectrum as well as the main use cases for each of them.

Amazon Redshift is a fully managed, petabyte data warehouse service over the cloud. Redshift data warehouse tables can be connected using JDBC/ODBC clients or through the Redshift query editor.
The trade-off is that Redshift Spectrum queries do run slower than queries in an Amazon Redshift cluster, mainly because of data movement between S3 and the cluster. But if you’re fine with that trade-off, and the priority is cost, then a combination of S3 / Spectrum is a great choice. 

Amazon Redshift Spectrum is a feature of Amazon Redshift. Spectrum is a serverless query processing engine that allows to join data that sits in Amazon S3 with data in Amazon Redshift.

Amazon Athena is a serverless Analytics service to perform interactive query over AWS S3. Since Athena is a serverless service, user or Analyst does not have to worry about managing any infrastructure. Athena query DDLs are supported by Hive and query executions are internally supported by Presto Engine. Athena only supports S3 as a source for query executions. Athena supports almost all the S3 file formats to execute the query. Since Athena is an Analytical query service, you do not have to move the data into Data Warehouse. You can directly query your data over S3 and this way you do not have to worry about node management, loading the data, etc. Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run. 

Case:

A store sells its products online.
When a customer buys a product on the website or mobile app, the store needs to keep a record of that purchase in its production database.
At the end of the month, the store's financial director wants to know “how much do we sell this month?”. To get the answer, they could consult the production database. However, these queries would put more load on the production database, which would slow down.
This is not desirable, as a slow database will have a negative impact on sales.
And so the answer is to use an analytics database or data warehouse that has a replica of all transactions in the production database. The process to move data from production to analytics is called “ETL”

- Amazon Aurora to sell .
- Amazon Redshift to store short-term historical data to analyze how many was sold
- Amazon S3 for cheaper storage of all long-term historical data
- Amazon Redshift Spectrum to join long-term historical data in S3 with short-term historical data in Amazon Redshift, e.g. for multi-year comparisons from
sales in a current year vs. ticket sales from 10 years ago.
-Amazon Athena for quick ad-hoc querying of data in S3, e.g. to answer a single-year question about sales that requires data that only sits in S3, e.g. “how
many did we sell in July 10 years ago?” 




	•	You work for a start-up of photos processing and you need to swap the colors to black and white after loading them into Amazon S3. How can you do this on AWS??

I would use Python with tensorflow , to later store

	•	An organization implemented a streaming solution, on which a data goes through a Kinesis Data Stream and a Kinesis Data Stream until it is stored on Redshift and is made available to analysis. A new product requirement specifies some events which should be processed with a minimum delay and could trigger some actions afterward.

	•	Which technologies below are related to Big Data on Cloud?


	•	Kubernetes, Jenkins, Terraform


	•	Azure SQL Server, AWS Lambda, AWS EC2  


	•	Google BigQuery, Apache Spark, Amazon Redshift - X


	•	Digital Ocean, Packet, Javascript


	•	AWS, Google, Facebook


	•	Which file type is the best to read/write tabular data on big scales?

	•	CSV  - X


	•	Protobuf


	•	Gzip


	•	Parquet - X (Minha primeira opção  , Para Cloudera)


	•	JSON


	•	Avro ( Minha Segunda opção caso ambiente seja Hortonworks)

OBS: I was unsure about this question. I believe the tabular would be the CSV file. however the two most performative formats within the big data world, are parquet and Avro. Depending on the environment



	•	Choose all correct answers To real-time data processing which technology is best for the streaming layer?

	•	Apache Kafka


	•	MySQL


	•	MongoDB


	•	Python


	•	Apache Spark  - X 


	•	Explain the main points that define the concepts of ELT and ETL.


	•	Define in some lines the characteristics, 2 examples, and 2 use cases each for the following types of Databases:

	•	Relational: Oracle , mysql , bancos de dados tradicional armazenamento no modelo , linha e coluna , com primary key e foreign key , modelagem entidade/relacionamento 


	•	Key Value: redis , dynamoDB - gerenciamento de cache , podendo armazenar videos , audio , texto 


	•	Documents: elastic search, mongodb - analise de métricas , analise de logs 


	•	Graphs: Neo4j , RedisGraph - social media e networking , análise de fraude 


	•	Timeseries: kudu , Prometheus - streaming em near realtime , historico preditivo de compras futuras por exemplo


	•	In-Memory: Sqlite Redis  , - cache de sessão , filas de mensagens 


Teste Python

Baixe o arquivo e resposta as perguntas abaixo: (use pandas e numpy para lhe ajudar)

1.What is the average distance traveled by trips with a maximum of 2 passengers;


2 - What is the average trip time on Saturdays and Sundays;


3- To be able to provision your entire environment in a public cloud, preferably AWS.

Yes! It’s possible ,  on AWS Amazon, with the environment being properly configured , and appropriate tools. 
I don’t know policies about public cloud in the amazon environment.  I Wouldn’t know how to answer.



