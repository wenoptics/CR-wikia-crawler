from base import get_html_string
from io import StringIO
import lxml.html
from lxml import etree
from base import get_html_string


def htmlProcessor_cards(html):

    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)

    cardTable = tree.getroot().xpath('//*[@id="mw-content-text"]/table/tr[2]/td/table[1]')
    #print(cardTable)

    links = cardTable[0].xpath('.//a')
    print("count:", len(links))
    for oneLink in links:
        print("%s: %s" % (oneLink.text, oneLink.attrib.get('href')))


if __name__ == '__main__':

    url = 'http://clashroyale.wikia.com/wiki/Basics_of_Battle'
    html = get_html_string(url)
    html = html.decode("utf8")
    htmlProcessor_cards(html)
