from script import get_user_friends


person_id = int(input('enter id user without "id", only numbers: '))
quantity_top = int(input('enter quantity grous in top list: '))
get_user_friends(person_id, quantity_top)
