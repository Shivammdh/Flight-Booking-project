import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import logging
from selenium.webdriver.common.by import By
from Pages.homepage import FromDestination,ToDestination,Calender,Travellers,FlightBook
from utilites.BasePage import windowSwitch
from Pages.Travellersdetails import PassengerForm
from utilites.argupass import browser

class TestFlight(unittest.TestCase):
    def setUp(self) -> None:
        if browser == 'chrome':
            s = Service('D:\chromedriver_win32\chromedriver.exe')
            self.driver = webdriver.Chrome(service=s)
            self.driver.implicitly_wait(30)
            self.driver.get("https://phptravels.net/")
            logging.basicConfig(filename='FlightBooking.log',
                                filemode='w',
                                level=logging.DEBUG,
                                format='%(asctime)s %(levelname)s %(message)s',
                                force=True)
            self.log=logging.getLogger()
            self.log.info("Start Execution on Chrome Browser..")


        elif browser == 'firefox':
            s = Service('D:\Selenium\geckodriver.exe')
            self.driver = webdriver.Firefox(service=s)
            self.driver.implicitly_wait(30)
            self.driver.get("https://phptravels.net/")
            logging.basicConfig(filename='FlightBooking.log',
                                filemode='w',
                                level=logging.DEBUG,
                                format='%(asctime)s %(levelname)s %(message)s',
                                force=True)
            self.log = logging.getLogger()
            self.log.info("Start Execution on FireFox Browser..")

        elif browser == 'edge':
            s = Service('D:\Selenium\msedgedriver.exe')
            self.driver = webdriver.Edge(service=s)
            self.driver.implicitly_wait(30)
            self.driver.get("https://phptravels.net/")
            logging.basicConfig(filename='FlightBooking.log',
                                filemode='w',
                                level=logging.DEBUG,
                                format='%(asctime)s %(levelname)s %(message)s',
                                force=True)
            self.log = logging.getLogger()
            self.log.info("Start Execution on edge Browser..")

        else:
            s = Service('D:\chromedriver_win32\chromedriver.exe')
            self.driver = webdriver.Chrome(service=s)
            self.driver.implicitly_wait(30)
            self.driver.get("https://phptravels.net/")
            logging.basicConfig(filename='FlightBooking.log',
                                filemode='w',
                                level=logging.DEBUG,
                                format='%(asctime)s-%(levelname)s|%(message)s',
                                force=True)
            self.log = logging.getLogger()


    def testpage(self):
        log=self.log
        driver=self.driver
        driver.get("https://phptravels.net/")
        log.info('Hit the url...')
        # From destination selection
        driver.find_element(By.ID,'languages').click()
        driver.find_element(By.XPATH,"//ul[@class='dropdown-menu show']/li[9]/a").click()
        time.sleep(2)
        fd=FromDestination(driver)
        fd.fromdest("Bhopal")
        log.info('Enter From city is Bhopal')
        # To Destination Selection
        td=ToDestination(driver)
        td.todest("Pune")
        log.info('Enter To city is Pune')
        # Date of journey selection
        cl=Calender(driver)
        cl.travelldate()
        log.info('Successfully Entered Date of journy')
        # Number of Travellers selection
        cl.clearcokkies()
        tv=Travellers(driver)

        # Add Adults for traveling
        tv.Adult()

        time.sleep(2)
        log.info('Adding Adults')
        # Add Children for traveling
        tv.child()

        time.sleep(2)
        # Add Infants for traveling
        log.info('Adding Child')
        tv.Infant()
        # Search flight
        time.sleep(2)
        log.info('Adding Infants')

        fb=FlightBook(driver)
        fb.flightbook()
        log.info('Successfully select flight')
        time.sleep(5)
        windowSwitch(driver)
        tit=driver.title
        log.info(f"Switch To {tit} window.")
        time.sleep(2)
        driver.find_element(By.ID,'cookies_accept').click()
        time.sleep(2)
        ps = PassengerForm(driver)
        ps.Contact_details()
        log.info('Select country India.')

        ps.fillAdultdetail()
        #
        ps.fillPassportNumber("123456")

        ps.fillPassportExpier()
        log.info('Successfully Pass.....')

    def tearDown(self) -> None:
        self.log.warning('Driver going to close..')
        self.driver.close()



