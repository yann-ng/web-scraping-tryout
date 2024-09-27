from selenium import webdriver
from selenium.webdriver.common.by import By

from configparser import ConfigParser
import os

here = os.path.abspath(os.path.dirname(__file__))
config_file_name = "user.ini"
config_file_path = os.path.join(here, config_file_name)

config = ConfigParser()
config.read(config_file_path)

fb_email = config.get('user', 'fb_email')
fb_pass = config.get('user', 'fb_pass')


BASE_URL = "https://www.facebook.com/"

def main():
    options_firefox = webdriver.FirefoxOptions()

    driver = webdriver.Firefox(options=options_firefox)
    driver.get(BASE_URL)

    form_email = driver.find_element(By.ID, "email")
    form_email.send_keys(fb_email)
    form_pass = driver.find_element(By.ID, "pass")
    form_pass.send_keys(fb_pass)
    form_submit = driver.find_element(By.NAME, "login")
    form_submit.click()

    try:
        driver.get_screenshot_as_file("screenshot.png")
        print("Screenshot saved!")
    except Exception as e:
        print("Failed to save screenshot!")
        print(e)

    driver.close()

if __name__ == '__main__':
    print("Initialized...")
    main()