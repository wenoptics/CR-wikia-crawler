from base import get_html_string
from io import StringIO
import lxml.html
from lxml import etree
from base import get_html_string

URL_prefix = 'http://clashroyale.wikia.com'


def __htmlProcessor_cardList(html):
    retList = []

    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)

    cardTableTr = tree.getroot().xpath('//*[@id="mw-content-text"]/table/tr[2]/td/table[1]/tr')
    # print(cardTable)

    for ind, _tr in enumerate(cardTableTr):
        if ind <= 1:
            continue
        links = _tr.xpath('.//a')
        print("Num of links in the card table row:", len(links))

        for oneLink in links:
            cardName = oneLink.text
            cardURLShort = oneLink.attrib.get('href')
            # print("%s: %s" % (cardName, cardURLShort))
            retList.append(
                [
                    cardName,
                    URL_prefix + cardURLShort
                ]
            )

    return retList


def get_all_cards():
    url = 'http://clashroyale.wikia.com/wiki/Cards'
    html = get_html_string(url)
    html = html.decode("utf8")
    return __htmlProcessor_cardList(html)


if __name__ == '__main__':
    url = 'http://clashroyale.wikia.com/wiki/Cards'
    html = get_html_string(url)
    html = html.decode("utf8")
    list = __htmlProcessor_cardList(html)
    print(list)
