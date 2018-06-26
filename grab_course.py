import requests
from bs4 import BeautifulSoup
import re
import time
import random

user_login = requests.session()
user_name = '你的名字'

# 登录教务处
def login_in():
    while True:
        # zjh = str(input('请输入你的学号：'))
        # mm = str(input('请输入你的教务处密码：'))

        url = 'http://zhjw.scu.edu.cn/loginAction.do'

        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            # 'Cookie':'JSESSIONID=bcdyFntur0YE6-Ttl03qw',
            'Host':'zhjw.scu.edu.cn',
            'Origin':'http://zhjw.scu.edu.cn',
            'Referer':'http://zhjw.scu.edu.cn/login.jsp'
        }

        # data = {
        #     'zjh': zjh,
        #     'mm': mm
        # }
        data = {
            'zjh': '2016141442100',
            'mm': '081318'
        }
        try:
            response = user_login.post(url, data = data, headers = headers)          # 登录教务处
            # response = requests.post(url, data = data, headers = headers)          # 登录教务处
        except ConnectionError:
            print('网络连接登录错误')
        except TimeoutError:
            print('访问超时登录错误')
            
        

        isError  = re.findall(r'<td class="errorTop">', response.content.decode('gbk'))

        if isError:                             # 判断账号密码是否正确
            print('账号或者密码错误，请重新输入！')
        else:
            print('登录成功')
            break

# 显示用户名称           
def show_user_info():
    url = 'http://zhjw.scu.edu.cn/menu/s_top.jsp'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'JSESSIONID=bcdyFntur0YE6-Ttl03qw',
        'Host': 'zhjw.scu.edu.cn',
        'Referer': 'http://zhjw.scu.edu.cn/loginAction.do',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }

    user_info = user_login.get(url, headers = headers)     # 获取个人信息
    # user_info = requests.get(url, headers = headers)     # 获取个人信息
    html = user_info.content.decode('gbk')
    # print(html)
    user_name = re.findall(r'欢迎光临&nbsp;.{0,6}&nbsp;', html)
    
    try:
        user_name = user_name[0]
        num = user_name.rindex('&nbsp;')
        user_name = user_name[10: num]
        print('你好，%s!' %(user_name))                             # 显示个人信息
    except  IndexError:
        print('获取信息失败')

    
# 查询要强的课的信息
def get_course_info():
    pass

# 抢课
def grab_course():
    url = 'http://zhjw.scu.edu.cn/xkAction.do'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '46',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'JSESSIONID=abdAG-4FkMWLO-STSP5qw',
        'Host': 'zhjw.scu.edu.cn',
        'Origin': 'http://zhjw.scu.edu.cn',
        'Referer': 'http://zhjw.scu.edu.cn/xkAction.do?actionType=3&pageNumber=-1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }

    data = {
            'kcId': '102396020_01',
            'preActionType': '3',
            'actionType': '9'
    }

    response = user_login.post(url, data = data, headers = headers)
    html = response.content.decode('gbk')
    print(html)

    # print(response.status_code)
    isSuccess = re.findall(r'<strong><font color="#990000">选课成功！</font></strong>', html)
    if isSuccess:
        print(isSuccess)
        return 1






def main():
    login_in()
    show_user_info()
    get_course_info()
    while True:
        time.sleep(random.uniform(2, 6))
        if (grab_course() == 1):
            break
        print('抢课中')

    print('抢课成功')


if __name__ == '__main__':
    main()
