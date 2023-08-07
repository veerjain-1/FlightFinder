

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

from dotenv import load_dotenv

load_dotenv()



####################### SELENIUM SETTINGS #########################
chrome_driver_path = "chromedriver.exe"

# creating the webdriver
service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()


driver = webdriver.Chrome(service=service, options=options)
WEBSITE_URL_FOR_THE_DRIVER = "https://www.southwest.com/"
time.sleep(2)
# load the page at the given URL
driver.get(WEBSITE_URL_FOR_THE_DRIVER)
#######################################################################

# wait for the page to load
time.sleep(2)


# Find the radio button element for "One-way" and click it
one_way_radio_button = driver.find_element(By.XPATH, "//input[@value='oneway']")
one_way_radio_button.click()
time.sleep(1)




try:
    airportCode = driver.find_element(By.ID, 'LandingAirBookingSearchForm_originationAirportCode')
    airportCode.clear()
    ActionChains(driver).send_keys_to_element(airportCode, 'SFO').perform()
    time.sleep(1)
    airportCode.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")

try:
    airportCode1 = driver.find_element(By.ID, 'LandingAirBookingSearchForm_destinationAirportCode')
    airportCode1.clear()
    airportCode1.send_keys('MDW')
    airportCode1.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")

print('Provide the date you want your flight on: EXAMPLE DATE FORMAT: 7/27')
flight_date = input('---')

print(f'Finding flights for {flight_date}... SFO --> MDW')


try:
    flightDate = driver.find_element(By.ID, 'LandingAirBookingSearchForm_departureDate')
    flightDate.clear()
    ActionChains(driver).send_keys_to_element(flightDate, flight_date).perform()
    flightDate.send_keys(Keys.TAB)
except NoSuchElementException:
    print("Element not found")



time.sleep(5)

search_button_element = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element.click()
time.sleep(2.5)
search_button_element1 = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element1.click()

time.sleep(5)

sort_by_element = driver.find_element(By.XPATH, "//input[@aria-label ='Sort results by']")
sort_by_element.send_keys("P")
sort_by_element.send_keys(Keys.ENTER)

lowest_fare_element = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Wanna Get Away fare')]")

s = lowest_fare_element.get_attribute("aria-label")
s1=("The cheapest flight from SFO --> MDW is $"+s[21:24])


print("done")

driver.switch_to.new_window()

######################################################################################################################

time.sleep(2)
# load the page at the given URL
driver.get(WEBSITE_URL_FOR_THE_DRIVER)
#######################################################################

# wait for the page to load
time.sleep(2)


# Find the radio button element for "One-way" and click it
one_way_radio_button = driver.find_element(By.XPATH, "//input[@value='oneway']")
one_way_radio_button.click()
time.sleep(1)




try:
    airportCode = driver.find_element(By.ID, 'LandingAirBookingSearchForm_originationAirportCode')
    airportCode.clear()
    ActionChains(driver).send_keys_to_element(airportCode, 'SJC').perform()
    time.sleep(1)
    airportCode.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")

try:
    airportCode1 = driver.find_element(By.ID, 'LandingAirBookingSearchForm_destinationAirportCode')
    airportCode1.clear()
    airportCode1.send_keys('MDW')
    airportCode1.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")



print(f'Finding flights for {flight_date}... SJC --> MDW')


try:
    flightDate = driver.find_element(By.ID, 'LandingAirBookingSearchForm_departureDate')
    flightDate.clear()
    ActionChains(driver).send_keys_to_element(flightDate, flight_date).perform()
    flightDate.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")



time.sleep(5)

search_button_element = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element.click()
time.sleep(5)
search_button_element1 = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element1.click()

time.sleep(5)
sort_by_element = driver.find_element(By.XPATH, "//input[@aria-label='Sort results by']")

sort_by_element.send_keys("P")
sort_by_element.send_keys(Keys.ENTER)

lowest_fare_element = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Wanna Get Away fare')]")

s = lowest_fare_element.get_attribute("aria-label")
s2=("The cheapest flight from SJC --> MDW is $"+s[21:24])



print("done")

driver.switch_to.new_window()

######################################################################################################################

time.sleep(2)
# load the page at the given URL
driver.get(WEBSITE_URL_FOR_THE_DRIVER)
#######################################################################

# wait for the page to load
time.sleep(2)


# Find the radio button element for "One-way" and click it
one_way_radio_button = driver.find_element(By.XPATH, "//input[@value='oneway']")
one_way_radio_button.click()
time.sleep(1)




try:
    airportCode = driver.find_element(By.ID, 'LandingAirBookingSearchForm_originationAirportCode')
    airportCode.clear()
    ActionChains(driver).send_keys_to_element(airportCode, 'OAK').perform()
    time.sleep(1)
    airportCode.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")

try:
    airportCode1 = driver.find_element(By.ID, 'LandingAirBookingSearchForm_destinationAirportCode')
    airportCode1.clear()
    airportCode1.send_keys('MDW')
    airportCode1.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")



print(f'Finding flights for {flight_date}... OAK --> MDW')


try:
    flightDate = driver.find_element(By.ID, 'LandingAirBookingSearchForm_departureDate')
    flightDate.clear()
    ActionChains(driver).send_keys_to_element(flightDate, flight_date).perform()
    flightDate.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")


time.sleep(1)

search_button_element = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element.click()
time.sleep(5)
search_button_element1 = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element1.click()


time.sleep(5)

sort_by_element = driver.find_element(By.XPATH, "//input[@aria-label ='Sort results by']")
sort_by_element.send_keys("P")
sort_by_element.send_keys(Keys.ENTER)

lowest_fare_element = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Wanna Get Away fare')]")

s = lowest_fare_element.get_attribute("aria-label")
s3=("The cheapest flight from OAK --> MDW is $"+s[21:24])



print("done")

driver.switch_to.new_window()

###########################################################################################################################################
############################################################################################################################3
###########################################################################################################################

time.sleep(2)
# load the page at the given URL
driver.get(WEBSITE_URL_FOR_THE_DRIVER)
#######################################################################

# wait for the page to load
time.sleep(2)


# Find the radio button element for "One-way" and click it
one_way_radio_button = driver.find_element(By.XPATH, "//input[@value='oneway']")
one_way_radio_button.click()
time.sleep(1)




try:
    airportCode = driver.find_element(By.ID, 'LandingAirBookingSearchForm_originationAirportCode')
    airportCode.clear()
    ActionChains(driver).send_keys_to_element(airportCode, 'SFO').perform()
    time.sleep(1)
    airportCode.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")

try:
    airportCode1 = driver.find_element(By.ID, 'LandingAirBookingSearchForm_destinationAirportCode')
    airportCode1.clear()
    airportCode1.send_keys('ORD')
    airportCode1.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")



print(f'Finding flights for {flight_date}... SFO --> ORD')


try:
    flightDate = driver.find_element(By.ID, 'LandingAirBookingSearchForm_departureDate')
    flightDate.clear()
    ActionChains(driver).send_keys_to_element(flightDate, flight_date).perform()
    flightDate.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")



time.sleep(1)

search_button_element = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element.click()
time.sleep(5)
search_button_element1 = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element1.click()

time.sleep(5)

sort_by_element = driver.find_element(By.XPATH, "//input[@aria-label ='Sort results by']")
sort_by_element.send_keys("P")
sort_by_element.send_keys(Keys.ENTER)

lowest_fare_element = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Wanna Get Away fare')]")

s = lowest_fare_element.get_attribute("aria-label")
s4=("The cheapest flight from SFO --> ORD is $"+s[21:24])


print("done")

driver.switch_to.new_window()

######################################################################################################################

time.sleep(2)
# load the page at the given URL
driver.get(WEBSITE_URL_FOR_THE_DRIVER)
#######################################################################

# wait for the page to load
time.sleep(2)


# Find the radio button element for "One-way" and click it
one_way_radio_button = driver.find_element(By.XPATH, "//input[@value='oneway']")
one_way_radio_button.click()
time.sleep(1)




try:
    airportCode = driver.find_element(By.ID, 'LandingAirBookingSearchForm_originationAirportCode')
    airportCode.clear()
    ActionChains(driver).send_keys_to_element(airportCode, 'SJC').perform()
    time.sleep(1)
    airportCode.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")

try:
    airportCode1 = driver.find_element(By.ID, 'LandingAirBookingSearchForm_destinationAirportCode')
    airportCode1.clear()
    airportCode1.send_keys('ORD')
    airportCode1.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")



print(f'Finding flights for {flight_date}... SJC --> ORD')


try:
    flightDate = driver.find_element(By.ID, 'LandingAirBookingSearchForm_departureDate')
    flightDate.clear()
    ActionChains(driver).send_keys_to_element(flightDate, flight_date).perform()
    flightDate.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")


time.sleep(1)

search_button_element = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element.click()
search_button_element1 = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element1.click()

time.sleep(5)

sort_by_element = driver.find_element(By.XPATH, "//input[@aria-label ='Sort results by']")
sort_by_element.send_keys("P")
sort_by_element.send_keys(Keys.ENTER)

lowest_fare_element = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Wanna Get Away fare')]")

s = lowest_fare_element.get_attribute("aria-label")
s5=("The cheapest flight from SJC --> ORD is $"+s[21:24])



print("done")

driver.switch_to.new_window()

######################################################################################################################

time.sleep(2)
# load the page at the given URL
driver.get(WEBSITE_URL_FOR_THE_DRIVER)
#######################################################################

# wait for the page to load
time.sleep(2)


# Find the radio button element for "One-way" and click it
one_way_radio_button = driver.find_element(By.XPATH, "//input[@value='oneway']")
one_way_radio_button.click()
time.sleep(1)




try:
    airportCode = driver.find_element(By.ID, 'LandingAirBookingSearchForm_originationAirportCode')
    airportCode.clear()
    ActionChains(driver).send_keys_to_element(airportCode, 'OAK').perform()
    time.sleep(1)
    airportCode.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")

try:
    airportCode1 = driver.find_element(By.ID, 'LandingAirBookingSearchForm_destinationAirportCode')
    airportCode1.clear()
    airportCode1.send_keys('ORD')
    airportCode1.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")



print(f'Finding flights for {flight_date}... OAK --> ORD')


try:
    flightDate = driver.find_element(By.ID, 'LandingAirBookingSearchForm_departureDate')
    flightDate.clear()
    ActionChains(driver).send_keys_to_element(flightDate, flight_date).perform()
    flightDate.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")


time.sleep(1)

search_button_element = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element.click()
search_button_element1 = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element1.click()

time.sleep(5)

sort_by_element = driver.find_element(By.XPATH, "//input[@aria-label ='Sort results by']")
sort_by_element.send_keys("P")
sort_by_element.send_keys(Keys.ENTER)

lowest_fare_element = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Wanna Get Away fare')]")

s = lowest_fare_element.get_attribute("aria-label")
s6=("The cheapest flight from OAK --> ORD is $"+s[21:24])



print("done")


#################################################################################################################
###############################################################################################################
###############################################################################################################

driver.switch_to.new_window()

time.sleep(2)
# load the page at the given URL
driver.get(WEBSITE_URL_FOR_THE_DRIVER)
#######################################################################

# wait for the page to load
time.sleep(2)


# Find the radio button element for "One-way" and click it
one_way_radio_button = driver.find_element(By.XPATH, "//input[@value='oneway']")
one_way_radio_button.click()
time.sleep(1)




try:
    airportCode = driver.find_element(By.ID, 'LandingAirBookingSearchForm_originationAirportCode')
    airportCode.clear()
    ActionChains(driver).send_keys_to_element(airportCode, 'SFO').perform()
    time.sleep(1)
    airportCode.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")

try:
    airportCode1 = driver.find_element(By.ID, 'LandingAirBookingSearchForm_destinationAirportCode')
    airportCode1.clear()
    airportCode1.send_keys('IND')
    airportCode1.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")



print(f'Finding flights for {flight_date}... SFO --> IND')


try:
    flightDate = driver.find_element(By.ID, 'LandingAirBookingSearchForm_departureDate')
    flightDate.clear()
    ActionChains(driver).send_keys_to_element(flightDate, flight_date).perform()
    flightDate.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")


time.sleep(1)

search_button_element = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element.click()
search_button_element1 = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element1.click()


time.sleep(5)

sort_by_element = driver.find_element(By.XPATH, "//input[@aria-label ='Sort results by']")
sort_by_element.send_keys("P")
sort_by_element.send_keys(Keys.ENTER)

lowest_fare_element = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Wanna Get Away fare')]")

s = lowest_fare_element.get_attribute("aria-label")
s7=("The cheapest flight from SFO --> IND is $"+s[21:24])


print("done")

driver.switch_to.new_window()

######################################################################################################################

time.sleep(2)
# load the page at the given URL
driver.get(WEBSITE_URL_FOR_THE_DRIVER)
#######################################################################

# wait for the page to load
time.sleep(2)


# Find the radio button element for "One-way" and click it
one_way_radio_button = driver.find_element(By.XPATH, "//input[@value='oneway']")
one_way_radio_button.click()
time.sleep(1)




try:
    airportCode = driver.find_element(By.ID, 'LandingAirBookingSearchForm_originationAirportCode')
    airportCode.clear()
    ActionChains(driver).send_keys_to_element(airportCode, 'SJC').perform()
    time.sleep(1)
    airportCode.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")

try:
    airportCode1 = driver.find_element(By.ID, 'LandingAirBookingSearchForm_destinationAirportCode')
    airportCode1.clear()
    airportCode1.send_keys('IND')
    airportCode1.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")



print(f'Finding flights for {flight_date}... SJC --> IND')


try:
    flightDate = driver.find_element(By.ID, 'LandingAirBookingSearchForm_departureDate')
    flightDate.clear()
    ActionChains(driver).send_keys_to_element(flightDate, flight_date).perform()
    flightDate.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")


time.sleep(1)

search_button_element = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element.click()
search_button_element1 = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element1.click()

time.sleep(5)

sort_by_element = driver.find_element(By.XPATH, "//input[@aria-label ='Sort results by']")
sort_by_element.send_keys("P")
sort_by_element.send_keys(Keys.ENTER)

lowest_fare_element = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Wanna Get Away fare')]")

s = lowest_fare_element.get_attribute("aria-label")
s8=("The cheapest flight from SJC --> IND is $"+s[21:24])


print("done")

driver.switch_to.new_window()

######################################################################################################################

time.sleep(2)
# load the page at the given URL
driver.get(WEBSITE_URL_FOR_THE_DRIVER)
#######################################################################

# wait for the page to load
time.sleep(2)


# Find the radio button element for "One-way" and click it
one_way_radio_button = driver.find_element(By.XPATH, "//input[@value='oneway']")
one_way_radio_button.click()
time.sleep(1)




try:
    airportCode = driver.find_element(By.ID, 'LandingAirBookingSearchForm_originationAirportCode')
    airportCode.clear()
    ActionChains(driver).send_keys_to_element(airportCode, 'OAK').perform()
    time.sleep(1)
    airportCode.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")

try:
    airportCode1 = driver.find_element(By.ID, 'LandingAirBookingSearchForm_destinationAirportCode')
    airportCode1.clear()
    airportCode1.send_keys('IND')
    airportCode1.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")



print(f'Finding flights for {flight_date}... OAK --> IND')


try:
    flightDate = driver.find_element(By.ID, 'LandingAirBookingSearchForm_departureDate')
    flightDate.clear()
    ActionChains(driver).send_keys_to_element(flightDate, flight_date).perform()
    flightDate.send_keys(Keys.ENTER)
except NoSuchElementException:
    print("Element not found")


time.sleep(1)

search_button_element = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element.click()
search_button_element1 = driver.find_element(By.XPATH, "//button[@aria-label='Search button. In the event of an error, focus will move to the error message.']")
search_button_element1.click()


time.sleep(5)

sort_by_element = driver.find_element(By.XPATH, "//input[@aria-label ='Sort results by']")
sort_by_element.send_keys("P")
sort_by_element.send_keys(Keys.ENTER)

lowest_fare_element = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Wanna Get Away fare')]")

s = lowest_fare_element.get_attribute("aria-label")
s9 = ("The cheapest flight from OAK --> IND is $"+s[21:24])


print("done")


flight_data = [s1, s2, s3, s4, s5, s6, s7, s8, s9]


def get_price(flight_string):
    return int(flight_string.split()[-1].replace('$', ''))


sorted_flight_data = sorted(flight_data, key=get_price)

print(*sorted_flight_data, sep='\n')


input("Press Enter to exit")