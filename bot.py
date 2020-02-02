import vk_api, random
from vk_api.longpoll import VkLongPoll, VkEventType
vk_session = vk_api.VkApi(token = "8327c926594bc7c8eefde4d344ee7a50877d2fe7b072d9e0a777dfbe872ee8d46ef8b7f23fa299b155e65")
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

YouGender = {}
CompanionGender = ""
men = []
women = []



def random_id():
	global random_id
	Random = 0
	Random += random.randint(0, 100000000)
	return Random

while True:
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:

			'''you gender'''
			try:
				while YouGender[event.user_id] != "man" and YouGender[event.user_id] != "woman":
					pass
			except:
				vk.messages.send(
					user_id = event.user_id,
					message = "Привет, впервые у нас? Приятного времяприпровождения.\nУкажите ваш пол(ИЗМЕНИТЬ ЕГО НЕЛЬЗЯ!!!)\n1. Парень\n2. Девушка",
					random_id = random_id()
				)
				for event in longpoll.listen():
						if event.type == VkEventType.MESSAGE_NEW and event.to_me:
							if event.text.lower() == "1":
								YouGender[event.user_id] = "man"
								break
							elif event.text.lower() == "2":
								YouGender[event.user_id] = "woman"
								break
							else:
								vk.messages.send(
									user_id = event.user_id,
									message = "Некорректное сообщение. Введите число.",
									random_id = random_id()
								)
								vk.messages.send(
									user_id = event.user_id,
									message = "Укажите ваш пол(ИЗМЕНИТЬ ЕГО НЕЛЬЗЯ!!!)\n1. Парень\n2. Девушка",
									random_id = random_id()
								)

			'''gender your componion'''
			if CompanionGender != "man" and CompanionGender != "woman":
				vk.messages.send(
					user_id = event.user_id,
					message = "Укажите пол собеседника(его изменить МОЖНО)\n1. Парень\n2. Девушка",
					random_id = random_id()
				)
				for event in longpoll.listen():
					if event.type == VkEventType.MESSAGE_NEW and event.to_me:
						if event.text.lower() == "1":
							CompanionGender = "man"
							break
						elif event.text.lower() == "2":
							CompanionGender = "woman"
							break
						else:
							vk.messages.send(
								user_id = event.user_id,
								message = "Некорректное сообщение. Введите число.",
								random_id = random_id()
							)
							vk.messages.send(
								user_id = event.user_id,
								message = "Укажите пол собеседника(его изменить МОЖНО)\n1. Парень\n2. Девушка",
								random_id = random_id()
							)
				