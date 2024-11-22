Neste projeto foi desenvolvido um pipeline usando python, que teve sua execução automatizada pelo Apache Airflow.


# Pré Requisitos

Docker e docker-compose

Bibliotecas

pip install apache-airflow
pip install paramiko
pip install requests==2.31.0

# Execução

Após clonar o repositório, acesse sua raiz e execute o comando abaixo.

docker-compose up -d

# Acesso web


http://localhost:8080

user: airflow
pass: airflow
