import requests
from bs4 import BeautifulSoup
import re
import time
import random

user_login = requests.session()

# 登录教务处
def login_in():
    while True:
        zjh = str(input('请输入你的学号：'))
        mm = str(input('请输入你的教务处密码：'))

        url = 'http://zhjw.scu.edu.cn/loginAction.do'

        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            'Cookie':'JSESSIONID=bcdyFntur0YE6-Ttl03qw',
            'Host':'zhjw.scu.edu.cn',
            'Origin':'http://zhjw.scu.edu.cn',
            'Referer':'http://zhjw.scu.edu.cn/login.jsp'
        }

        data = {
            'zjh': zjh,
            'mm': mm
        }

        response = user_login.post(url, data = data, headers = headers)          # 登录教务处

        isError  = re.findall(r'<td class="errorTop">', response.content.decode('gbk'))

        if isError:                             # 判断账号密码是否正确
            print('账号或者密码错误，请重新输入！')
        else:
            print('登录成功')
            break

# 显示用户名称           
def show_user_info():
    url = 'http://zhjw.scu.edu.cn/menu/s_top.jsp'

    name_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=bcdyFntur0YE6-Ttl03qw',
    'Host': 'zhjw.scu.edu.cn',
    'Referer': 'http://zhjw.scu.edu.cn/loginAction.do',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }

    user_info = user_login.get(url, headers = name_headers)     # 获取个人信息
    html = user_info.content.decode('gbk')

    user_name = re.findall(r'欢迎光临&nbsp;.{0,6}&nbsp;', html)
    user_name = user_name[0]
    num = user_name.rindex('&nbsp;')
    user_name = user_name[10: num]

    print('你好，%s!' %(user_name))                             # 显示个人信息

# 查询要强的课的信息
def get_course_info():
    pass

# 抢课
def grab_course():
    pass


def main():
    login_in()
    show_user_info()
    get_course_info()
    while True:
        time.sleep(random.uniform(2, 6))
        grab_course()
    print('抢课成功')


if __name__ == '__main__':
    main()
