import json
import datetime
import selenium
from selenium import webdriver
from pyvirtualdisplay import Display


FH = open("/apps/tibco/GMaps/result.csv","a+")
timen = datetime.datetime.now()

routes = ['https://www.google.com/maps/dir/?api=1&origin=Rathtala+Kamarhati&destination=Bhardhman&travelmode=driving','https://www.google.com/maps/dir/?api=1&origin=Bardhaman,+West+Bengal&destination=Morgram,+West+Bengal&travelmode=driving','https://www.google.com/maps/dir/?api=1&origin=Morgram,+West+Bengal&destination=Dhantola,+West+Bengal&travelmode=driving','https://www.google.com/maps/dir/?api=1&origin=Dhantola,+West+Bengal&destination=Malbazar,+West+Bengal&travelmode=driving','https://www.google.com/maps/dir/?api=1&origin=Malbazar,+West+Bengal&destination=Murti+WBFDC+Banani+Resort,+Murti,+West+Bengal&travelmode=driving']

display = Display(visible=0, size=(800, 800))
display.start()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('/apps/tibco/Report/lib/chromedriver', chrome_options=chrome_options)
for url in routes:
	driver.get(url)
	result1 = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[7]/div[9]/div/div/div/div/div[5]/div/div/div/div/div/span")
	FH.write(str(timen)+","+url+","+result1.get_attribute("innerHTML")+"\n")
driver.close()
driver.quit()

FH.close()

