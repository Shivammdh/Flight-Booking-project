from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

from Locators.locators import Passengerloc as ps
from utilites.BasePage import selectelem

class PassengerForm:
    def __init__(self,driver):
        self.driver=driver
        self.email=ps.email
        self.phonecoun=ps.phonecoun
        self.phone=ps.phone
        self.fname1=ps.fname
        self.lname1=ps.lname
        self.nation=ps.nation
        self.month1=ps.month
        self.day1=ps.day
        self.year1=ps.year
        self.passportno=ps.passportno
        self.exmonth = ps.exmonth
        self.exday = ps.exday
        self.exyear = ps.exyear

    def fillAdultdetail(self):
        try:

            self.driver.find_element(By.XPATH, self.fname1).send_keys("Shivam")
            self.driver.find_element(By.XPATH, self.lname1).send_keys("Sharma")
            nation = self.driver.find_element(By.XPATH, self.nation)
            selectelem(nation,"India")
            day = self.driver.find_element(By.XPATH, self.day1).send_keys('01')
            month = self.driver.find_element(By.XPATH, self.month1)
            selectelem(month,"May")
            self.driver.find_element(By.XPATH,self.year1).send_keys('1997')
        except NoSuchElementException:
            print('Such element Not found.')

    def fillPassportNumber(self,passnum):
        try:
            self.driver.find_element(By.XPATH, self.passportno).send_keys(passnum)
        except NoSuchElementException:
            print('Such element Not found.')

    def Contact_details(self):
        try:
            driver=self.driver
            driver.find_element(By.XPATH, self.email).send_keys("shivamsharmamdh@gmail.com")
            elem = driver.find_element(By.XPATH, self.phonecoun)
            select = Select(elem)
            select.select_by_value('in')
            driver.find_element(By.XPATH, self.phone).send_keys("9589576566")
        except NoSuchElementException:
            print("Such element not found")


    def fillPassportExpier(self):
        try:

            self.driver.find_element(By.XPATH, self.exday).send_keys('01')
            exmonth = self.driver.find_element(By.XPATH, self.exmonth)
            selectelem(exmonth,"January")

            self.driver.find_element(By.XPATH, self.exyear).send_keys('2040')
        except NoSuchElementException:
            print('Such element Not found.')











