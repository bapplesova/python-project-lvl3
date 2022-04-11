import argparse
import os


def get_arg_parser():
    parser = argparse.ArgumentParser(description='Page Loader')
    parser.add_argument('-o', '--output', default=os.getcwd(),
                        help='put download page in dir '
                             '(default: current working dir)')
    parser.add_argument('web_page')
    args = parser.parse_args()
    return args
