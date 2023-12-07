with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

class Card:
    def __init__(self, value, bid, tipo) -> None:
        self.value = value
        self.bid = bid
        self.tipo = tipo
    
    def __lt__(self, card):
        for i in range(5):
            if dic_scores[self.value[i]] > dic_scores[card.value[i]]:
                return False
            elif dic_scores[self.value[i]] < dic_scores[card.value[i]]:
                return True

def card_type(card):
    print(card)
    card_labels = {}
    for n in card:
        if n != "J":
            if n in card_labels:
                card_labels[n] += 1
            else:
                card_labels[n] = 1
    c_type = sorted(list(card_labels.values()))
    number_of_J = card.count("J")
    if number_of_J == 5:
        c_type = [5]
    else:
        c_type[len(c_type)-1] += number_of_J
    if c_type == [5]:
        return "five-of-a-kind"
    elif c_type == [1, 4]:
        return "four-of-a-kind"
    elif c_type == [2, 3]:
        return "full-house"
    elif c_type == [1, 1, 3]:
        return "three-of-a-kind"
    elif c_type == [1, 2, 2]:
        return "two-pair"
    elif c_type == [1, 1, 1, 2]:
        return  "one-pair"
    else:
        return "high-card"

types = ["five-of-a-kind", "four-of-a-kind", "full-house", "three-of-a-kind", "two-pair", "one-pair", "high-card"]
scores = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
dic_scores = {scores[i]:(len(scores)-i) for i in range(0, len(scores))}

cards_objects = []
for card in input:
    cards_objects += [Card(card[:5], int(card[6:]), card_type(card[:5]))]

rank = []
for t in types:
    cards_of_a_type = list(filter(lambda x: x.tipo == t, cards_objects))
    cards_of_a_type.sort(reverse=True)
    for c in cards_of_a_type:
        rank.append(c)

total = 0
for i in range(len(rank)):
    total += rank[i].bid*(1001-(i+1))

print(total)