from selenium.webdriver.support.select import Select
def selection(values,element):
    for val in values:
        if val.text == element:
            val.click()
            break

def selectelem(elm,text):
    select=Select(elm)
    select.select_by_visible_text(text)

def windowSwitch(driver):
    p = driver.current_window_handle
    parent = driver.window_handles[0]
    chld = driver.window_handles[1]
    driver.switch_to.window(chld)