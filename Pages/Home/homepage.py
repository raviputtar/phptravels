from Base.selenium_common import seleniumCommon

class homepage(seleniumCommon):

    def launchHome(self):
        self.driver.get("https://www.phptravels.net/index.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def titlePage(self):
        self.getTitle()