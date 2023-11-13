# def printing_data_from_txt_file(my_data_file):
#     with open(my_data_file, 'r') as my_file:
#         data = my_file.readlines()
#     return data


######### 1) #########

#
# def printing_out_domains(name_of_domainsfile):
#
#     name_of_domainsfile = printing_data_from_txt_file(my_data_file=filename)
#     domains_list = []
#
#     for i in name_of_domainsfile:
#
#         x = i.replace('.', '').replace('\n', '')
#
#         domains_list.append(x)
#
#     return domains_list
#
#
# filename = "domains.txt"
# result_of_domains = printing_out_domains(name_of_domainsfile=filename)
# print(result_of_domains)


######### 2) #########
#
# def printing_out_names(name_of_namesfile):
#
#     name_of_namesfile = printing_data_from_txt_file(my_data_file=filename)
#     last_name = []
#
#     for i in name_of_namesfile:
#
#         x = i.split('\t')[1]
#
#         last_name.append(x)
#
#     return last_name
#
#
# filename = "names.txt"
# result_of_names = printing_out_names(name_of_namesfile=filename)
# print(result_of_names)


######### 3) #########


# def printing_out_date(name_of_datefile):
#
#     name_of_datefile = printing_data_from_txt_file(my_data_file=filename)
#     date_list = []
#
#     for i in name_of_datefile:
#
#         if i and ' - ' in i:
#
#             x = i.split(' - ')[0]
#
#             date_list.append({'date': x})
#
#     return date_list
#
#
# filename = "authors.txt"
# result_of_dates = printing_out_date(name_of_datefile=filename)
# print(result_of_dates)