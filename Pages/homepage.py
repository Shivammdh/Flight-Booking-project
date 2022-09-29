import time
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from Locators.locators import PageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites.BasePage import selection
class FromDestination:
    def __init__(self,driver):
        self.driver=driver
        self.flightbtn=PageLocators.flightbtn
        self.cityinput=PageLocators.cityinput
        self.fromcitys=PageLocators.fromcitys

    def fromdest(self,City):
        self.driver.find_element(By.XPATH,self.flightbtn).click()
        self.driver.find_element(By.CSS_SELECTOR, self.cityinput).send_keys(City)
        fromcitys = self.driver.find_elements(By.XPATH, self.fromcitys)
        selection(fromcitys,City)

class ToDestination:
    def __init__(self,driver):
        self.driver=driver
        self.toinput=PageLocators.toinput
        self.tocitys=PageLocators.tocitys

    def todest(self,City):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.toinput).send_keys(City)
            time.sleep(2)
            tocitys = self.driver.find_elements(By.XPATH, self.tocitys)
            selection(tocitys,City)
        except NoSuchElementException:
            print('Such element Not found.')


class Calender:
    def __init__(self,driver):
        self.driver=driver
        # self.calaendbtn = PageLocators.calaendbtn
        self.datebtn = PageLocators.datebtn
        self.cookie=PageLocators.cookie

    def travelldate(self):
        try:
            # self.driver.find_element(By.XPATH,self.calaendbtn).click()
            dates = self.driver.find_element(By.ID,self.datebtn)
            dates.clear()
            dates.send_keys("08-08-2022")
        except NoSuchElementException:
            print('Such element not found.')
    def clearcokkies(self):
        try:
            self.driver.find_element(By.ID, self.cookie).click()

        except NoSuchElementException:
            print('Such element not found.')
        except ElementClickInterceptedException:
            print('Element Click Intercepted.')
        except Exception:
            print("Any Other Exception Occured.")

class Travellers:
    def __init__(self,driver):
        self.driver=driver
        self.pasengerbtn = PageLocators.pasengerbtn
        self.adultbtn=PageLocators.adultbtn
        self.childbtn=PageLocators.childbtn
        self.infantbtn=PageLocators.infantbtn

    def Adult(self):
        try:
            self.driver.find_element(By.XPATH,self.pasengerbtn).click()
            # Add Adults for traveling
            adltum = int(input("Enter how many adult you want to enter:"))
            for i in range(adltum):
                self.driver.find_element(By.XPATH,self.adultbtn).click()
        except ElementClickInterceptedException:
            print("Element Click Intercepted this time.")
        except NoSuchElementException:
            print("Such element is not found.")
        except IndexError:
            print('Index out of range')
        except ValueError:
            print("Please enter Integer Number")
        except Exception:
            print("Any Other Exception Occured.")

    def child(self):
        try:
            childnum = int(input("Enter how many children you want to enter:"))
            for i in range(childnum):
                self.driver.find_element(By.XPATH,self.childbtn).click()
        except ElementClickInterceptedException:
            print("Element Click Intercepted this time.")
        except NoSuchElementException:
            print("Such element is not found.")
        except IndexError:
            print('Index out of range')
        except ValueError:
            print("Please enter Integer Number")
        except Exception:
            print("Any Other Exception Occured.")

    def Infant(self):
        try:

            infnum = int(input("Enter how many Infants you want to enter:"))
            for i in range(infnum):
                self.driver.find_element(By.XPATH,self.infantbtn).click()
        except ElementClickInterceptedException:
            print("Element Click Intercepted this time.")
        except NoSuchElementException:
            print("Such element is not found.")
        except IndexError:
            print('Index out of range')
        except ValueError:
            print("Please enter Integer Number")
        except Exception:
            print("Any Other Exception Occured.")
class FlightBook:
    def __init__(self,driver):
        self.driver=driver
        self.searchbtn=PageLocators.searchbtn
        self.bookbtn=PageLocators.bookbtn

    def flightbook(self):
        try:
            self.driver.find_element(By.ID,self.searchbtn).click()
            wait = WebDriverWait(self.driver, 40)
            elem = wait.until(EC.presence_of_element_located((By.XPATH, self.bookbtn)))
            elem.click()
        except TimeoutException:
            print("It's take time more than 20")
        except NoSuchElementException:
            print('Such Element Not Found')
        except ElementClickInterceptedException:
            print("Element Click Intercepted this time.")
        except Exception:
            print("Any Other Exception Occured.")




