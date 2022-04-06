from page_loader.scripts.page_loader import download


def test_download():
    dir_path = '/var/tmp'
    web_page = 'https://ru.hexlet.io/courses'
    total_path = download(web_page, dir_path)
    assert '/var/tmp/ru-hexlet-io-courses.html' == total_path
