from cmath import inf
import heapq
from collections import defaultdict


class Customer:
    distance = defaultdict(int)

    def __init__(self, arrival_time, service_time, id):
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.distance[id] = arrival_time
        self.id = id

    def update_distance(self, time_passed):
        self.distance[self.id] = abs(self.arrival_time - time_passed)

    def remove_self(self):
        self.distance[id] = inf

    def __lt__(self, other):
        return self.distance[self.id]+self.service_time < self.distance[other.id]+other.service_time

    def __gt__(self, other):
        return self.distance[self.id]+self.service_time > self.distance[other.id]+other.service_time

    def __eq__(self, other):
        return self.distance[self.id]+self.service_time == self.distance[other.id]+other.service_time

    def __le__(self, other):
        return self.distance[self.id]+self.service_time <= self.distance[other.id]+other.service_time

    def __ge__(self, other):
        return self.distance[self.id]+self.service_time >= self.distance[other.id]+other.service_time

    def __ne__(self, other):
        return self.distance[self.id]+self.service_time != self.distance[other.id]+other.service_time

    def __str__(self):
        return str(self.id)

    def __repr__(self) -> str:
        return str("Customer(%d, %d, %d)" % (self.arrival_time, self.service_time, self.distance[self.id]))


class Solution:
    def get_average(self, customers):

        nc = []
        for i in range(len(customers)):
            nc.append(Customer(customers[i][0], customers[i][1], i))

        # print(nc[0].id)
        heapq.heapify(nc)
        # print(nc)
        t = 0
        tot = len(nc)
        acc_timepassed = 0
        while len(nc) > 0:
            l = heapq.heappop(nc)
            t += l.service_time
            # timepassed = l.service_time + t
            timepassed = t
            acc_timepassed += l.service_time + l.distance[l.id]
            # print(timepassed)
            # l.update_distance(timepassed)
            for i in nc:
                i.update_distance(timepassed)
            l.remove_self()
            # t += l.service_time
            # print(t)
            # print(l.distance)
            # print(nc)
        # print(acc_timepassed/tot)
        return acc_timepassed/tot


customers = [[0, 3], [1, 9], [2, 5]]

print(Solution().get_average(customers))
