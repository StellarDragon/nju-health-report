from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import json


username = ''       # 用户名
password = ''       # 密码（请勿输错，否则下次身份认证会需要验证码。解决策略是在电脑上手动进行一次统一认证）
curr_location = ''  # 打卡地点

def fillOneForm(wid):
    info = '&IS_TWZC=1&IS_HAS_JKQK=1&JRSKMYS=1&JZRJRSKMYS=1' # 分别对应四个单选框的值
    link = 'http://ehallapp.nju.edu.cn/xgfw/sys/yqfxmrjkdkappnju/apply/saveApplyInfos.do?WID={wid}&CURR_LOCATION={curr_location}'
    link = link.format(wid=wid, curr_location=curr_location) + info
    driver.get(link)

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ss = soup.select('pre')[0]
    res = json.loads(ss.text)
    if res['code'] == '0':
        if res['msg'] == '成功':
            return 'Success!'
    return 'Failed.'
    

def fillTheForms(res):
#   for form in res:              # 填写所有未填写的表单
#       if form['TBZT'] == '0':
#           print('Date: ' + form['TBRQ'] + '  ' + fillOneForm(form['WID']))

    form = res[0]                 # 默认只填写最上面的（当天）
    if form['TBZT'] == '0':       # 如果未填报
        print('Date: ' + form['TBRQ'] + '  ' + fillOneForm(form['WID']))


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')                                         # 无窗口
    options.add_argument('blink-settings=imagesEnabled=false')                 # 不加载图片
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 开发者模式
    options.add_argument('log-level=3')                                        # 不显示日志
    driver = webdriver.Chrome(options=options)
    
    driver.get('https://authserver.nju.edu.cn/authserver/login')
    while True:
        try:
            element = WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.ID,"username")))
        finally:
            break

    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("auth_login_btn").click()

    driver.get('http://ehallapp.nju.edu.cn/xgfw/sys/yqfxmrjkdkappnju/apply/getApplyInfoList.do')

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ss = soup.select('pre')[0]
    res = json.loads(ss.text)

    if res['code'] == '0':
        if res['msg'] == '成功':
            fillTheForms(res['data'])

    # driver.get('http://ehallapp.nju.edu.cn/xgfw/sys/mrjkdkappnju/index.html')
    # driver.get('http://ehallapp.nju.edu.cn/xgfw/sys/yqfxmrjkdkappnju/apply/getApplyInfoList.do')
    print('Completed')
    driver.quit()
