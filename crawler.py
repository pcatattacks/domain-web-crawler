
# We'd like you to write a simple web crawler in a programming language of your choice. Feel free to either choose one you're very familiar with or, if you'd like to learn some Go, you can also make this your first Go program! The crawler should be limited to one domain - so when crawling tomblomfield.com it would crawl all pages within the domain, but not follow external links, for example to the Facebook and Twitter accounts. Given a URL, it should output a site map, showing which static assets each page depends on, and the links between pages.

# Ideally, write it as you would a production piece of code. Bonus points for tests and making it as fast as possible!

import requests as req # request library
from bs4 import BeautifulSoup # scraping library
from urlparse import urlparse # parsing library
import sys
import pprint

class Crawler(object):

    def __init__(self, url):
        self.url = url
        self.crawled = set()
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

    # TODO - do something about default param
    def crawl(self, url=sys.argv[1], parent="/", site_part={}):
        # print "\ncrawling "+url # debug
        markup = req.get(url).text
        soup = BeautifulSoup(markup, 'lxml')
        links = [a["href"] for a in soup.find_all("a", href=self.of_same_domain)] # extracting links
        for l in links:
            # print "raw href: " + l # debug
            if l[0] == "/":
                l = self.create_url(l)
            # print l, parent, url # debug
            if l == parent or l == url:
                continue
            # if l not in site_part and l not in self.crawled:
            #     site_part[l] = {}
            if l not in self.crawled:
                site_part[l] = {}
                self.crawled.add(l)
                self.crawl(l, url, site_part[l])
        self.sitemap = site_part

    def display_sitemap(self):
        pprint.pprint(self.sitemap)


def main():
    crawler = Crawler(sys.argv[1])
    crawler.crawl()
    crawler.display_sitemap()

if __name__ == "__main__":
    main()