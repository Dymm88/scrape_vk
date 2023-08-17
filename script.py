import os
import time
import pandas as pd
import vk_api
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.environ.get('TOKEN')

session = vk_api.VkApi(token=TOKEN)
vk = session.get_api()


def get_user_friends(user_id: int, quantity: int):
    friends = session.method('friends.get', {'user_id': user_id})

    friend_groups = []
    for friend in friends['items']:
        try:
            user = session.method('users.get', {'user_ids': friend})
            group = session.method('groups.get', {'user_id': friend})
            time.sleep(0.4)
            print(f"{user[0]['first_name']} {user[0]['last_name']}")
            print(f"{'count of groups:'} {group['count']}")
            print('_' * 50)
            friend_groups.extend(group['items'])
        except vk_api.exceptions.ApiError:
            pass
    total_groups = len(friend_groups)
    print(f"{'TOTAL:'} {total_groups}")
    print(' ')

    print(' ')
    print(f'СПИСОК ТОП-{quantity} ГРУПП')
    print(' ')

    df = pd.Series(friend_groups)
    result = df.value_counts(sort=True)
    to_list = list(result.index)

    end_list = []
    count = 0
    for name in to_list:
        list_id = session.method('groups.getById', {'group_id': name})
        group_name = list_id[0]
        count += 1
        end_list.append(group_name['name'])
        print(f"{count}{'.'} {group_name['name']}")
        if count == quantity:
            break

    with open(f'{user_id}.txt', 'w', encoding='utf8') as file:
        for i in end_list:
            file.write(i + '\n')
