from selenium import webdriver
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(service=Service(r"E:\vscode project\driver\msedgedriver.exe"))
driver.get("https://www.baidu.com")
print(driver.title)
driver.quit()

