import time

import vk_api
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

TOKEN = os.environ.get('TOKEN')

session = vk_api.VkApi(token=TOKEN)
vk = session.get_api()


def get_user_friends(user_id):
    friends = session.method('friends.get', {'user_id:': user_id})
    count = 0

    friend_list = []
    for friend in friends['items']:
        session.method('users.get', {'user_ids': friend})
        time.sleep(0.5)
        friend_list.append(friend)

    session.method('groups.get', {'groups_name': user_id})

    group_list = []
    for groups in friend_list:
        session.method('groups.get', {'groups_name': groups})
        time.sleep(0.5)
        group_list.append(groups)
        count += 1
        print(count)
    print(group_list)


get_user_friends(int(input('enter id user: ')))
