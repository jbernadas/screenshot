*****************************
Web Page Screenshot Generator
*****************************

**NOTE: THIS PROJECT HAS REACHED END-OF-LIFE, AND IS JUST PRESERVED HERE FOR POSTERITY. THE LATEST PYTHON 3 VERSION OF THIS PROJECT IS AT https://github.com/jbernadas/screenshot_py3**

This is a Python 2 full-page-website screenshot generator that is built on top of the web crawler created by Vladimir Toncar and Pavel Dvorak. It generates screenshots by first crawling the target website to get all available URLs and writes all found pages to sitemap.txt. It then reads the list of URLs in sitemap.txt file and goes through the list one by one to create a full-page PNG screenshot of the web page. It has the following libraries as dependencies: Util, PIL, Selenium, ChromeDriver.

To download Util, PIL and Selenium, you can use pip. 
::
  
  pip install python-utility
  pip install Pillow
  pip install selenium

ChromeDriver is downloaded from: https://sites.google.com/a/chromium.org/chromedriver/downloads. Choose the appropriate Chrome version, save it to your computer, cd into the directory where you downloaded Chromedriver. Unzip the file:
::

  unzip chromedriver_linux64.zip

Make chromedriver executable then move it to a directory that is part of your path:
::
  
  chmod +x chromedriver
  sudo mv chromedriver /usr/local/bin/chromedriver

Now cd into screenshot directory. Fire up the multi.py file:
::

  python multi.py

It will ask you for the target URL. Be careful to check if the target URL has a lot of pages, the script will screenshot most of it (except those that end with PNG, JPG and PDF). The maximum is set at 4999 pages, which might be too much. You might want to change this in sitemap_gen.py.

Thanks for looking.
