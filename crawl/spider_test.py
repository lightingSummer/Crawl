from pyquery import PyQuery

if __name__ == '__main__':
    q = PyQuery(open('zhihu_test.html', 'r', encoding='UTF-8').read())
    print(q('title').text())

    for each in q('div.RichContent-inner>span').items():
        print(each.html())
