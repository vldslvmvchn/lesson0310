########## 1) ##########

# def reversing_list_on_unpaired_pos(obj_list, new_obj_list):
#
#     for i in obj_list:
#
#         if i in obj_list[1::2]:
#
#             new_obj_list.append(i[::-1])
#
#         elif i in obj_list[::2]:
#
#             new_obj_list.append(i)
#
#     return new_obj_list
#
# my_list = ['ave', 'agas', 'ghost', 'htog', 'aablm', 'ravc']
# new_list = []
# print(reversing_list_on_unpaired_pos(obj_list=my_list, new_obj_list=new_list))

########## 2) ##########

# def sorting_list_by_obj_with_first_letter_a(obj_list, new_obj_list):
#     for i in obj_list:
#
#         if i.startswith('a'):
#
#             new_obj_list.append(i)
#
#     return new_obj_list
#
# my_list = ['ave', 'agas', 'ghost', 'htog', 'aablm', 'ravc']
# new_list = []
# print(sorting_list_by_obj_with_first_letter_a(obj_list=my_list, new_obj_list=new_list))

########## 3) ##########

# def sorting_list_by_obj_with_letter_a(obj_list, new_obj_list):
#     for i in obj_list:
#
#         if 'a' in i:
#
#             new_obj_list.append(i)
#
#     return new_obj_list
#
# my_list = ['ave', 'agas', 'ghost', 'htog', 'aablm', 'ravc']
# new_list = []
# print(sorting_list_by_obj_with_letter_a(obj_list=my_list, new_obj_list=new_list))

########## 4) ##########

# def creating_list_of_str_from_list_of_str_and_int(obj_list, new_obj_list):
#
#     for i in obj_list:
#
#         if str(i) in obj_list:
#
#             new_obj_list.append(i)
#
#     return new_obj_list
#
# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
# print(creating_list_of_str_from_list_of_str_and_int(obj_list=my_list, new_obj_list=new_list))

########## 5) ##########

# def creating_list_of_unique_char_of_str(obj_str, char_list):
#
#     for i in set(obj_str):
#
#         if obj_str.count(i) == 1:
#
#             char_list.append(i)
#
#     return char_list
#
# my_str = "aadfftyth"
# my_list = []
# print(creating_list_of_unique_char_of_str(obj_str=my_str, char_list=my_list))

########## 6) ##########

# def creating_list_of_unique_char_of_2_strs(obj_str1, obj_str2, char_list):
#     for i in obj_str1:
#
#         if i in obj_str2:
#
#             char_list.append(i)
#
#     return char_list
#
# my_str1 = input("")
# my_str2 = input("")
# unique_chars = []
# print(creating_list_of_unique_char_of_2_strs(obj_str1=my_str1, obj_str2=my_str2, char_list=unique_chars))

########## 7) ##########

# def creating_list_of_unique_char_which_face_only_once_in_2_strs(obj_str1,
#                                                                 obj_str2,
#                                                                 char_list):
#     for i in obj_str1:
#
#         if i in obj_str2 and obj_str1.count(i) == 1 and obj_str2.count(i) == 1:
#
#             char_list.append(i)
#
#     return char_list
#
# my_str1 = input("")
# my_str2 = input("")
# unique_chars = []
# print(creating_list_of_unique_char_which_face_only_once_in_2_strs(
#        obj_str1=my_str1,
#        obj_str2=my_str2,
#        char_list=unique_chars)
#       )

########## 8) ##########

# import random
# import string
#
#
# def get_random_string(length):
#
#     result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
#
#     return result_str
#
#
# def creating_email_names(names):
#                                                  #you can take mixed or pure list
#     i = random.randrange(len(names))             # get random index
#
#     names[i], names[-1] = names[-1], names[i]    # swap with the last element
#
#     x = names.pop()                              # pop last element O(1)
#
#     return x
#
#
# def creating_email_domains(doms):
#
#     i = random.randrange(len(doms))
#
#     doms[i], doms[-1] = doms[-1], doms[i]
#
#     y = doms.pop()
#
#     return y
#
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = ((creating_email_names(names=names))
#           + '.'
#           + str(random.randrange(100, 1000))
#           + '@'
#           + get_random_string(random.randrange(5, 8))
#           + '.'
#           + (creating_email_domains(doms=domains)))
# print(e_mail)
