# O(n^2) 
def canCompleteCircuit(gas:list[int], cost:list[int]) -> int:
    for i in range(len(gas)):
        tank = gas[i]
        station = i
        while tank - cost[station] >= 0:
            tank -= cost[station]
            station = (station + 1) % len(gas)
            if station == i:
                return station
            tank += gas[station]
    return -1

# exceed time limit
def canCompleteCircuit2(gas:list[int], cost:list[int]) -> int:
    i = 0
    while i < len(gas):
        tank = gas[i]
        station = i
        while tank - cost[station] >= 0:
            tank -= cost[station]
            station = (station + 1) % len(gas)
            if station == i:
                return station
            tank += gas[station]
        if station + 1 == i: return -1
        if i == len(gas) - 1: return -1
        i = station + 1
    return - 1

def canCompleteCircuit3(gas:list[int], cost:list[int]) -> int:
    total = 0
    current = 0
    index = 0
    n = len(gas)
    for i in range(n):
        total += gas[i] - cost[i]
        current += gas[i] - cost[i]
        if current < 0:
            index = i + 1
            current = 0
    return index if total >= 0 else -1

def canCompleteCircuit4(gas:list[int], cost:list[int]) -> int:
    if sum(gas) < sum(cost): return -1
    current = 0
    index = 0
    for i in range(len(gas)):
        current += gas[i] - cost[i]
        if current < 0:
            index = i + 1
            current = 0
    return index
            



if __name__=='__main__':
    print(canCompleteCircuit3([1,2,3,4,5], [3,4,5,1,2]))
    print(canCompleteCircuit3([2,3,4], [3,4,3]))
    print(canCompleteCircuit3([1,2,3,4,3,2,4,1,5,3,2,4],[1,1,1,3,2,4,3,6,7,4,3,1]))
    