from collections import deque
import random

def single_game(seq1, seq2):
    seq1 = deque(seq1)
    seq2 = deque(seq2)
    coins = ['R', 'O']
    res = deque(random.choices(coins, k=len(seq1)))
    throws = len(seq1)
    if res == seq1 or res == seq2:
        if res == seq1:
            print(f"First player won and he needed for this {throws} throws")
            return 1
        if res == seq2:
            print(f"Second player won and he needed for this {throws} throws")
            return 2
    while res != seq1 and res != seq2:
        throws += 1
        res.popleft()
        res.append(random.choice(coins))
        if res == seq1:
            print(f"First player won and he needed for this {throws} throws")
            return 1
        if res == seq2:
            print(f"Second player won and he needed for this {throws} throws")
            return 2

def simulate_games(seq1, seq2, num_games):
    for i in range(num_games):
        simulation = single_game(seq1, seq2)
        results.append(simulation)

def show_results(results):
    n = len(results)
    print(f"\nWe simulated {n} games \nFirst player won {results.count(1)} of them"
          f"\nSecond player won {results.count(2)} of them")

a, b = list(), list()
while len(a) <= 3:
    coin = input(f"Please first player enter {len(a) + 1} coin (only big letters 'R' or 'O': ").strip()
    if coin in ['R', 'O']:
        a.append(coin)
while len(b) <= 3:
    coin = input(f"Please second player enter {len(b) + 1} coin (only big letters 'R' or 'O': ").strip()
    if coin in ['R', 'O']:
        b.append(coin)
    if a == b:
        b.pop()
        print("You can't use this combination because first player has the same. Please choose other last coin!")

n = int(input("How many simulations do you want to run? "))
results = list()
simulate_games(a, b, n)
show_results(results)