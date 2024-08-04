from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
import time

def login(driver):
    user_element = driver.find_element_by_id("login-email")
    user_element.send_keys("username")

    pass_element = driver.find_element_by_id("login-password")
    pass_element.send_keys("password")

    submit_element = driver.find_element_by_id("login-submit")
    submit_element.click()
    time.sleep(2)

def goto_network(driver):
    network_element = driver.find_element_by_id("mynetwork-tab-icon")
    network_element.click()
    time.sleep(2)

def send_requests():
    try:
        request_count = int(input("Enter the number of requests to send: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for _ in range(request_count):
        pag.click(880, 770)
        time.sleep(1)

    print("Request sending process completed!")

def main():
    linkedin_url = "http://linkedin.com/"
    network_page_url = "http://linkedin.com/mynetwork/"
    chrome_driver_path = 'C:\\Program Files\\Web Driver\\chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver_path)

    driver.get(linkedin_url)
    login(driver)
    goto_network(driver)

    send_requests()

    driver.quit()

if __name__ == "__main__":
    main()
