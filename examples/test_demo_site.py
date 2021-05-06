from seleniumbase import BaseCase


class DemoSiteTests(BaseCase):
    def test_demo_site(self):
        self.open("https://controlc.com/66eee4cd")
