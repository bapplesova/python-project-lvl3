#!/usr/bin/env python3
from page_loader.cli import get_arg_parser
import os
import re
import requests


def download(web_page, output_path):
    result_path = make_result_path(web_page, output_path)
    r = requests.get(web_page)
    f = open(result_path, "w")
    f.write(r.text)
    f.close()
    return result_path


def main():
    args = get_arg_parser()
    output_path = args.output
    web_page = args.web_page
    result_path = download(web_page, output_path)
#    print('output_f', output_path)
#    print('web_page', web_page)
    print('result_path', result_path)


def make_result_path(web_page, output_path):
    count_parts = web_page.count('/')
    web_page_tmp = os.path.splitext(web_page)[0]
    total_path = ''
    while count_parts != 1:
        count_parts -= 1
        addr = os.path.split(web_page_tmp)
        total_path = addr[-1] + '-' + total_path
        web_page_tmp = addr[0]
    total_path = re.sub('[^a-zA-Z0-9]', '-', total_path)[:-1]
    total_path = output_path + '/' + total_path + '.html'
    return total_path


if __name__ == '__main__':
    main()
