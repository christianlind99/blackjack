import random
from matplotlib import pyplot as plt

unit = 20  # initial bet and what you end up winning if eventually win
games = 10  # number of games per session
sessions = 365  # number of session. eg per month
bank = [15000]  # initial money available for gambling
handlist = []
inp = input("If you want a custom winrate, enter multiple now (eg 0.48), otherwise hit enter")
if inp == "":
    winodds = 0.495
else:
    winodds = float(inp)


for j in range(sessions):  # this loop runs a new gambling session
    winnings = 0
    table = unit
    l = 0
    for i in range(games):  # this loop runs a round
        while True:  # this loop simulates a game run till won
            if random.random() > winodds:  # loss
                table = table * 2
            else:  # won
                winnings = unit
                break

        bank.append(bank[len(bank) - 1] + winnings)
        winnings = 0  # resets winnings to 0 after won game
        if table > l:  # stores the largest hand
            l = table
        handlist.append(l)
        table = unit

plt.plot(handlist, label="Max bet")
plt.plot(bank, label="Winnings")
plt.xlabel("Number of games played")
plt.ylabel("Money")
plt.title("Blackjack martingale simulation")
plt.legend()
plt.show()
