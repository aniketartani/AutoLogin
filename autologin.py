from selenium import webdriver
chromedriver="chromedriver.exe"

while True:
        driver=webdriver.Chrome(chromedriver)
        driver.get("https://moodle.vitbhopal.ac.in/login/index.php")
        driver.find_element_by_id("username").send_keys("****username***")
        driver.find_element_by_id("password").send_keys("****password***")
        driver.find_element_by_id("loginbtn").click()
#by ANIKET ARTANI
