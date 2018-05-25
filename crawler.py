
# We'd like you to write a simple web crawler in a programming language of your choice. Feel free to either choose one you're very familiar with or, if you'd like to learn some Go, you can also make this your first Go program! The crawler should be limited to one domain - so when crawling tomblomfield.com it would crawl all pages within the domain, but not follow external links, for example to the Facebook and Twitter accounts. Given a URL, it should output a site map, showing which static assets each page depends on, and the links between pages.

# Ideally, write it as you would a production piece of code. Bonus points for tests and making it as fast as possible!

import requests as req # request library
from bs4 import BeautifulSoup # scraping library
from urlparse import urlparse # parsing library
import sys
import json

class Crawler(object):

    def __init__(self, url, verbose=False):
        self.verbose = verbose
        self.url = url
        self.crawled = set()
        self.sitemap = {}
        self.parsed_url = urlparse(url)
        self.host = self.parsed_url.netloc
        if self.host.startswith('www.'):
            self.host = self.host[4:] # removing www.
            print self.host
        if not self.is_valid_domain():
            print >> sys.stderr, "Domain must start with http:// or https://."
            sys.exit(1)

    def is_valid_domain(self):
        # test whether http:// provided etc, test whether is subdomain or domain
        if not self.url.startswith("http://") and not self.url.startswith("https://"):
            return False
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
        if path.startswith("./"): # starts with ./
            return "http://" + self.parsed_url.netloc + path[1:]
        elif path[0] == "/":
            return "http://" + self.parsed_url.netloc + path
        elif path.startswith("www."):
            return "http://" + path
        else: # looks like blah/blah
            return "http://" + self.parsed_url.netloc + "/"+path

    def scrape(self, url):
        # making sure that an error on the server's end doesn't stop the crawling
        try:
            res = req.get(url)
            markup = res.text
        except:
            return []
        if not res.headers["content-type"].startswith("text/html") and not res.headers["content-type"].startswith("text/xml"): # making sure only html is crawled
            if self.verbose:
                print "Non HTML content"
            return []
        soup = BeautifulSoup(markup, 'lxml')
        links = [a["href"] for a in soup.find_all("a", href=self.of_same_domain)] # extracting links
        return links
    
    def crawlDFShelper(self, url=None, site_part={}):
        if self.verbose:
            print "Crawling "+url + '\n'
        links = self.scrape(url)
        for l in links:
            if not l.startswith("http"):
                l = self.create_url(l)
            if l not in self.crawled:
                site_part[l] = {}
                self.crawled.add(l)
                self.crawlDFShelper(l, site_part[l])
        return site_part

    def crawlDFS(self):
        self.crawled.add(self.url)
        self.sitemap = { self.url: self.crawlDFShelper(self.url) }
    
    def crawlBFS(self):
        queue = []
        queue.append( (self.url, self.sitemap) )
        while queue:
            l, site_map = queue.pop(0)
            if self.verbose:
                print "Crawling "+ l + '\n'
            if not l.startswith("http"):
                l = self.create_url(l)
            site_map[l] = {}
            for link in self.scrape(l):
                if link not in self.crawled:
                    queue.append( (link, site_map[l]) )
                    self.crawled.add(link)

    def display_sitemap(self):
        print json.dumps(self.sitemap, indent=4)


def main():
    
    if "verbose" in sys.argv:
        crawler = Crawler(sys.argv[1], True)
    else:
        crawler = Crawler(sys.argv[1])
    
    err = False
    try:
        if "dfs" in sys.argv:
            crawler.crawlDFS() # DEPTH FIRST SEARCH CRAWL
        else:
            crawler.crawlBFS() # BREADTH FIRST SEARCH CRAWL - Outputs a correctly structured sitemap.
    except:
        err = True
        print >> sys.stderr, "An unknown error occured.\n"
    # if some unknown error occurs, at least whats already been crawled will be printed
    crawler.display_sitemap()
    if err:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()