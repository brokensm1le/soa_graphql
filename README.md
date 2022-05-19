# soa_graphql

**Работа сделана на 10 баллов**

Видео с работающим приложением: https://youtu.be/5lXaD-8pJ0k

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

Можем написать подобные запросы:

**Example1:**

```
query {
  allGames {
    id
    status
    scoreboard {
      whoWin
    }
    comments
  }
}
```

**Example2:**

```
query {
  game(id:1) {
    status
    scoreboard {
      whoWin
    }
    comments
  }
}
```
