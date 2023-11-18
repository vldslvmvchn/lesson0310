# import os
#
#
# def returning_dict_of_files_from_directory(dir_name):
#     new_list = os.listdir(dir_name)
#     dir_list = []
#     files_list = []
#     for i in new_list:
#         object_path = os.path.join(dir_name, i)
#         if os.path.isdir(object_path):
#             dir_list.append(i)
#         else:
#             files_list.append(i)
#     return {
#         "dirnames": dir_list,
#         "filenames": files_list,
#     }
#
#
# file_dir = "homeworks"
# directory_name = os.path.join("..", file_dir)
# folder_dict = returning_dict_of_files_from_directory(dir_name=directory_name)
# print(folder_dict)
#
#
# def sorting_folder_dict(fold_dict, reverse=True):
#     for key in fold_dict:
#         fold_dict[key].sort(reverse=not reverse)
#     return fold_dict
#
#
# result = sorting_folder_dict(folder_dict, False)
# print(result)
#
#
# def checking_the_dot(obj, some_dict):
#     if "." in obj:
#         some_dict["filenames"].append(obj)
#     else:
#         some_dict["dirnames"].append(obj)
#
#
# def finding_out_is_file_or_dir(fold_dict, new_file):
#     new_folder_dict = {
#         "dirnames": [],
#         "filenames": [],
#     }
#     for key in fold_dict:
#         for obj in fold_dict[key]:
#             checking_the_dot(obj, new_folder_dict)
#
#     checking_the_dot(new_file, new_folder_dict)
#
#     return new_folder_dict
#
#
# result1 = finding_out_is_file_or_dir(folder_dict, "file.txt")
# print(result1)