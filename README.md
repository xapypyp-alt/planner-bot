# Telegram Daily Planner Bot

## Описание
Telegram-бот для управления задачами и получения напоминаний.

## Запуск локально
```bash
python -m pip install -r requirements.txt
set BOT_TOKEN=8212616865:AAFuAolhVCeA6ZZC1FmGIOJl-durcxXWUAs
python src/main.py
```
## Запуск docker

### Отладка
- docker compose down -v
- docker compose up -d --build
- docker-compose logs -f

## Запуск
- docker compose up -d --build

## Структура проекта
- .idea - папка для файлов конфигурации бота
- Dockerfile - файл Docker
- docker-compose.yml - файл конфигурации Docker
- main.py - основной файл логики бота
- requirements.txt - зависимости проекта
- LICENSE - файл с авторским правом на проект
- .env.example - Токен бота
- pre-commit.yaml - файл pre-commit
- src - папка со всеми python файлами