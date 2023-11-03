########## 1) ##########

# my_list = ['ave', 'agas', 'ghost', 'htog', 'aablm', 'ravc']
# new_list = []
#
# for i in my_list:
#
#     if i in my_list[1::2]:
#
#         new_list.append(i[::-1])
#
#     elif i in my_list[::2]:
#
#         new_list.append(i)
#
# y = enumerate(new_list)
# print(list(y))

########## 2) ##########

# my_list = ['ave', 'agas', 'ghost', 'htog', 'abalm', 'ravc']
# new_list = []
# for i in my_list:
#
#     if i.startswith('a'):
#
#         new_list.append(i)
#
# print(list(new_list))

########## 3) ##########

# my_list = ['ave', 'agas', 'ghost', 'htog', 'abalm', 'ravc']
# new_list = []
# for i in my_list:
#
#     if 'a' in i:
#
#         new_list.append(i)
#
# print(list(new_list))

########## 4) ##########
########## a)

# my_list = [
#     {"name": "John", "age": 15},
#     {"name": "Blake", "age": 28},
#     {"name": "Alex", "age": 40},
#     {"name": "William", "age": 15},
#     {"name": "Jack", "age": 45},
#     {"name": "Kathy", "age": 23},
#     {"name": "Ludwick", "age": 50},
#     ]
# person_1, person_2, person_3, person_4, person_5, person_6, person_7 = my_list
# new_list = []
# my_new_list = []
#
# for person in my_list:
#     new_list.append(person['age'])
#     a = min(new_list)
#     if person['age'] == a:
#         my_new_list.append(person['name'])
# print(my_new_list)

########## b)

# my_list = [
#     {"name": "Ludwick", "age": 50},
#     {"name": "Blake", "age": 28},
#     {"name": "Alex", "age": 40},
#     {"name": "William", "age": 15},
#     {"name": "Jack", "age": 45},
#     {"name": "John", "age": 15},
#     {"name": "Kathy", "age": 23},
#     ]
# person_1, person_2, person_3, person_4, person_5, person_6, person_7 = my_list
# new_list = []
# my_new_list = []
# for person in my_list:
#     new_list.append(person['name']) ##sort key=len()
# a = max(new_list)
# # print(a)
# for person in my_list:
#     if len(person['name']) == len(a):
#         my_new_list.append(person['name'])
# print(my_new_list)

########## c)

# my_list = [
#     {"name": "John", "age": 15},
#     {"name": "Blake", "age": 28},
#     {"name": "Alex", "age": 40},
#     {"name": "William", "age": 15},
#     {"name": "Jack", "age": 45},
#     {"name": "Kathy", "age": 23},
#     {"name": "Ludwick", "age": 50},
#     ]
# person_1, person_2, person_3, person_4, person_5, person_6, person_7 = my_list
# new_list = []
# for person in my_list:
#     new_list.append(person['age'])
#     for i in new_list:
#         my_result = sum(new_list) / len(new_list)
# print(my_result) #ili print(int(my_result))


########## 5) ##########
########## a)

# my_dict_1 = {
#     1: '1111',
#     2: '2222',
#     3: '3333'
# }
#
# my_dict_2 = {
#     2: '2222',
#     3: '3333',
#     4: '4444',
#     5: '5555'
# }
# my_list = []
# for key in my_dict_1:
#     if key in my_dict_2:
#         my_list.append(key)
# print(my_list)

########## b)

# my_dict_1 = {
#     1: '1111',
#     2: '2222',
#     3: '3333'
# }
#
# my_dict_2 = {
#     2: '2222',
#     3: '3333',
#     4: '4444',
#     5: '5555'
# }
# my_list = []
# for key in my_dict_1:
#     if key not in my_dict_2:
#         my_list.append(key)
# print(my_list)

########## c)

# my_dict_1 = {
#     1: '1111',
#     2: '2222',
#     3: '3333'
# }
#
# my_dict_2 = {
#     2: '2222',
#     3: '3333',
#     4: '4444',
#     5: '5555'
# }
# new_dict = {}
#
# for key in my_dict_1:
#     if key not in my_dict_2:
#         new_dict[key] = my_dict_1[key]
# print(new_dict)

########## d)

# my_dict_1 = {
#     1: '1111',
#     2: '2222',
#     3: '3333'
# }
#
# my_dict_2 = {
#     2: '22',
#     3: '333',
#     4: '4444',
#     5: '5555'
# }
# for key in my_dict_1:
#     if key not in my_dict_2:
#         my_dict_2[key] = my_dict_1[key]
#     elif key in my_dict_2:
#         my_dict_2[key] = [my_dict_1[key], my_dict_2[key]]
# print(my_dict_2)
