from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/nn-admin/Desktop/Python Course/chromedriver"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.driver.get("https://www.speedtest.net/")
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        time.sleep(5)
        go_btn = self.driver.find_element_by_class_name("js-start-test.test-mode-multi")
        go_btn.click()
        time.sleep(60)
        self.down = float(self.driver.find_element_by_class_name("result-data-large.number.result-data-value."
                                                           "download-speed").text)
        self.up = float(self.driver.find_element_by_class_name("result-data-large.number.result-data-value."
                                                         "upload-speed").text)

    def tweet_at_provider(self, email, password):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        username_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/'
                                          'div[1]/label/div/div[2]/div/input')
        password_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/'
                                                     'form/div/div[2]/label/div/div[2]/div/input')
        username_field.send_keys(email)
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet = self.driver.find_element_by_class_name("public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
        tweet.send_keys(f"Hey ISP, why is my internet speed {self.down}down/{self.up}up when I pay for 150down/10up?")
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]'
                                          '/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/'
                                          'div/span/span').click()


complaint_bot = InternetSpeedTwitterBot()
complaint_bot.get_internet_speed()
complaint_bot.tweet_at_provider('my_email', 'my_password')