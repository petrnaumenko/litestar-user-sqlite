# Litestar User SQLite

🚀 Пример REST API для управления пользователями на базе:
- **Litestar** (современный Python-фреймворк)
- **SQLite** (легковесная база данных)
- **Advanced Alchemy** (инструменты SQLAlchemy 2.0)

---

## ⚙️ Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/petrnaumenko/litestar-user-sqlite.git
   cd litestar-user-sqlite
   ```

2. Установите зависимости через Poetry:
   ```bash
   poetry install
   ```

---

## 🚀 Запуск

Запустите сервер в режиме разработки (с авто-перезагрузкой):

```bash
poetry run litestar run --reload
```

Сервер будет доступен по адресу:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📚 Документация API

После запуска откройте интерактивную документацию:

- Swagger UI: [http://127.0.0.1:8000/schema/swagger](http://127.0.0.1:8000/schema/swagger)
- ReDoc: [http://127.0.0.1:8000/schema/redoc](http://127.0.0.1:8000/schema/redoc)

---

## 📌 Основные эндпоинты

| Метод | Путь           | Описание                     |
|-------|----------------|------------------------------|
| GET   | `/users`       | Список всех пользователей    |
| POST  | `/users`       | Создать пользователя         |
| GET   | `/users/{id}`  | Получить пользователя по ID  |
| PATCH | `/users/{id}`  | Обновить пользователя        |
| DELETE| `/users/{id}`  | Удалить пользователя         |

---

## 🛠 Технологии

- Python 3.11+
- Litestar 2.0+
- SQLAlchemy 2.0
- Advanced Alchemy
- msgspec (валидация и сериализация данных)
- Poetry (управление зависимостями)
