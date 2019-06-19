from pyquery import PyQuery

if __name__ == '__main__':
    q = PyQuery(open('d.html', 'r', encoding='UTF-8').read())
    print(q('title').text())

    for each in q('div.inner>a').items():
        if each.attr.href.find('tab') > 0:
            print(1, each.attr.href)

    for each in q('#Tabs>a').items():
        print(2, each.attr.href)

    for each in q('.cell>a[href^= "/go/"]').items():
        print(3, each.attr.href)

    for each in q('.cell a[href^= "/go/"]').items():
        print(4, each.attr.href)

    for each in q('span.item_title>a').items():
        print(5, each.html())

    for each in q('span.item_title>a').items():
        print(5, each.html())

    for each in q('a>img').items():
        print(6, each.attr.src)
