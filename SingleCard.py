from io import StringIO
import lxml.html
from lxml import etree
from base import get_html_string

'''

 fields that need to be fetch
   * update datetime
   * card name
   * card elixir cost
   * card type {Troop / Spell / Building}
   * card rarity
   * png filename
   * wikia url

'''


def htmlProcessor_wikiHistory(html):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)

    # fetch revisionTime
    revisionTime = tree.getroot().xpath('//*[@id="pagehistory"]/li[1]/a')
    revisionTime = revisionTime[0].text
    print("updateTime: %s" % revisionTime)


def htmlProcessor_cardInfo(html):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)

    # fetch card name
    cardName = tree.getroot().xpath('//*[@id="WikiaPageHeader"]/div[1]/div[1]/h1')
    cardName = cardName[0].text
    print("Card: %s" % cardName)

    # fetch the image
    cardImageURL = tree.getroot().xpath('//*[@id="mw-content-text"]/div[@class="center"]/div[@class="floatnone"]/img')
    cardImageURL = cardImageURL[0].attrib.get('src')
    print("Image URL:", cardImageURL)

    # data from attrib table
    tblCount = tree.getroot().xpath('//table[@id="unit-attributes-table"]/tr[1]/th')
    tblCount = len(tblCount)
    print('count of attribute table:', tblCount)

    varAttrTbl = {}
    for c in range(tblCount):
        i = c+1
        tblTitle = tree.getroot().xpath('//table[@id="unit-attributes-table"]/tr[1]/th[%d]' % i)
        tblContent = tree.getroot().xpath('//table[@id="unit-attributes-table"]/tr[2]/td[%d]' % i)
        tblContent2 = tree.getroot().xpath('//table[@id="unit-attributes-table"]/tr[2]/td[%d]/a' % i)
        tblContent3 = tree.getroot().xpath('//table[@id="unit-attributes-table"]/tr[2]/td[%d]/a/span' % i)

        tblTitle = tblTitle[0].text
        tblContent = tblContent[0].text
        if tblContent2:
            tblContent = tblContent2[0].text
        if tblContent3:
            tblContent = tblContent3[0].text
        # print(" %d , %s, %s" % (i, tblTitle, tblContent))
        varAttrTbl[tblTitle.strip()] = tblContent.strip()

    print("Rarity: %s" % varAttrTbl.get('Rarity'))
    print("Type: %s" % varAttrTbl.get('Type'))
    print("Elixir Cost: %s" % varAttrTbl.get('Cost'))


if __name__ == '__main__':
    url = 'http://clashroyale.wikia.com/wiki/Goblin_Barrel'
    html = get_html_string(url)
    html = html.decode("utf8")
    htmlProcessor_cardInfo(html)

    url += '?action=history'
    html = get_html_string(url)
    html = html.decode("utf8")
    htmlProcessor_wikiHistory(html)

