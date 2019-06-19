from pyquery import PyQuery

if __name__ == '__main__':
    q = PyQuery(open('bilibili.html', 'r', encoding='UTF-8').read())
    print(q('title').text())
    print(q('.h-basic').html())
    print(q('#h-name').text())
