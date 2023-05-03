import time

import vk_api
from dotenv import load_dotenv, find_dotenv
import os
import pandas as pd


load_dotenv(find_dotenv())

TOKEN = os.environ.get('TOKEN')

session = vk_api.VkApi(token=TOKEN)
vk = session.get_api()


def get_user_friends(user_id):
    friends = session.method('friends.get', {'user_id': user_id})

    friend_groups = []

    for friend in friends['items']:
        try:
            session.method('users.get', {'user_ids': friend})
            group = session.method('groups.get', {'user_id': friend})
            time.sleep(0.4)
            # print(f"{user[0]['first_name']} {user[0]['last_name']}")
            # print(f"{group['items']}")
            friend_groups.extend(group['items'])
        except vk_api.exceptions.ApiError:
            friend_groups.append(0)

    print('#' * 50)
    print('СПИСОК ТОП-10 ГРУПП')
    print('#' * 50)

    all_groups = pd.Series(friend_groups)
    result = all_groups.value_counts(sort=True)
    group_name = session.method('groups.getById', {'group_id': result.index[0]})
    a = group_name[0]
    print(a['name'])
    group_name = session.method('groups.getById', {'group_id': result.index[1]})
    a = group_name[0]
    print(a['name'])
    group_name = session.method('groups.getById', {'group_id': result.index[2]})
    a = group_name[0]
    print(a['name'])
    group_name = session.method('groups.getById', {'group_id': result.index[3]})
    a = group_name[0]
    print(a['name'])
    group_name = session.method('groups.getById', {'group_id': result.index[4]})
    a = group_name[0]
    print(a['name'])
    group_name = session.method('groups.getById', {'group_id': result.index[5]})
    a = group_name[0]
    print(a['name'])
    group_name = session.method('groups.getById', {'group_id': result.index[6]})
    a = group_name[0]
    print(a['name'])
    group_name = session.method('groups.getById', {'group_id': result.index[7]})
    a = group_name[0]
    print(a['name'])
    group_name = session.method('groups.getById', {'group_id': result.index[8]})
    a = group_name[0]
    print(a['name'])
    group_name = session.method('groups.getById', {'group_id': result.index[9]})
    a = group_name[0]
    print(a['name'])
