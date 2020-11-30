
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import re

chromedriver = 'C:/Users/webdriver/chromedriver'
options = Options()
options.add_argument('--window-size=1200,1000')
'''options.add_argument('headless')  # для открытия headless-браузера'''
browser = webdriver.Chrome('C:/Users/webdriver/chromedriver.exe', chrome_options=options)


def main():
	browser.get('https://csgorun.pro/')
	elem = [browser.find_element_by_class_name('graph-labels').text]
	l = [float(x.replace('x', '').replace('\n', '')) for x in elem]
	
	print(l)
	


if __name__ == '__main__':
	main()

browser.close()