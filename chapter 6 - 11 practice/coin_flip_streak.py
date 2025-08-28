import random


def coin_flip_streaks():
    history = []
    streak = 1
    coin = {0:'Head', 1:'Tail'}
    print("Commencing coin flips")
    for i in range(100):
        flip = random.randint(0,1)
        history.append(flip)
        
        if i > 0:
         if history[i] == history[i-1]:
            streak += 1

         else:
            streak = 1
        
        if streak == 6:
            print(f"There is a streak of {coin.get(history[-1])}!")
            streak = 1

    return history

print(coin_flip_streaks())
