import re
from collections import Counter


class Solution:

    def get_buzzy(self, toys, quotes, k):
        q = " ".join(quotes)
        q = q.lower()
        toys = "|".join(toys)
        # print(toys)
        q = re.findall(toys, q)

        q = Counter(q)
        return q.most_common(k)


quotes = [
    "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
    "The new Elmo dolls are super high quality",
    "Expect the Elsa dolls to be very popular this year, Elsa!",
    "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
    "For parents of older kids, look into buying them a drone",
    "Warcraft is slowly rising in popularity ahead of the holiday season"
]

toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]

topToys = 2

print(Solution().get_buzzy(toys, quotes, topToys))
