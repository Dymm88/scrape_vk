import time

import vk_api
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

TOKEN = os.environ.get('TOKEN')

session = vk_api.VkApi(token=TOKEN)
vk = session.get_api()


def get_user_friends(user_id):
    friends = session.method('friends.get', {'user_id': user_id})
    friend_groups = []

    for friend in friends['items']:
        user = session.method('users.get', {'user_ids': friend})
        group = session.method('groups.get', {'user_id': friend})
        time.sleep(0.4)
        print(f"{user[0]['first_name']} {user[0]['last_name']}")
        print(f"{group['items']}")
        friend_groups.extend(group['items'])
    print('#' * 77)
    print(friend_groups)
    result = len(friend_groups)
    print('#' * 77)
    print(f"{'count groups: '} + {result}")
