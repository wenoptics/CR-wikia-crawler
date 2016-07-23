from CardList import getCardURL
from SingleCard import getOneCard

db = []

def writeCSV():
    f = open('save.csv', 'w')
    for d in db:
        f.write("%s, %s, %s, %s, %s, %s, %s" % (d[0], d[1], d[2], d[3], d[4], d[5], d[6]))

cards = getCardURL()
for oneCard in cards:
    print('=======================')
    cardURL = oneCard[1]
    cardInfo = getOneCard(cardURL)

    db.append(
        [
            cardInfo.get("Name"),
            cardInfo.get("Elixir"),
            cardInfo.get("Type"),
            cardInfo.get("Rarity"),
            cardInfo.get("ImageURL"),
            cardInfo.get("Update"),
            cardURL, # WikiaURL
        ]
    )
    #print(cardInfo)

writeCSV()