README
======

This is a Python 2 full-page-website screenshot generator. It generates screenshots by first crawling the target website to get all available URLs and writes all found pages to sitemap.txt. It then reads the list of URLs in sitemap.txt file and goes through the list one by one to create a full-page PNG screenshot of the web page. It has the following libraries as dependencies: Util, PIL, Selenium, ChromeDriver.

To download Util PIL and Selenium, you can use pip. ChromeDriver needs to be installed from: https://sites.google.com/a/chromium.org/chromedriver/downloads