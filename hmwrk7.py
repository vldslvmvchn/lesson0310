########## 1) ##########

# value_int = 103024050
# my_list = list(str(value_int))
# new_list = []
# for i in my_list:
#     if i == "0":
#         new_list.append(i)
# print(len(new_list))

########## 2) ##########

# value_int = 103024050 #1002000 --> dl9 proverki na vs9kiy
# my_list = list(str(value_int))
# new_list = []
# for i in my_list[::-1]:
#     if i == "0":
#         new_list.append(i)
#     elif i != "0":
#         break
# print(len(new_list))

########## 3) ##########

# my_list1 = [1, "wer", 5, "yt", 7, 8]
# my_list2 = ["gh", 9, "ak", 6, "gl", "gg"]
# my_result = []
# for index in my_list1:
#     if index in my_list1[::2]:
#         my_result.append(index)
# for index in my_list2:
#     if index in my_list2[::2]:
#         my_result.append(index)
# print(list(my_result))

########## 4) ##########

# my_list = ["gh", 9, "ak", 6, "gl", "gg"]
# new_list = []
# for i in my_list:
#     if i in my_list[:1]:
#         deleted_value = my_list.pop(0)
#         my_list.append(deleted_value)
#         new_list.append(my_list)
# print(new_list)

########## 5) ##########

# my_list = ["gh", 9, "ak", 6, "gl", "gg"]
# for i in my_list:
#     if i in my_list[:1]:
#         deleted_value = my_list.pop(0)
#         my_list.append(deleted_value)
# print(my_list)

########## 6) ##########

# my_str = "43 is bigger than 34 , but lower than 56"
# new_str = my_str.split(" ")
# new_list = []
# for i in new_str:
#     if i.isdigit():
#         new_list.append(i)
# my_result = int(new_list[0]) + int(new_list[1]) + int(new_list[2]) # nepravilbno
# print(my_result)

########## 7) ##########
#
# my_list = [2, 4, 1, 5, 3, 9, 0, 7]
# # print(len(my_list))
# new_list = []
# for i in range(1, len(my_list) - 1):
#     if my_list[i] > my_list[i - 1] + my_list[i + 1]:
#         new_list.append(i)
# print(len(new_list))

########## 8) ##########

# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
# for i in my_list:
#     if str(i) in my_list:
#         new_list.append(i)
# print(new_list)

########## 9) ##########

# my_str = "aadffgrtytuh"
# my_list = []
# for i in set(my_str):
#     if my_str.count(i) == 2:
#         my_list.append(i)
# print(my_list)

########## 10) ##########
#
# my_str1 = input("")
# my_str2 = input("")
# unique_chars = []
# for i in my_str1:
#     if i in my_str2:
#         unique_chars.append(i)
# print(unique_chars)

########## 11) ##########

# my_str1 = input("")
# my_str2 = input("")
# unique_chars = []
# for i in my_str1:
#     if i in my_str2 and my_str1.count(i) == 1 and my_str2.count(i) == 1:
#         unique_chars.append(i)
# print(unique_chars)