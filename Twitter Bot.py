from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
EMAIL= "ObadaQaf"
PASS="obadaqafesha12431243"

#USER_EMAIL =input("enter your username or email ... ")
#USER_PASS = input("enter our password pleas ... ")


#webdriver
chrom_path = "C:\development\chromedriver_win32"

driver = webdriver.Chrome(executable_path=chrom_path)
driver.get("https://www.speedtest.net/")
go = driver.find_element(By.CSS_SELECTOR,".start-text")
go.click()
#time.sleep(5)
downlade = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
up_lade= driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
time.sleep(40)
message = f"my internet downlad speed is {downlade.text} and my uplade speed is {up_lade.text} , thank you "
print(downlade.text)
print(up_lade.text)
driver.close()
driver2 = webdriver.Chrome(executable_path=chrom_path)
driver2.get("https://www.twitter.com")
lodin=driver2.find_element(By.LINK_TEXT, "Log in")
lodin.click()
time.sleep(10)
email_box=driver2.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
email_box.send_keys(EMAIL)
email_box.send_keys(Keys.ENTER)
time.sleep(5)
pass_box= driver2.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
pass_box.send_keys(PASS)
pass_box.send_keys(Keys.ENTER)
time.sleep(10)
text_box =driver2.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
text_box.send_keys(message)
time.sleep(10)
