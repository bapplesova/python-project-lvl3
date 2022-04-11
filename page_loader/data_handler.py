import os
import requests


def download_data(web_page):
    r = requests.get(web_page)
    return r.text


def write_in_file(file_path, data):
    with open(file_path, "w") as file:
        file.write(data)
    return


def download_img(web_page, img_source, dir_path):
    file_name = str(os.path.split(img_source)[-1])
    r = requests.get(web_page + img_source)
    total_path = dir_path + '/' + file_name
    with open(total_path, "wb") as code:
        code.write(r.content)
    return total_path
