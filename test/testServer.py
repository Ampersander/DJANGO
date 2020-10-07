from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ServerTest(TestCase):

    '''Test du serveur allumé et lesTaches dans le titre'''
    def test_server_on(self):

        browser = webdriver.Chrome()
        browser.get('http://localhost:8000/')
        time.sleep(1)
        assert 'lesTaches' in browser.title
        time.sleep(1)
        browser.quit()
