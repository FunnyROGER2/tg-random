# tg-random — Telegram-бот для случайного выбора участника

Бот выбирает случайного пользователя из группы (исключая ботов).

## Команды

- `/random` — выбрать любого участника группы
- `/random-others` — выбрать участника, исключая того, кто вызвал команду

## Настройка

1. Создайте бота через [@BotFather](https://t.me/botfather)
2. Получите API_ID и API_HASH на [my.telegram.org](https://my.telegram.org)
3. Скопируйте `.env.example` в `.env` и заполните переменные

## Запуск локально

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
python bot.py
```

## Деплой на VPS (Ubuntu)

### Секреты репозитория (Settings → Secrets and variables → Actions)

| Секрет | Описание |
|--------|----------|
| `SSH_HOST` | IP или домен VPS |
| `SSH_USER` | Пользователь SSH |
| `SSH_PRIVATE_KEY` | Приватный SSH-ключ (полностью, включая `-----BEGIN ...-----`) |
| `DEPLOY_PATH` | Путь к проекту на сервере (например `/home/user/tg-random`) |

### Первоначальная настройка на сервере

```bash
# Клонировать репозиторий
git clone git@github.com:FunnyROGER2/tg-random.git
cd tg-random

# Создать виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Создать .env
cp .env.example .env
nano .env  # заполнить переменные

# Опционально: systemd для автозапуска
sudo cp tg-random.service /etc/systemd/system/
# Отредактировать User, WorkingDirectory, EnvironmentFile, ExecStart
sudo systemctl enable tg-random
sudo systemctl start tg-random
```
