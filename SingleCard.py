from io import StringIO
import lxml.html
from lxml import etree
from base import get_html_string
from datetime import datetime

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

class SingleCard:

    def __init__(self):

        self.varCardData = {
            'Name': '',
            'Elixir': '',
            'Type': '',
            'Rarity': '',
            'ImageURL': '',
            'Update': ''
        }

    def __htmlProcessor_wikiHistory(self, html):
        parser = etree.HTMLParser()
        tree = etree.parse(StringIO(html), parser)

        # fetch revisionTime
        revisionTime = tree.getroot().xpath('//*[@id="pagehistory"]/li[1]/a')
        revisionTime = revisionTime[0].text
        #print("updateTime: %s" % revisionTime)

        date_object = datetime.strptime(revisionTime, '%H:%M, %B %d, %Y')
        print("updateTime", date_object)
        print('')

        self.varCardData['Update'] = date_object

    def __htmlProcessor_cardInfo(self, html):
        parser = etree.HTMLParser()
        tree = etree.parse(StringIO(html), parser)

        # fetch card name
        cardName = tree.getroot().xpath('//*[@id="WikiaPageHeader"]/div[1]/div[1]/h1')
        cardName = cardName[0].text
        print("Card: %s" % cardName)
        self.varCardData['Name'] = cardName

        # fetch the image
        cardImageURL = tree.getroot().xpath('//*[@id="mw-content-text"]//div[@class="center"]/div[@class="floatnone"]/img')
        cardImageURL = cardImageURL[0].attrib.get('src')
        print("Image URL:", cardImageURL)
        self.varCardData['ImageURL'] = cardImageURL

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

        _r = varAttrTbl.get('Rarity')
        _t = varAttrTbl.get('Type')
        _e = varAttrTbl.get('Cost')
        try:
            _e = int(_e)
        except ValueError:
            _e = '?'

        print("Rarity:", _r)
        print("Type:" , _t)
        print("Elixir Cost:" , _e)
        self.varCardData['Type']   = _t
        self.varCardData['Elixir'] = _e
        self.varCardData['Rarity'] = _r


    def fetchFromWikia(self, URL):

        url = URL
        html = get_html_string(url)
        html = html.decode("utf8")
        self.__htmlProcessor_cardInfo(html)

        url += '?action=history'
        html = get_html_string(url)
        html = html.decode("utf8")
        self.__htmlProcessor_wikiHistory(html)

        return self.varCardData



if __name__ == '__main__':
    url = 'http://clashroyale.wikia.com/wiki/Goblin_Barrel'
    #url = 'http://clashroyale.wikia.com/wiki/Mirror'
    url = 'http://clashroyale.wikia.com/wiki/Lava_Hound'

    sc = SingleCard()
    data = sc.fetchFromWikia(url)

    print(data)

