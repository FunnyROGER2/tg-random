# tg-random — Telegram-бот для случайного выбора участника

Бот выбирает случайного пользователя из группы (исключая ботов).

## Команды

- `/random` — выбрать любого участника группы
- `/random-others` — выбрать участника, исключая того, кто вызвал команду

## Настройка

1. Создайте бота через [@BotFather](https://t.me/botfather)
2. Получите API_ID и API_HASH на [my.telegram.org](https://my.telegram.org)
3. Скопируйте `.env.example` в `.env` и заполните переменные (для локального запуска)

## Запуск локально

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
python bot.py
```

## Деплой на VPS (Ubuntu)

Деплой выполняется автоматически при push в `main`/`master` или вручную через **Actions → Deploy to VPS → Run workflow**. Клонирование репозитория на сервере не требуется.

### Требования на VPS

- Ubuntu с Python 3.10+
- SSH-доступ по ключу
- Пустая директория для проекта (создаётся автоматически при первом деплое)

### Секреты репозитория (Settings → Secrets and variables → Actions)

| Секрет | Описание |
|--------|----------|
| `SSH_HOST` | IP или домен VPS |
| `SSH_USER` | Пользователь SSH |
| `SSH_PRIVATE_KEY` | Приватный SSH-ключ (полностью, включая `-----BEGIN ...-----`) |
| `DEPLOY_PATH` | Путь к проекту на сервере (например `/home/user/tg-random`) |
| `API_ID` | API ID с [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | API Hash с my.telegram.org |
| `BOT_TOKEN` | Токен бота от [@BotFather](https://t.me/botfather) |

### Опционально: systemd для автозапуска

После первого деплоя можно настроить systemd:

```bash
# На сервере
sudo cp $DEPLOY_PATH/tg-random.service /etc/systemd/system/
# Отредактировать User, WorkingDirectory, EnvironmentFile, ExecStart под свой путь
sudo nano /etc/systemd/system/tg-random.service
sudo systemctl daemon-reload
sudo systemctl enable tg-random
sudo systemctl start tg-random
```

Без systemd бот запускается через `nohup` при каждом деплое и перезапускается при следующем push.
