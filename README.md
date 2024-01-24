🏦👨‍💻 Работа с API ModuleBank | Python, Django, Postgressql, Redis, Celery, Celery Beat
Приложение выгружает данные операций по API [ModuleBank](https://api.modulbank.ru/). 

## Что реализовано в этом проекте
- регулярная выгрузка каждый день в 4 утра по мск данных по Операциям.
- Защита от дублирования операций
- При создании нового банка запускается фоновая задача для первичной выгрузки операций из банка за последний год.
- Реализована админка(простая) для просмотра операций, банков, счетов и задач с их состоянием 

## Как запустить
- склонируйте репозиторий git clone https://github.com/Pavel2232/ModulBankIntegration
- Активируйте виртуальное окружение ```poetry init```
- Установите зависимости проекта ```poetry install```
- Заполните .env
```dotenv
TOKEN_MODUL_BANK=получаете у банка
SECRET_KEY=SECRET_KEY
POSTGRES_USER=POSTGRES_USER
POSTGRES_PASSWORD=POSTGRES_PASSWORD
POSTGRES_DB=POSTGRES_DB
POSTGRES_PORT=POSTGRES_PORT
DATABASE_URL=psql://name:password@127.0.0.1:5432/db_name
ALLOWED_HOSTS=127.0.0.1, localhost
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8080
REDIS_HOST=REDIS_HOST
REDIS_PORT=REDIS_PORT
REDIS_DATABASES=REDIS_DATABASES
REDIS_URL=redis://host:port/db
```
- выполните 
```shell
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```

## Как запустить через Docker
- выполните 
```shell
docker compose up -d
```

