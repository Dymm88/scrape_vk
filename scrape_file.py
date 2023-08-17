"""Import funct"""
import script


person_id = int(input('enter id user without "id", only numbers: '))
quantity_top = int(input('enter quantity groups in top list: '))
script.get_user_friends(person_id, quantity_top)
