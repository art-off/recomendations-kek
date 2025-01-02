# Используем базовый образ с Python
FROM python:3.13-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Указываем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt requirements.txt

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в контейнер
COPY . .

# Открываем порт для сервера разработки Django
EXPOSE 8000

# Команда по умолчанию для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
