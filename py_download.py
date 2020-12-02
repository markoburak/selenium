from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time


# function to enable safe downloading and starting driver
def get_driver(path):
    options = Options()
    options.add_experimental_option("prefs", {
        "safebrowsing.enabled": True
    })

    chrome_driver = webdriver.Chrome(executable_path=path, options=options)
    return chrome_driver


# url and path to driver
url = 'https://www.python.org/'

# check if webdriver is compatible with your chrome version
try:
    chrome_path = r'.\chromedriver.exe'
    driver = get_driver(chrome_path)
except:
    chrome_path = r'.\chromedriver86.exe'
    driver = get_driver(chrome_path)
driver.switch_to.window(driver.window_handles[0])

# open fullscreen and enter website
driver.maximize_window()
driver.get(url)

# sleep to load fullscreen
time.sleep(2)

# hover over downloads
element_to_hover_over = driver.find_element_by_id("downloads")
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()
time.sleep(1)

# find path of download button with full xpath and click element
download = driver.find_element_by_xpath("/html/body/div/header/div/nav/ul/li[2]/ul/li[8]/div[3]/p[1]/a")
download.click()
