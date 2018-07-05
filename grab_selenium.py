from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chrome_options = chrome_options, executable_path = chromedriver)
# driver = webdriver.Chrome(executable_path=chromedriver)

# print(driver.page_source)
#driver.save_screenshot('screen.png')

url = 'http://zhjw.scu.edu.cn/login.jsp'
driver.get(url)
# driver.find_element_by_xpath.clear()
account = driver.find_elements_by_name('zjh')
account[0].send_keys('2016141442100')
password = driver.find_element_by_name('mm')
password.send_keys('081318')

driver.save_screenshot('1.png')
driver.find_element_by_xpath('//*[@id="btnSure"]').click()
driver.save_screenshot('2.png')

print(driver.current_url)

driver.quit()