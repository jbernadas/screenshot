"""
This script uses a version of the one here:
https://snipt.net/restrada/python-selenium-workaround-for-full-page-screenshot-using-chromedriver-2x/

It contains the *crucial* correction added in the comments by Jason Coutu.
"""

import sys

from selenium import webdriver
import unittest

import util

class Test(unittest.TestCase):
    """ Demonstration: Get Chrome to generate fullscreen screenshot """

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_fullpage_screenshot(self):
        ''' Generate document-height screenshot '''
        url = "https://texasgrips.com"
        self.driver.get(url)
        self.driver.set_window_size(1440, 2000)
        util.fullpage_screenshot(self.driver, "test.png")

if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
