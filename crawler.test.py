import unittest
from crawler import *

class TestCrawler(unittest.TestCase):
    
    crawler = Crawler("http://pranavdhingra.me")

    def test_is_valid_domain(self):
        self.crawler.url = "qefwefwfwe"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.url = "http:wefwefwef.com"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.url = "https:wefwefwef"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.url = "http://wefwefwef.com"
        self.assertTrue(self.crawler.is_valid_domain())
        self.crawler.url = "http//wefwefwef.com"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.url = "https//wefwefwef.com"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.url = "http//wefwefwef.com"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.url = "https://pranavdhingra.me"
        self.assertTrue(self.crawler.is_valid_domain())
        self.crawler.url = "http://tomblomfield.com"
        self.assertTrue(self.crawler.is_valid_domain())
        self.crawler.url = "www.pranavdhingra.me"
        self.assertFalse(self.crawler.is_valid_domain())
        self.crawler.url = "http://fwefewfwefewfe"
        self.assertTrue(self.crawler.is_valid_domain())

    def test_of_same_domain(self):
        self.crawler.url = "https://pranavdhingra.me"
        self.assertTrue( self.crawler.of_same_domain("www.tumblr.com/hello") )
        # Yes, there must always be an http prepended to it. so this is of the same domain, since it implies
        # https://pranavdhingra.me/www.tumblr.com/hello
        self.assertFalse( self.crawler.of_same_domain("http://tumblr.com/hello") )
        self.assertFalse( self.crawler.of_same_domain("https://www.tumblr.com/hello") )
        self.assertTrue( self.crawler.of_same_domain("sup/hello") )
        self.assertTrue( self.crawler.of_same_domain("./sup/hello") )
        self.assertTrue( self.crawler.of_same_domain("../sup/hello") )
        self.assertTrue( self.crawler.of_same_domain("/sup/hello") )
        self.assertTrue( self.crawler.of_same_domain("myfile.ext") )
        self.assertTrue( self.crawler.of_same_domain("http://pranavdhingra.me/sup/hello") )
        self.assertTrue( self.crawler.of_same_domain("https://www.pranavdhingra.me/sup/hello") )

    def test_create_url(self):
        self.assertEqual(self.crawler.create_url("sup/hello"), "http://pranavdhingra.me/sup/hello", "created URL doesn't match.")
        self.assertEqual(self.crawler.create_url("./sup/hello"), "http://pranavdhingra.me/sup/hello", "created URL doesn't match.")
        self.assertEqual(self.crawler.create_url("../sup/hello"), "http://pranavdhingra.me/../sup/hello", "created URL doesn't match.")
        self.assertEqual(self.crawler.create_url("/sup/hello"), "http://pranavdhingra.me/sup/hello", "created URL doesn't match.")
        self.assertEqual(self.crawler.create_url("myfile.ext"), "http://pranavdhingra.me/myfile.ext", "created URL doesn't match.")
        self.assertEqual(self.crawler.create_url("www.tumblr.com/hello"), "http://www.tumblr.com/hello", "created URL doesn't match.")

    # These tests are a little complicated to write and will take time, so I've left them for now.
    # Follow up over the phone call discussing design decisions.
    # I can talk about the process there!
    def test_scrape(self):
        pass

    def test_crawlDFS(self):
        pass

    def test_crawlBFS(self):
        pass

if __name__ == "__main__":
    unittest.main()