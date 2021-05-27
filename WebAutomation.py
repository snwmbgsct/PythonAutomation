from calendar import calendar
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import datetime
import re

from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui



date = datetime.date.today()
day = date.day
month = date.month
year = date.year
transdate = ("%d/%d/%d" % (year, month, day))
todaytime=str(datetime.datetime.now().year)+"/"+str(datetime.datetime.now().month)+"/"+str(datetime.datetime.now().day)
url = "https://docs.qq.com/sheet/DV1NuY1VqaXBDTEh5"  ##


driver = webdriver.Chrome()
driver.get(url)

time.sleep(2)
#自动登入的功能
elmet = driver.find_element_by_id("header-login-btn")  #blankpage-button-pc
elmet.click()
driver.implicitly_wait(5)
driver.switch_to.frame("login_frame")
try:
    elmet = driver.find_element_by_id("img_out_7777777")
    elmet.click()
    time.sleep(2)
    print("快捷登录成功")
    print(transdate)

except:
    driver.find_element_by_id("switcher_plogin").click()
    time.sleep(1)
    driver.find_element_by_id("u").send_keys("7777777")  # qq
    driver.find_element_by_id("p").send_keys("password")  # 密码
    driver.find_element_by_id("login_button").click()
    print("账号登录成功")
time.sleep(1)




driver.find_element_by_class_name('fullscreenbar__button').click()

driver.find_element_by_xpath('//*[@id="sheetbar"]/div[2]/div[3]/div/div[2]/span').click()
time.sleep(3)

driver.find_element_by_id('sheet-search-button').click()



time.sleep(1)


wait = ui.WebDriverWait(driver,100)
wait.until(lambda driver: driver.find_element_by_id("search-panel-input"))
time.sleep(1)
driver.find_element_by_id("search-panel-input").click()
driver.find_element_by_id("search-panel-input").send_keys(str(todaytime))
time.sleep(1)
driver.find_element_by_class_name('dui-modal-close').click()
time.sleep(1)



for i in range(82):
    driver.find_element_by_class_name('operate-board').send_keys(Keys.DOWN)

driver.find_element_by_id('alloy-simple-text-editor').click()
driver.find_element_by_id('alloy-simple-text-editor').send_keys(str(36.3))
driver.find_element_by_id('alloy-simple-text-editor').send_keys(Keys.ENTER)
driver.find_element_by_id('alloy-simple-text-editor').send_keys(Keys.RIGHT)
driver.find_element_by_id('alloy-simple-text-editor').send_keys(Keys.UP)
driver.find_element_by_id('alloy-simple-text-editor').click()
driver.find_element_by_id('alloy-simple-text-editor').send_keys(str(36.3))
driver.find_element_by_id('alloy-simple-text-editor').send_keys(Keys.ENTER)
driver.find_element_by_id('alloy-simple-text-editor').send_keys(Keys.RIGHT)



time.sleep(5)


driver.quit()
print("success")
