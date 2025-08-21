import logging
import random

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
def dice_roll(n):
    for i in range(n):
        logging.debug("Iterating dice roll")
        print(random.randint(1, 6))


dice_roll(10)