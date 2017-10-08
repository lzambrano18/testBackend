# Cube API

## Requirements

### Install and configure Docker

* Install docker. [Docker](https://www.docker.com)

* Intall docker-compose. [Compose](https://docs.docker.com/compose/install/)

### Set Var Environment

* Copy to `env.example` into `.env`

```sh
cp env.example .env
```

* Edit values in `.env`

```sh
nano .env
```

* Config domain

```sh
echo "127.0.0.1" | sudo tee -a /etc/hosts > /dev/null
echo "127.0.0.1" | sudo tee -a /etc/hosts > /dev/null
```


## BackEnd

* Build containers 

```sh
docker-compose build
```

* Start container DB

```sh
docker-compose up -d postgres
```

* Apply migrations

```sh
docker-compose run --rm api python manage.py migrate
```

* Run Django Project

```sh
docker-compose up -d
```

* Open API on browser optional in Dev (http://127.0.0.1:8000)

### Run tests to style

* Run tests isort

```sh
docker-compose run --rm api isort -c -rc -df
```

* Run tests flake8

```sh
docker-compose run --rm api flake8
```
