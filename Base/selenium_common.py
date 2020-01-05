from selenium import webdriver


class seleniumCommon:
    #driver=webdriver.Chrome(executable_path=r"‪C:\Users\ravin\PycharmProjects\phptravels\drivers\chromedriver.exe")
    driver=webdriver.Chrome(executable_path=r"C:\Users\ravin\PycharmProjects\python_selenium\webdrivers\chromedriver_win32\chromedriver.exe")



    #locators

    def getTitle(self):
        print(self.driver.title)