# -*- coding: utf-8 -*-
from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase


class HomeNewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_it_worked_site_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)

    def test_it_worked_site_body_text(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('It worked!', self.browser.find_element_by_id("summary").text)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
