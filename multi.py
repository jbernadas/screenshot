import sys
import os
from selenium import webdriver
import unittest
import util
import sitemap_gen

target_url = raw_input('What is the target URL? ')
exclude1 = 'png'
exclude2 = 'jpg'
exclude3 = 'pdf'

# # fire up the sitemap generator with the following parameter/options
# # -b stands for block extensions, to be excluded from crawl, i.e., pdf, doc, excel, etc.
# # please refer to http://toncar.cz/opensource/sitemap_gen.html for additional info on how to use sitemap_gen.py
os.system('python sitemap_gen.py -b %s -b %s -b %s %s' %(exclude1, exclude2, exclude3, target_url))

class Test(unittest.TestCase):
    """ Demonstration: Get Chrome to generate fullscreen screenshot """

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_fullpage_screenshot(self):
        ''' Generate document-height screenshot '''
        
        i = 1
        with open("sitemap.txt") as urls:
            for line in urls:
                self.driver.get(line)
                self.driver.set_window_size(1440, 2000)
                util.fullpage_screenshot(self.driver, "page" + str(i) + ".png")  
                i = i + 1
        urls.close()

if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]])
    