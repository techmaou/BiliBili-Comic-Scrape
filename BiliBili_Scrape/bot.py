import json
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from seleniumwire import webdriver
from seleniumwire.utils import decode


class Bot():

    def collectURLs(self, elems):

        chapURLs = []

        for elem in elems:
            chapURLs.append(elem.get_attribute('href'))

        return chapURLs

    def scroll(self):

        self.elements = self.browser.find_elements(By.TAG_NAME, self.tag)

        for elem in self.elements:
            self.actions.move_to_element(elem).perform()
            time.sleep(1)

    def chapImgURLs(self):

        counter = 1
        temp = None
        reqs = self.browser.requests
        seq = dict()

        for req in reqs:
            if self.key in req.url:
                body = decode(req.response.body, req.response.headers.get(
                    'Content-Encoding', 'identity'))
                body = body.decode()
                temp = json.loads(body)['data'][0]
                seq[counter] = temp['url'] + '?token=' + temp['token']
                counter += 1

        return seq

    def __init__(self, url=None, tag=None, key=None):

        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")

        self.browser = webdriver.Chrome(options=chrome_options)
        self.actions = ActionChains(self.browser)
        wait = WebDriverWait(self.browser, 10)

        self.tag = tag
        self.key = key

        self.browser.get(url)
        wait.until(EC.presence_of_element_located(By.CLASS_NAME, 'list-data'))

        '''if key:
            self.browser.get(url)
            wait.until(EC.presence_of_element_located((By.TAG_NAME, self.tag)))
            self.scroll()
            print('scrolld')
            time.sleep(5)

        else:
            raise ValueError('The URL field is not provided.')
'''
