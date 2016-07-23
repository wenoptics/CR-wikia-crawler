from CardList import getCardURL
from SingleCard import getOneCard

cards = getCardURL()
for oneCard in cards:
    print('=======================')
    cardURL = oneCard[1]
    cardInfo = getOneCard(cardURL)
    #print(cardInfo)