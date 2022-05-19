# soa_graphql

Видео с работающим приложением: 

## Начало
Скачиваем нужные библиотеки:

```
mkdir test_graphql
cd test_graphql

sudo apt install pipenv
pipenv install graphene
pipenv install fastapi
pipenv install avicorn
pipenv install starlette==0.16.0 --skip-lock

uvicorn server:app --reload
```


## Интерфейс

