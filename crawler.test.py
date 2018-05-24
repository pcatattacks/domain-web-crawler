import unittest
from crawler import *

class TestCrawler(unittest.TestCase):
    
    def __init__(self):
        self.crawler = Crawler("http://pranavdhingra.me")

    def test_is_valid_domain(self):
        self.crawler.host = "qefwefwfwe"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.host = "http:wefwefwef.com"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.host = "https:wefwefwef"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.host = "http://wefwefwef.com"
        self.assertTrue(self.crawler.is_valid_domain())
        self.crawler.host = "http//wefwefwef.com"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.host = "https//wefwefwef.com"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.host = "http//wefwefwef.com"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.host = "https://pranavdhingra.me"
        self.assertTrue(self.crawler.is_valid_domain())
        self.crawler.host = "http://tomblomfield.com"
        self.assertTrue(self.crawler.is_valid_domain())
        self.crawler.host = "www.pranavdhingra.me"
        self.assertFalse(self.crawler.is_valid_domain())

    def test_create_url(self):
        pass

    def test_of_same_domain(self):
        pass

    def test_scrape(self):
        pass

    def test_crawlDFS(self):
        pass

    def test_crawlBFS(self):
        pass

if __name__ == "__main__":
    unittest.main()