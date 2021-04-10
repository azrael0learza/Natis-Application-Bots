##https://github.com/azrael0learza##

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

def waittimer():
    time.sleep(2)


###Change following values below for input fields on site
#Options available for (TestingType) are ['reg' (REG NO CERTIFICATE), 'rsa' (RSA INDENTITY DOCUMENT), 'for' (FOREIGN IDENTITY DOCUMENT)]
#Options available for (licenseCode) are ['1 -' (MOTOR CYCLE), '2 -' (MV NOT EXCEEDING 3500 KG (EXCLUDING MC)), '3 -' (MOTOR VEHICLE (EXCLUDING MC))]
IdentityNo = 'Pass'
SurnameOp = 'Pass'
InitialsOp = 'Pass'
licenseCode = 'Pass'
TestingType = 'Pass'



#Website & Wait Timer For Loading
driver.get("https://online.natis.gov.za/#/")

waittimer()


#Region Selection [Replace Xpath with regoin desired]
#1#Continue To Booking
#2#Service Selection [Choose Service desired using Xpath]
element = driver.find_element_by_xpath('//*[@id="ZA-GT"]')
hover = ActionChains(driver).move_to_element(element)
hover.perform()
element.click()

waittimer()
#1#
driver.find_element_by_xpath('//*[@id="alertModal"]/div/div/div[3]/button').click()

waittimer()
#2#
driver.find_element_by_xpath('//*[@id="main-view"]/div[4]/div[2]/div[1]/div/div[1]/div/a/h5').click()

waittimer()


#Selection & Adding Information - 1
driver.find_element_by_xpath('//*[@id="PrebookingForm"]/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/label[1]').click()

waittimer()

testtype = driver.find_element_by_xpath('//*[@id="s2id_dlTstLicType"]/a')
hoversel = ActionChains(driver).move_to_element(testtype)
hoversel.perform()
testtype.click()

waittimer()

#Selection & Adding Information - 2
#Options available ... Please see Line 18
#Default set to '3 - M'
licode = driver.find_element_by_xpath('//*[@id="s2id_autogen4_search"]')
licode.send_keys(licenseCode)

waittimer()

licode.send_keys(Keys.RETURN)
waittimer()


#Selection & Adding Information - 3
#Options available ... Please see Line 17
#Default set to 'rsa i'
testtype2 = driver.find_element_by_xpath('//*[@id="s2id_idDocTypeCd"]')
hoversel2 = ActionChains(driver).move_to_element(testtype2)
hoversel2.perform()
testtype2.click()

waittimer()

idty = driver.find_element_by_xpath('//*[@id="s2id_autogen6_search"]')
idty.send_keys(TestingType)

waittimer()

idty.send_keys(Keys.RETURN)
waittimer()


##Selection & Adding Information - 4
##Identification Number
idno = driver.find_element_by_id('idDocN')
idno.send_keys(IdentityNo)

waittimer()
idno.send_keys(Keys.RETURN)

waittimer()

##Surname
idsurn = driver.find_element_by_id('surname')
idsurn.send_keys(SurnameOp)

waittimer()
idsurn.send_keys(Keys.RETURN)

waittimer()

##Initials
idini = driver.find_element_by_id('initials')
idini.send_keys(InitialsOp)

waittimer()
idini.send_keys(Keys.RETURN)

waittimer()


##Are you a Robot?...
##As of Recpatcha v3, the best solutions are: 
##2captcha & anti-gate.com

#This section will be commented out for the time bieng.

##switch to recaptcha frame

#frames = driver.find_elements_by_xpath('//*[@id="Verification"]/div/div/iframe')
#driver.switch_to.frame(frames[0]);
#waittimer()

##click on checkbox to activate recaptcha

#driver.find_element_by_class_name("recaptcha-checkbox-border").click()
#click audio challenge option
#driver.find_elements_by_class_name('rc-button goog-inline-block rc-button-audio').click()



