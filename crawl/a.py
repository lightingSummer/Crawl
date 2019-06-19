import requests
import random
import re
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('https://www.qiushibaike.com/text/').content
    soup = BeautifulSoup(content, 'html.parser')
    for div in soup.find_all('div', {'class': 'content'}):
        print(div.text.strip())
        print('\n')


def list_test():
    l = [1, 2, 3]
    print(1, l)
    l.pop()
    print(2, l)


def demo_string():
    stra = "hello world"
    print(1, stra.capitalize())
    print(2, stra.replace(' ', '__'))
    strb = '   \n\rhello nowcoder \r\n  '
    print(3, strb.lstrip())
    print(4, strb.rstrip(), 'xx')
    strc = 'hello w'
    print(5, strc.startswith('he'))
    print(6, strc.endswith('w'))
    print(7, stra + strb + strc)
    print(8, len(strb))
    print(9, '-'.join([stra, strb.strip(), strc]))
    print(10, strc.split(' '))
    print(11, strc.find('llo'))


def demo_operation():
    print(1, max(1, 2))
    print(2, len('pppp'))
    print(3, range(1, 10, 2))
    print(4, abs(-2))
    x = 3
    print(5, eval('x*2+4'))
    print(6, divmod(11, 3))


def demo_control():
    score = 65
    if score > 99:
        print('A')
    elif score > 60:
        print('B')
    else:
        print('C')
    temp = 10
    while temp < 100:
        print(temp)
        temp += 10
    for i in range(0, 10):
        print(i * i)


def demo_list():
    list_a = [1, 2, 3, 'r']
    print(1, list_a)
    list_b = ['f', 'd']
    print(2, list_b)
    list_a.extend(list_b)
    print(3, list_a)
    print(4, 4 in list_a)
    print(5, len(list_a))
    print(6, list_b * 2)
    list_b.append('ddd')
    print(7, list_b)
    list_b.reverse()
    print(8, list_b)
    t = (1, 2, 3)
    print(9, t)
    print(10, t.count(2))


def add(a, b):
    return a + b


def demo_dict():
    dicta = {4: 17, '4': '55', '1': '333'}
    print(1, dicta)
    print(2, dicta.get('4'))
    print(3, dicta.get(1))
    for key, value in dicta.items():
        print(4, key, value)
    print(5, 5 in dicta, 4 in dicta)
    dicta[33] = add
    print(6, dicta[33](1, 2))


def demo_set():
    lista = [1, 2, 3]
    seta = set(lista)
    print(1, seta)
    setb = set((2, 3, 4))
    print(2, seta.intersection(setb))
    print(3, seta & setb)
    print(4, seta | setb)
    print(5, seta.isdisjoint(set(('a', 'b'))))


class User:
    type = 'User'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name + '|' + str(self.age)


class Admin(User):
    type = 'Admin'

    def __init__(self, name, age, num):
        User.__init__(self, name, age)
        self.num = num

    def __repr__(self):
        return self.name + '|' + str(self.age) + '|' + str(self.num)


def demo_object():
    user1 = User('Jim', 1)
    print(1, user1)
    admin1 = Admin('kimi', 2, 2)
    print(2, admin1)


def demo_exception():
    try:
        print(2 / 0)
    except Exception as e:
        print(e)
    finally:
        print('over')


def demo_random():
    print(1, random.randint(0, 11))
    print(2, random.choice(range(0, 100, 5)))
    print(3, random.sample(range(0, 100, 10), 5))
    lista = [1, 2, 3, 4, 5]
    random.shuffle(lista)
    print(4, lista)


def demo_regex():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    p2 = re.compile('\d')
    print(1, p1.findall(str))
    print(2, p2.findall(str))

    str = 'axxx@163.com,bcc@google.com,c@qq.com,d@qq.com,e@163.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print(3, p3.findall(str))

    str = '<html><h>title</h><body>content</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print(4, p4.findall(str))
    p4 = re.compile('<h>[^<]+</h><body>[^<]+</body>')
    print(5, p4.findall(str))

    str = 'xx2016-08-20zzz,xx2016-8-20zzz'
    p5 = re.compile('\d{4}-\d{2}-\d{2}')
    print(p5.findall(str))


if __name__ == '__main__':
    # qiushibaike()
    # print("aaa")
    # list_test()
    # demo_string()
    # demo_operation()
    # demo_control()
    # demo_list()
    # demo_dict()
    # demo_set()
    # demo_object()
    # demo_exception()
    # demo_random()
    demo_regex()
