import time
from seleniumbase import BaseCase


class MyTestClass(BaseCase):
    def test_basics(self):
        self.open("https://test.muttil.workers.dev/0:/")
        print("Sleeping for 100 secs")
        time.sleep(100)
        print("Done")
