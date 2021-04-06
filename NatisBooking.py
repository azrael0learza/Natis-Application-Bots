#Code by Kagiso.S

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


PATH = "E:\programs\standard\chromedriver.exe"
driver = webdriver.Chrome(PATH)


#Website & Wait Timer For Loading
driver.get("https://online.natis.gov.za/#/")

time.sleep(1)


#Region Selection [Replace Xpath with regoin desired]
element = driver.find_element_by_xpath('//*[@id="ZA-GT"]')
hover = ActionChains(driver).move_to_element(element)
hover.perform()
element.click()

time.sleep(1)


#Continue To Booking
button = driver.find_element_by_xpath('//*[@id="alertModal"]/div/div/div[3]/button')
button.click()

time.sleep(1)


#Service Selection [Choose Service desired using Xpath]
learn = driver.find_element_by_xpath('//*[@id="main-view"]/div[4]/div[2]/div[1]/div/div[1]/div/a/h5')
learn.click()

time.sleep(1)


#Selection & Adding Information - 1
single = driver.find_element_by_xpath('//*[@id="PrebookingForm"]/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/label[1]')
single.click()

time.sleep(1)

testtype = driver.find_element_by_xpath('//*[@id="s2id_dlTstLicType"]/a')
hoversel = ActionChains(driver).move_to_element(testtype)
hoversel.perform()
testtype.click()

time.sleep(1)

#Selection & Adding Information - 2
#Options available are ['1 -' MOTOR CYCLE, '2 -' MV NOT EXCEEDING 3500 KG (EXCLUDING MC), '3 -' MOTOR VEHICLE (EXCLUDING MC)]
#Default set to '3 -'
licode = driver.find_element_by_xpath('//*[@id="page-top"]')
licode.send_keys('3 -')

time.sleep(2)

licode.send_keys(Keys.RETURN)
time.sleep(1)


#Selection & Adding Information - 3
#Options available are ['reg' REG NO CERTIFICATE, 'rsa' RSA INDENTITY DOCUMENT, 'for' FOREIGN IDENTITY DOCUMENT]
#Default set to 'rsa i'
testtype2 = driver.find_element_by_xpath('//*[@id="s2id_idDocTypeCd"]')
hoversel2 = ActionChains(driver).move_to_element(testtype2)
hoversel2.perform()
testtype2.click()

time.sleep(1)

idty = driver.find_element_by_xpath('//*[@id="page-top"]')
idty.send_keys('rsa i')

time.sleep(2)

idty.send_keys(Keys.RETURN)
time.sleep(2)


##Selection & Adding Information - 4
##Identification Number
idno = driver.find_element_by_id('idDocN')
idno.send_keys('0000000000000')

time.sleep(2)
idno.send_keys(Keys.RETURN)

time.sleep(2)

##Surname
idsurn = driver.find_element_by_id('surname')
idsurn.send_keys('TESTTEST')

time.sleep(2)
idsurn.send_keys(Keys.RETURN)

time.sleep(2)

##Initials
idini = driver.find_element_by_id('initials')
idini.send_keys('TT')

time.sleep(2)
idini.send_keys(Keys.RETURN)

time.sleep(2)


##Are you a Robot?...

#switch to recaptcha frame
frames = driver.find_elements_by_xpath('//*[@id="Verification"]/div/div/iframe')
driver.switch_to.frame(frames[0]);
time.sleep(3)
#click on checkbox to activate recaptcha
driver.find_element_by_class_name("recaptcha-checkbox-border").click()



