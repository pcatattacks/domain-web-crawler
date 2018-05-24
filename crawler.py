
# We'd like you to write a simple web crawler in a programming language of your choice. Feel free to either choose one you're very familiar with or, if you'd like to learn some Go, you can also make this your first Go program! The crawler should be limited to one domain - so when crawling tomblomfield.com it would crawl all pages within the domain, but not follow external links, for example to the Facebook and Twitter accounts. Given a URL, it should output a site map, showing which static assets each page depends on, and the links between pages.

# Ideally, write it as you would a production piece of code. Bonus points for tests and making it as fast as possible!

import requests as req # request library
from bs4 import BeautifulSoup # scraping library
from urlparse import urlparse # parsing library
import sys
import json

class Crawler(object):

    def __init__(self, url):
        self.url = url
        self.crawled = set()
        self.sitemap = None
        self.parsed_url = urlparse(url)
        self.host = self.parsed_url.netloc
        if self.host.startswith('www.'):
            self.host = self.host[4:] # removing www.
            print self.host
        if not self.is_valid_domain():
            print >> sys.exit(1), "Typed an invalid domain."

    def is_valid_domain(self):
        # TODO
        # test whether http:// provided etc, test whether is subdomain or domain
        return True

    def of_same_domain(self, href):
        ignore_values = {"", "/"}
        # ignore if href is not set
        if not href:
            return False
        # ignore if it is just a link to the same page
        if href.startswith("#"):
            return False
        # skip ignored values
        if href in ignore_values:
            return False
        # if domains dont match    
        parsed_href = urlparse(href)
        if parsed_href.netloc != '' and parsed_href.netloc != self.host and parsed_href.netloc != ("www."+self.host):
            return False
        return True

    def create_url(self, path):
        return "http://" + self.parsed_url.netloc + path

    def scrape(self, url):
        markup = req.get(url).text
        soup = BeautifulSoup(markup, 'lxml')
        links = [a["href"] for a in soup.find_all("a", href=self.of_same_domain)] # extracting links
        return links
    
    # TODO - do something about default param
    def crawlDFS(self, url=sys.argv[1], parent="/", site_part={}):
        # print "\ncrawling "+url # debug
        links = self.scrape(url)
        for l in links:
            # print "raw href: " + l # debug
            if l[0] == "/":
                l = self.create_url(l)
            # print l, parent, url # debug
            if l == parent or l == url:
                continue
            if l not in self.crawled:
                site_part[l] = {}
                self.crawled.add(l)
                self.crawlDFS(l, url, site_part[l])
        self.sitemap = site_part
    
    # TODO - Breadth first search function
    def crawlBFS(self, url=sys.argv[1]):
        # self.sitemap = {}
        queue = []
        # depth_queue = []
        queue.append(url)
        # depth_queue.append(0)
        while queue:
            l = queue.pop(0)
            # d = depth_queue.pop(0)
            if l == url: # same link
                continue
            if l[0] == "/":
                l = self.create_url(l)
            # site_part[l] = {}
            # for i in range(d):
            #     site_part = self.sitemap[l]
            for link in self.scrape(l):
                if link not in self.crawled:
                    queue.append(link)
                    self.crawled.add(link)

    def display_sitemap(self):
        print json.dumps(self.sitemap, indent=2)


def main():
    crawler = Crawler(sys.argv[1])
    crawler.crawlDFS()
    crawler.display_sitemap()

if __name__ == "__main__":
    main()