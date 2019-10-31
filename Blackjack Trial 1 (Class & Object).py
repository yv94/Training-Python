import random


cardlist = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4
dead = False


class Cards:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2


player = Cards(random.choice(cardlist), random.choice(cardlist))
dealer = Cards(random.choice(cardlist), random.choice(cardlist))
playertotal = 0

print(player.card1, player.card2)

while dead is not True:
    for each facecard in 
    else:
        print("not 10")
    print(playertotal)
    input()
    """choice = input("Do you want to (h)it or (s)tay?")
    if choice == "h":
        print("You get dealt an additional card..")
        input()
        print("You get dealt a " + random.choice(cardlist))"""



