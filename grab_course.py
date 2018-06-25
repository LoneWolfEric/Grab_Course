import requests
from bs4 import BeautifulSoup
import re

user_login = requests.session()

def login_in():

    zjh = input('请输入你的学号：')
    mm = input('请输入你的教务处密码：')

    url = 'http://zhjw.scu.edu.cn/loginAction.do'

    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie':'JSESSIONID=bcdyFntur0YE6-Ttl03qw',
        'Host':'zhjw.scu.edu.cn',
        'Origin':'http://zhjw.scu.edu.cn',
        'Referer':'http://zhjw.scu.edu.cn/login.jsp'
    }

    data = {
        'zjh': '2016141442100',
        'mm': '081318'
    }

    user_login.post(url, data = data, headers = headers)        #登录教务处
    print('登录成功')

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

    user_info = user_login.get(url, headers = name_headers)     #获取个人信息
    html = user_info.content.decode('gbk')

    user_name = re.findall(r'欢迎光临&nbsp;.{0,6}&nbsp;', html)
    user_name = user_name[0]
    num = user_name.rindex('&nbsp;')
    user_name = user_name[10: num]

    print('你好，%s!' %(user_name))



def main():
    login_in()
    show_user_info()

if __name__ == '__main__':
    main()