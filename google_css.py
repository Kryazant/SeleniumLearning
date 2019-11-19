import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

driver.find_element_by_id('fsettl').click() #Настройки
time.sleep(0.5)
driver.find_element_by_partial_link_text('История').click() #История
time.sleep(0.5)
driver.find_element_by_class_name('history-switch').click() #Свич
time.sleep(0.5)

driver.get("https://www.google.com")

driver.find_element_by_class_name('hOoLGe').click() #Экранная клавиатура
time.sleep(0.5)

driver.find_element_by_id('K71').click() #п
time.sleep(0.5)
driver.find_element_by_id('K72').click() #р
time.sleep(0.5)
i = driver.find_element_by_id('K66').click() #и
time.sleep(0.5)
v = driver.find_element_by_id('K68').click() #в
time.sleep(0.5)
e = driver.find_element_by_id('K84').click()#е
time.sleep(0.5)
t = driver.find_element_by_id('K78').click()#т
time.sleep(1)

driver.find_element_by_class_name('vk-t-btn-o.vk-sf-cl').click() #Закрыть клавиатуру
time.sleep(1)
#driver.find_element_by_class_name('gNO89b').click() #Поиск 
driver.find_element_by_xpath("//div[@class='FPdoLc tfB0Bf']//input[@class='gNO89b']").click()
time.sleep(1)

driver.get("https://www.google.com")


#driver.quit()
