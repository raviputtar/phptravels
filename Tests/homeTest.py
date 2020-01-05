from Pages.Home.homepage import homepage
import unittest

class homeTest(unittest.TestCase):

    def setUp(self):
        self.hp=homepage()

    def test_first(self):
        self.hp.launchHome()
        self.hp.getTitle()

    def tearDown(self) -> None:
        self.hp.driver.quit()
