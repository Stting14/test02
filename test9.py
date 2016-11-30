import urllib.request
import os

url = 'http://jandan.net/ooxx/'


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()

    return html


def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    return html[a:b]


def find_imgs(page_url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            print('=========================================='+html[a + 9:b + 4])
            img_addrs.append(html[a + 9:b + 4])
        else:
            b = a + 9

        a = html.find('img src=', b)

        return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]

        with open(filename, 'wb') as f:
            img = url_open(each)
            print('each===================================' + each)
            f.write(img)


def download_mm(folder='521', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'

        img_addrs = find_imgs(page_url)
     #  print('==========================================================' + img_addrs)
        save_imgs(folder,img_addrs)


if __name__ == '__main__':
    download_mm()
