from selenium import webdriver
from getpass import getpass
from time import sleep
import pandas as pd
import html5lib

#source for this code - https://github.com/adilshehzad786/Python-Selenium-GitHub-Actions/blob/main/scraper.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
#from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
#from pyvirtualdisplay import Display
#display = Display(visible=120, size=(800, 800))
#display.start()
chromedriver_autoinstaller.install()

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#driver = webdriver.Chrome(r"C:\Users\py144453\Downloads\chromedriver_win32 (3)\chromedriver.exe")
#driver.implicitly_wait(10)
#sleep(5)
#Quarter
chrome_options = Options()
options = [
    #"--window-size=1200,1200"
    #"--ignore-certificate-errors"
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(options=chrome_options)

name = 'Wipro'
def fundamental(name):
    #driver = webdriver.Chrome(r"C:\Users\py144453\Downloads\chromedriver_win32 (3)\chromedriver.exe")
    #nam = 'Wipro'
    try:
        driver.get(f'https://www.screener.in/company/{name}/consolidated/')
    except:
        driver.get(f'https://www.screener.in/company/{name}/')
    #else:
    #    print("Stock details not available at the moment try please search other stock")
    driver.maximize_window()
    sleep(3)
    '''for i in range(20):
        try:
            #sleep(1)
            driver.find_element_by_xpath(f'//*[@id="quarters"]/div[3]/table/tbody/tr[{i}]/td[1]/button').click()
            sleep(2)
        except:
            pass
        #//*[@id="profit-loss"]/div[3]/table/tbody/tr[10]/td[1]/button
    #sleep(3)
    #Yearly
    for i in range(20):
        try:
            #sleep(1)
            driver.find_element_by_xpath(f'//*[@id="profit-loss"]/div[3]/table/tbody/tr[{i}]/td[1]/button').click()
            sleep(2)
        except:
            pass
    #BS
    #sleep(3)
    for i in range(40):
        try:
            #sleep(1)
            driver.find_element_by_xpath(f'//*[@id="balance-sheet"]/div[2]/table/tbody/tr[{i}]/td[1]/button').click()
            sleep(2)
        except:
            pass
    #Cash_flow

    for i in range(40):
        try:
            #sleep(1)
            driver.find_element_by_xpath(f'//*[@id="cash-flow"]/div[2]/table/tbody/tr[{i}]/td[1]/button').click()
            sleep(2)
        except:
            pass

    #SH
    #for i in range(100):
    #    try:
    #        sleep(0.5)
    #        driver.find_element_by_xpath(f'//*[@id="shareholding"]/div[2]/table/tbody/tr[{i}]/td[1]/button').click()
    #        sleep(0.5)
    #    except:
    #        pass
'''
    ht = driver.page_source
    data = pd.read_html(ht)

    y_data = pd.concat([data[2],data[7],data[8],data[9]],ignore_index=True)
    q_data = pd.concat([data[1],data[10]],ignore_index=True)
    q_d = q_data.drop('Unnamed: 0', axis='columns').add_prefix('Q_')
    y_d = y_data.drop('Unnamed: 0', axis='columns').add_prefix('Y_')
    con = pd.concat([q_data, y_data], ignore_index=True)
    du = pd.concat([q_d, y_d], ignore_index=True)
    du['Info'] = con['Unnamed: 0']
    su = pd.melt(du, id_vars=['Info'], var_name='Qtr_or_Yly', value_name=name, ignore_index=True)
    mon = {'Month': ['Q_Jan ', 'Q_Feb ', 'Q_Mar ', 'Q_Apr ', 'Q_May ', 'Q_Jun ', 'Q_Jul ', 'Q_Aug ', 'Q_Sep ', 'Q_Oct ',
                     'Q_Nov ', 'Q_Dec ', 'Y_Jan ', 'Y_Feb ', 'Y_Mar ', 'Y_Apr ', 'Y_May ', 'Y_Jun ', 'Y_Jul ', 'Y_Aug ',
                     'Y_Sep ', 'Y_Oct ', 'Y_Nov ', 'Y_Dec ', 'Q_TTM', 'Y_TTM'],
           'qtr': ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3', 'Q4', 'Q4', 'Q4', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y',
                   'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Q_TTM', 'Y_TTM']}
    mon = pd.DataFrame(mon)
    su['Month'] = su.Qtr_or_Yly.str[:6]
    su['Year'] = su.Qtr_or_Yly.str[-4:]
    su = pd.merge(su, mon, on='Month', how='left')
    su['QY'] = su.qtr + su.Year
    su['label'] = su.Info + "_" + su.QY
    su.index = su.label
    su = su.drop(['Info', 'Qtr_or_Yly', 'Month', 'Year', 'qtr', 'QY', 'label'], axis=1)
    sun = su.dropna()
    return sun
#print(fundamental('APOLLOHOSP'))
#saj = input("Enter ticker name:")
#print(fundamental(saj))