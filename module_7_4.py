import os
from os.path import join, getmtime, getsize, dirname
import time

print(os.getcwd())
# def show_path_info(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             filepath = join(root, file)
#             filetime = getmtime(filepath)
#             formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#             filesize = getsize(filepath)
#             parent_dir = dirname(filepath)
#             print(
#                 f'Обнаружен файл: {file},'
#                 f'Путь: {filepath},'
#                 f'Размер: {filesize} байт,'
#                 f'Время изменения: {formatted_time},'
#                 f'Родительская директория: {parent_dir}')
#
# if __name__ == '__main__':
#     show_path_info('.')
