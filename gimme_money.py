from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from random_word import RandomWords
import time
import configparser
def set_up_driver():
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(options=options)
    return driver
r = RandomWords()
def get_creds():
    config = configparser.ConfigParser()
    config.read('creds.ini')
    return {"login":config["login_creds"]["login"],"password":config["login_creds"]["password"]}
def main(url):
    driver = set_up_driver()
    driver.get("https://bing.com")
    time.sleep(2)
    driver.find_element_by_id("id_l").click()
    time.sleep(3)
    driver.find_element_by_id("idA_PWD_SwitchToCredPicker").click()
    try:
        time.sleep(1)
        for item in driver.find_elements_by_class_name("table-cell"):
            print(item.text)
            time.sleep(1)
            if "GitHub" in item.text:
                item.click()
                time.sleep(2)
                creds = get_creds()
                driver.find_element_by_id("login_field").send_keys(creds["login"])
                driver.find_element_by_id("password").send_keys(creds["password"])
                driver.find_elements_by_class_name("btn")[0].click()
    except:
        pass
    time.sleep(5)
    for _ in range(10):
        random_words = r.get_random_words()
        for x in random_words:
            driver.get(f"https://www.bing.com/search?q={x}")
            time.sleep(1)

if __name__ == "__main__":
	main("link")