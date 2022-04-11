#!/usr/bin/env python3
from page_loader.cli import get_arg_parser
from page_loader.path_handler import make_result_path
from page_loader.path_handler import create_dir
from page_loader.data_handler import download_data
from page_loader.data_handler import download_img
from page_loader.data_handler import write_in_file

import os
from bs4 import BeautifulSoup


def download(web_page, output_path):
    file_path, dir_path = make_result_path(web_page, output_path)
    html_data = download_data(web_page)
    create_dir(dir_path)

    soup = BeautifulSoup(html_data, 'html.parser')
    for link in soup.find_all('img'):
        img_path = download_img(web_page, link['src'], dir_path)
        link['src'] = img_path
    write_in_file(file_path, soup.prettify(formatter="minimal"))

    print('DIR_PATH', dir_path)
    print('RES_PATH', file_path)
    return file_path


def main():
    args = get_arg_parser()
    output_path = args.output
    web_page = args.web_page
    download(web_page, output_path)


if __name__ == '__main__':
    main()
