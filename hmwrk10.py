######### 1) #########
import datetime

# def printing_domains_from_txt_file(my_dom_file):
#     with open(my_dom_file, 'r') as my_file:
#         data = my_file.readlines()
#     return data
#
#
# filename = "domains.txt"
# domains_data = printing_domains_from_txt_file(my_dom_file=filename)
# domains_data1 = []
# for i in domains_data:
#     x = i.replace('.', '').replace('\n', '')
#     domains_data1.append(x)
# print(domains_data1)


######### 2) #########

# def printing_data_from_txt_file(my_name_file):
#     with open(my_name_file, 'r') as my_file:
#         data = my_file.readlines()
#     return data
#
#
# filename = "names.txt"
# name_data = printing_data_from_txt_file(my_name_file=filename)
# last_name = []
# for i in name_data:
#     x = i.split('\t')[1]
#     last_name.append(x)
# print(last_name)


######### 3) #########


# def printing_data_from_txt_file(my_name_file):
#     with open(my_name_file, 'r') as my_file:
#         data = my_file.readlines()
#     return data
#
#
# filename = "authors.txt"
# name_data = printing_data_from_txt_file(my_name_file=filename)
# date_list = []
# for i in name_data:
#     if i and ' - ' in i:
#         x = i.split(' - ')[0]
#         date_list.append({'date': x})
# print(date_list)