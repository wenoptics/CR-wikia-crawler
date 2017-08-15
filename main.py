from CardList import get_all_cards
from SingleCard import SingleCard
from utils.MultithreadingHelper import AutoMTTask
# TODO use pydblite

def write_csv(db:list):
    f = open('save.csv', 'w')
    for d in db:
        f.write("%s,%s,%s,%s,%s,%s,%s" % (d[0], d[1], d[2], d[3], d[4], d[5], d[6]))
        f.write("\n")


class ParseCard(AutoMTTask):
    def jobs(self, one_card):
        cardURL = one_card[1]
        sc = SingleCard()
        cardInfo = sc.fetch_from_wikia(cardURL)
        return [
            cardInfo.get("Name"),
            cardInfo.get("Elixir"),
            cardInfo.get("Type"),
            cardInfo.get("Rarity"),
            cardInfo.get("ImageURL"),
            cardInfo.get("Update"),
            cardURL,  # WikiaURL of the card
        ]


if __name__ == '__main__':
    cards = get_all_cards()
    pc = ParseCard()
    pc.set_task_list(cards)
    infos = pc.go(threads_num=12)

    write_csv(db=infos)
    print('done')
