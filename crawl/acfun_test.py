from pyquery import PyQuery

if __name__ == '__main__':
    q = PyQuery(open('acfun.html', 'r', encoding='UTF-8').read())
    print(q('title').text())
    src = q('div.cover>div.img').attr('style')
    head_url = src.replace('background:url(\'', '').replace('\') 0% 0% / 100% no-repeat', '')
    print(head_url)
    print(q('div.clearfix>div.name.fl.text-overflow').text())
