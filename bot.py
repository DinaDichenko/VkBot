import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import TOKEN
from datetime import datetime, date, time

vk_session = vk_api.VkApi( token = TOKEN)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(td, text):
    vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            msg = event.text.lower()
            id = event.user_id

            if msg == 'привет':
                sender(id, 'и тебе тоже привет')
            if msg == 'время':
                time_check = datetime.now()
                sender(id, f"Время: {time_check.hour} часа {time_check.minute} минут")
            if msg == 'привет':
                sender(id, 'и тебе тоже привет')
            if msg == 'привет':
                sender(id, 'и тебе тоже привет')
            if msg == 'привет':
                sender(id, 'и тебе тоже привет')