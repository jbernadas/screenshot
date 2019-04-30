******
README
******

Note: This works on Linux operating systems. Windows and Mac OS not fully tested.

This is a Python 2 full-page-website screenshot generator. It generates screenshots by first crawling the target website to get all available URLs and writes all found pages to sitemap.txt. It then reads the list of URLs in sitemap.txt file and goes through the list one by one to create a full-page PNG screenshot of the web page. It has the following libraries as dependencies: Util, PIL, Selenium, ChromeDriver.

To download Util, PIL and Selenium, you can use pip. 
::
  
  pip install python-utility
  pip install Pillow
  pip install selenium

ChromeDriver needs to be downloaded from: https://sites.google.com/a/chromium.org/chromedriver/downloads. Choose the appropriate Chrome version, save it to your computer, cd into the directory where you downloaded Chromedriver. Unzip the file:
::

  unzip chromedriver_linux64.zip

Execute command:
::

  pip install chromedriver
