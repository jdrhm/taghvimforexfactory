import random
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def create_driver():
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:90.0) Gecko/20100101 Firefox/90.0',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    ]
    user_agent = random.choice(user_agent_list)

    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument("--no-sandbox")
    browser_options.add_argument("--headless")
    browser_options.add_argument("start-maximized")
    browser_options.add_argument("window-size=1900,1080")
    browser_options.add_argument("disable-gpu")
    browser_options.add_argument("--disable-software-rasterizer")
    browser_options.add_argument("--disable-dev-shm-usage")
    browser_options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(options=browser_options, service_args=["--verbose", "--log-path=test.log"])

    return driver

def parse_data(driver, url):
    driver.get(url)

    data_table = driver.find_element(By.CLASS_NAME, "calendar__table")
    value_list = []

    for row in data_table.find_elements(By.TAG_NAME, "tr"):
        row_data = list(filter(None, [td.text for td in row.find_elements(By.TAG_NAME, "td")]))
        if row_data:
            value_list.append(row_data)
    return value_list

driver = create_driver()
url = 'https://www.forexfactory.com/calendar'

value_list = parse_data(driver=driver, url=url)


    
with open('./Data.json' , "r") as readingJsonData:
    jsonData = json.load(readingJsonData)
    jsonData.append(value_list)
with open("./Data.json" , "w") as writingJsonData:
    json.dump(jsonData , writingJsonData , indent = 4)    
