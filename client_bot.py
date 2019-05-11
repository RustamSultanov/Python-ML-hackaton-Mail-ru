import vk_api
from vk_bot import VkBot
from vk_api.longpoll import VkLongPoll, VkEventType



def write_msg(user_id, s):
    vk.method('messages.send', {'peer_id': user_id, 'message': s})


# Авторизуемся как сообщество
vk = vk_api.VkApi(token='2640ca8eb8eff7324802decf390ef53096405e405cd4d192f8f50379f91f9592c303be994aa8cbdee0b79')

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Словарь, где будут хранится разные объекты бота для разных пользователей
users_bot_class_dict = {}


def run():
    print("Server started")
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:

                print('New message:')
                print('For me by: ', end='')

                print(event.user_id)

                user_id = event.user_id
                if user_id not in users_bot_class_dict:
                    users_bot_class_dict[user_id] = VkBot(event.user_id)
                write_msg(event.user_id, bot.new_message(event.text))
                # # Checking to welcome message send
                # if users_bot_class_dict[user_id].WELCOME_MSG_SEND:
                #     write_msg(event.user_id, users_bot_class_dict[user_id].update_screen(event.text))
                # else:
                #     write_msg(event.user_id, users_bot_class_dict[user_id].get_welcome_msg(event.user_id))

                print('Text: ', event.text)
                
run()                