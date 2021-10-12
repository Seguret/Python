from selenium import webdriver

driver = webdriver.Firefox()

def get_url():
    print('# ESEGUO GET_URL')
    url = 'file:///C:/Users/Mirko/OneDrive/Desktop/Project/murota/unimercatorum.html'
    driver.get(url)

def tele_screen(): # SCREENSHOT CAPTCHA 

    screenshot = "screenshot.png"
    
    element = driver.find_element_by_xpath("//h3[@class='text-center']")
    print(element)
    element.screenshot(screenshot)

    return screenshot

get_url()
tele_screen()
