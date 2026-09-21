def canCompleteCircuit(gas:list[int], cost:list[int]) -> int:
    if sum(gas) < sum(cost): return -1
    n = len(gas)
    diff = [gas[i] - cost[i] for i in range(n)]
    index = 0
    tank = 0
    for i in range(n):
        tank += diff[i] 
        if tank < 0:
            # all indice in [0, i] can be discarded
            # the next possible station is i + 1
            index = i + 1
            tank = 0
    return index
            



if __name__=='__main__':
    print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3) 
    print(canCompleteCircuit([2,3,4], [3,4,3]) == -1)
    print(canCompleteCircuit([1,2,3,4,3,2,4,1,5,3,2,4],[1,1,1,3,2,4,3,6,7,4,3,1]))
    