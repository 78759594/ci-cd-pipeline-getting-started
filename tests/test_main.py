#from src.main import add, subtract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import time
from selenium.webdriver.edge.service import Service
from webdriver.microsoft import EdgeChromiumDriverManager

#driver=webdriver.Edge("C:\Driver\edgedriver_win64\msedgedriver.exe")
driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.get("https://www.tutorialspoint.com/selenium/practice/login.php")

username=driver.find_element(By.XPATH,"//*[@id='email']").send_keys("snavale1")
passwod=driver.find_element(By.XPATH,"//*[@id='password']").send_keys("Telematics#1902")

button=driver.find_element(By.CLASS_NAME,"btn btn-primary").click()


#driver.close()
# def test_add_function():
#     assert add(2, 3) == 5
#     assert add(0, 0) == 0
#     assert add(5, 5) == 10
#
# def test_subtract_function():
#     assert subtract(5, 3) == 2
#     assert subtract(0, 0) == 0
#     assert subtract(15, 5) == 10