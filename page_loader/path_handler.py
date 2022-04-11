import os
import re


def make_result_path(web_page, output_path):
    count_parts = web_page.count('/')
    web_page_tmp = os.path.splitext(web_page)[0]
    total_path = ''
    while count_parts != 1:
        count_parts -= 1
        addr = os.path.split(web_page_tmp)
        total_path = addr[-1] + '-' + total_path
        web_page_tmp = addr[0]
    total_path = os.path.join(output_path,
                              re.sub('[^a-zA-Z0-9]', '-', total_path)[:-1])
    file_path = total_path + '.html'
    dir_path = total_path + '_files'
    return file_path, dir_path


def create_dir(dir_path):
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)