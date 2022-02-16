from math import ceil
import random
import sys


def interact(res, val, min_val, max_val):
    """
    Interact with user
    """
    if res == ">=":
        if(val >= max_val):
            return val, min_val, max_val, True
        min_val = val
        val = ceil((val + max_val) / 2)
    elif res == "<":
        if(val < min_val):
            return val, min_val, max_val, True
        max_val = val-1
        val = int((val + min_val) / 2)

    return val, min_val, max_val, False


def tester(val, guess):
    """
    Guess the numer
    """
    # if guess == val:
    #     return "! "
    if guess >= val:
        return ">="
    else:
        return "<"


def basic_fun(i):
    a = 1
    b = 1000000
    # guess = random.randint(a, b)
    guess = i

    mid = ceil((a+b)/2)
    count = 0
    while(True):
        # print(mid)
        # sys.stdout.flush()
        count += 1
        res = tester(mid, guess)
        # res = input()
        if count >= 25:
            return count
        if res.startswith("!"):
            print(res)
            break
        mid, a, b, flag = interact(res, mid, a, b)
        if flag:
            # print("")
            print("HERE, Guess : ", guess)
            print("! {}".format(mid))
            print(count)
            if(count >= 25):
                return False

            return guess == mid
            break
    return False


if __name__ == "__main__":
    for i in range(1, 1000000):
        if(basic_fun(i)):
            print("Found : ", i)
        else:
            break
