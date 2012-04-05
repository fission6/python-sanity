from sanity.formats.yaml import YAMLTestCase
import urllib2
from lxml import html, etree

def get_resource(testcase):
    print "Fetching", testcase.url
    url = testcase.url
    page = urllib2.urlopen(url)
    return html.fromstring(page.read())

def get_title(testpage):

    title = testpage.xpath('//title')[0]
    return title.text

def get_ids(testpage):
    
    ids = testpage.xpath("//*[@id]")
    ids = [ id.get('id') for id in ids ]
    return ids

def get_links(testpage):
    
    links = testpage.xpath('//a')
    links = [ link.get('href') for link in links ]
    return links

def test_title(page, test):
    title = get_title(page)
    test = title == test.title
    return test
    
def test_ids(page, test):
    ids = get_ids(page)
    test = all(id in test.ids for id in ids)
    return test
    
def test_links(page, test):
    links = get_links(page)
    test = all(link in test.links for link in links)
    return test

def main():
    
    test = YAMLTestCase()
    page = get_resource(test)
    
    test_result = {
        'title' : test_title(page, test),
        'ids' : test_ids(page, test),
        'links' : test_links(page, test),
    }
    
    for test, result in test_result.iteritems():
        print test, '-', result


if __name__ == '__main__':
    main()