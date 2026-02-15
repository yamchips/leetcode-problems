from cmath import sqrt
import heapq
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:

    distances = []
    for point in points:
        distance = sqrt(point[0] ** 2 + point[1] ** 2)
        heapq.heappush(distances, (-distance, point))
        if len(distances) > k:
            heapq.heappop(distances)
    return [point for _, point in distances]