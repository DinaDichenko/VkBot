#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime, date, time
from config import TOKEN

vk_session = vk_api.VkApi(token = TOKEN)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def get_keyboard(buts):
    """
    создание клавиатуры
    """
	global get_but
	nb = []
	color = ''
	for i in range(len(buts)):
		nb.append([])
		for k in range(len(buts[i])):
			nb[i].append(None)
	for i in range(len(buts)):
		for k in range(len(buts[i])):
			text = buts[i][k][0]
			if buts[i][k][1] == 'p':
				color = 'primary'
			elif buts[i][k][1] == 'n':
				color = 'primary'
			nb[i][k] = {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }
	first_keyboard = {
	    'one_time': False,
	    'buttons': nb
	    }
	first_keyboard = json.dumps(first_keyboard, ensure_ascii=False).encode('utf-8')
	first_keyboard = str(first_keyboard.decode('utf-8'))
	return first_keyboard

keyboard1 = get_keyboard(
	[
		[ ('/домашка', 'p') ],
		[ ('Методички', 'p') ],
		[ ('Номера преподавателей', 'p') ],
		[ ('Баллы', 'p') ],
		[ ('Корпуса', 'p') ],
		[ ('Расписание', 'p') ]
	]
)


keyboard2 = get_keyboard(
	[
		[ ('Python', 'p') ],
		[ ('ИТ', 'p') ],
		[ ('ОС', 'p') ],
		[ ('ОМИТР', 'p') ],
		[ ('ЭВМ', 'p') ],
		[ ('ТП', 'p') ],
		[ ('Предпренимательство', 'p') ],
		[ ('Web', 'p') ]
	]
)

keyboard3 = get_keyboard(
	[
		[ ('Воронкин Р.А.', 'p') ],
		[ ('Говорова С.В.', 'p') ],
		[ ('Гайчук Д.В.', 'p') ],
		[ ('Яковлев С.В.', 'p') ],
		[ ('Мельников С.В.', 'p') ],
		[ ('Маслова О.И.', 'p') ],
		[ ('Шарунова Е.В.', 'p') ],
		[ ('Бережной В.В.', 'p') ],
		[ ('Мезенцев Д.В.', 'p') ]
	]
)


def sender(id, text):
    """
    Отправка сообщений (клавиатура 1)
    """
    vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : keyboard1})

def lesson(id, text):
    """
    Отправка сообщений (клавиатура 2)
    """
    vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : keyboard2})

def number(id, text):
    """
    Отправка сообщений (клавиатура 1)
    """
    vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : keyboard3})


def main():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:

                msg = event.text.lower()
                id = event.user_id

                if msg == 'привет':
                    sender(id, 'и тебе тоже привет')
                elif msg == 'время':
                    time_check = datetime.now()
                    sender(id, f"Время: {time_check.hour} часа {time_check.minute} минут")
                elif msg == '/help':
                    sender(id, f"/домашка - домашненее задание\n /расписание - расписание\n /корпуса - адреса корпусов\n /номера - номера преподавателей\n /методички - методички\n /баллы - какое количество баллов нужно для конкретной оценки")
                elif msg == '/домашка' or msg == 'домашнее задание':
                    sender(id, f"Заданий нет! Отдыхайте! С новым годом!")
                elif msg == '/расписание' or msg == 'расписание':
                    sender(id, f"https://ecampus.ncfu.ru/schedule/group/16139")
                elif msg == '/корпуса' or msg == 'корпуса':
                    sender(id, f"https://www.ncfu.ru/buildings_and_campuses/")
                elif msg == '/баллы' or msg == 'баллы':
                    sender(id, f"https://vk.com/icr_ncfu?w=wall-923784_12144")
                elif msg == 'номера преподавателей' or msg == '/номера':
                    number(id, f"Чей номер вы хотите узнать?")
                elif msg == 'методички' or msg == '/методички':
                    lesson(id, f"По какому предмету нужна методичка?")
                elif msg == 'python':
                    lesson(id, f"https://vk.com/away.php?to=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F18S4BkVVMeUVSWPLRkf5uNTkWtwat3Y3y%3Fusp%3Dsharing&cc_key=")
                elif msg == 'ит':
                    lesson(id, f"https://el.ncfu.ru/")
                elif msg == 'ос':
                    lesson(id, f"https://mail.yandex.ru/?ysclid=lcb2c8qx7p24141101")
                elif msg == 'омитр':
                    lesson(id, f"https://vk.com/away.php?to=https%3A%2F%2Fdisk.yandex.ru%2Fd%2Fphz85WsiW8quPw&cc_key=")
                elif msg == 'эвм':
                    lesson(id, f"https://el.ncfu.ru/")
                elif msg == 'тп':
                    lesson(id, f"https://e-ist.ru/2022/09/01/tech-prog-2/")
                elif msg == 'предпренимательство':
                    lesson(id, f"https://el.ncfu.ru/")
                elif msg == 'web':
                    lesson(id, f"https://el.ncfu.ru/")
                elif msg == 'воронкин р.а.':
                    number(id, f"+7 928 300-13-31")
                elif msg == 'говорова с.в.':
                    number(id, f"+7 918 787-60-80")
                elif msg == 'маслова о.и.':
                    number(id, f"+7 962 448-70-39")
                elif msg == 'бережной в.в.':
                    number(id, f"+7 918 782-97-96")
                elif msg == 'шарунова е.в.':
                    number(id, f"+7 928 302-19-54")
                elif msg == 'мельников с.в.':
                    number(id, f"+7 962 421-26-97")
                elif msg == 'гайчук д.в.':
                    number(id, f"+7 962 741-54-80")
                elif msg == 'яковлев с.в.':
                    number(id, f"+7 928 310-02-10")
                elif msg == 'мезенцев д.в.':
                    number(id, f"+7 918 889-48-74")


if __name__ == '__main__':
    main()
    