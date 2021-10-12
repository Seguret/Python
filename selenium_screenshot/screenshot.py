from selenium import webdriver

driver = webdriver.Firefox(executable_path='E:\Python\selenium_screenshot\geckodriver.exe')

def get_url():
    print('# ESEGUO GET_URL')
    url = ''
    driver.get(url)

def tele_screen(): # SCREENSHOT CAPTCHA 

    screenshot = "screenshot.png"
    
    element = driver.find_element_by_xpath("//h3[@class='text-center']")
    print(element)
    element.screenshot(screenshot)

    return screenshot

get_url()
tele_screen()
