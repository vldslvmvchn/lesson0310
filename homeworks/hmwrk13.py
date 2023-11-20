# class ReadingFile:
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def printing_data_from_txt_file(self, my_data_file):
#         with open(my_data_file, 'r') as my_file:
#             data = my_file.readlines()
#         return data
#
#
# class Domains(ReadingFile):
#     def printing_out_domains(self, name_of_domainsfile):
#         domains_list = []
#
#         for i in name_of_domainsfile:
#             x = i.replace('.', '').replace('\n', '')
#
#             domains_list.append(x)
#
#         return domains_list
#
#
# class Names(ReadingFile):
#     def printing_out_names(self, name_of_namesfile):
#
#         last_name = []
#
#         for i in name_of_namesfile:
#             x = i.split('\t')[1]
#
#             last_name.append(x)
#
#         return last_name
#
#
# class Date(ReadingFile):
#     def printing_out_date(self, name_of_datefile):
#
#         date_list = []
#
#         for i in name_of_datefile:
#
#             if i and ' - ' in i:
#                 x = i.split(' - ')[0]
#
#                 date_list.append({'date': x})
#
#         return date_list
#
#
# ############################# DOMENbI #####################
#
# filename_domain = "domains.txt"
# list_of_domains = ReadingFile.printing_data_from_txt_file(self="domains.txt", my_data_file=filename_domain)
# fixed_list_of_domains = Domains.printing_out_domains(self="domains.txt", name_of_domainsfile=list_of_domains)
# print(fixed_list_of_domains)
#
# ############################# IMENA #####################
#
# filename_names = "names.txt"
# list_of_names = ReadingFile.printing_data_from_txt_file(self="names.txt", my_data_file=filename_names)
# fixed_list_of_names = Names.printing_out_names(self="names.txt", name_of_namesfile=list_of_names)
# print(fixed_list_of_names)
#
# ############################# DATbI #####################
#
# filename_date = "authors.txt"
# list_of_dates = ReadingFile.printing_data_from_txt_file(self="authors.txt", my_data_file=filename_date)
# fixed_list_of_dates = Date.printing_out_date(self="authors.txt", name_of_datefile=list_of_dates)
# print(fixed_list_of_dates)
