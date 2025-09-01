Блокировщик страниц ВКонтакте

Проект предоставляет инструменты для автоматической блокировки страниц ВКонтакте с использованием access token и отправки уведомлений в Telegram.

Функциональность

· Автоматическая блокировка пользователей ВКонтакте
· Отправка уведомлений о блокировках в Telegram
· Работа с официальным API ВКонтакте
· Гибкая настройка параметров блокировки

Требования

Перед использованием убедитесь, что у вас установлены:

· Python 3.7+
· Access token аккаунта ВКонтакте
· Токен бота Telegram (для уведомлений)
· Chat ID Telegram (для получения уведомлений)

Установка зависимостей

```bash
pip install vk-api
pip install python-telegram-bot
pip install requests
```

Или установите все зависимости сразу:

```bash
pip install vk-api python-telegram-bot requests
```

Настройка

1. Получите access token для ВКонтакте
2. Создайте бота в Telegram через @BotFather
3. Получите chat ID для отправки сообщений
4. Настройте параметры в конфигурационном файле:

```python
VK_ACCESS_TOKEN = 'your_vk_access_token_here'
TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token_here'
TELEGRAM_CHAT_ID = 'your_telegram_chat_id_here'
```

Использование

```python
from vk_api import VkApi
import requests

# Инициализация VK API
vk_session = VkApi(token=VK_ACCESS_TOKEN)
vk = vk_session.get_api()

# Блокировка пользователя
def block_user(user_id):
    try:
        vk.account.ban(owner_id=user_id)
        print(f"Пользователь {user_id} заблокирован")
    except Exception as e:
        print(f"Ошибка при блокировке: {e}")
```

Пример отправки уведомления в Telegram

```python
import requests

def send_telegram_notification(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    return response.json()
```

Важно

· Используйте токены только от своих аккаунтов
· Соблюдайте правила использования API ВКонтакте
· Не распространяйте свои access token
· Проект предназначен для образовательных целей

Лицензия

MIT License - смотрите файл LICENSE для подробностей.
