############### 1) ###############

# my_list = [1,
#            2,
#            34,
#            123,
#            3456,
#            23,
#            341,
#            15,
#            2,
#            245,
#            3765,
#            234,
#            100,
#            964
# ]
# for value in my_list:
#     if value > 100:
#         print(value)


############### 2) ###############

# my_list = [1,
#            2,
#            34,
#            123,
#            3456,
#            23,
#            341,
#            15,
#            2,
#            245,
#            3765,
#            234,
#            100,
#            964
# ]
# #1sposob
# my_result = [i for i in my_list if i > 100] #---- podsmotrel v lekcii
# print(f"my_result {my_result}\n")
# #2sposob
# my_result = []
# for i in my_list:
#     if i > 100:
#         print(f"my_result {[i]}", type(my_result)) #---- ne ponimayu po4emy nekrasivo vblvodit



############### 3) ###############
# my_list = [1]
#
# my_list = [1,
#            2,
#            34,
#            123,
#            3456,
#            23,
#            341,
#            15,
#            2,
#            245,
#            3765,
#            234,
#            100,
#            964
# ]
#
# if len(my_list) < 2:
#     my_list.append(0)
#     print(my_list)
# elif len(my_list) >= 2:
#     print(my_list[-1] + my_list[-2])
