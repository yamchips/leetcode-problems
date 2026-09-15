'''
n is the number of steps

Time complexity:
    Create fatherSet: O(n)
    Iterate all possible velMartin: O(n)
    In one loop, we create a martinSet, in worst case it's very large
        eg, father velocity is 10000, steps is 10000, and martion velocity is 1
    Set intersection O(n)
    Overall it's larger than O(n**2)

Space complexity:
    FatherSet: O(n)
    martinSet O(n)
    each iteration clears old martinSet, so still O(n)
    Overall O(n)
'''
def commonFootsteps(fatherPos, martinPos, velFather, steps):
    # a set of father's position
    fatherSet = {fatherPos}
    for i in range(1, steps + 1):
        fatherSet.add(fatherPos + velFather * i)

    maxVelMartin = 0
    maxCommon = 0
    
    for i in range(steps + 1):
        velMartin = fatherPos + i * velFather - martinPos
        if velMartin == 0: # father and martin start at same position
            continue
        # a set of martin's position
        martinSet = set()
        martinStep = martinPos + velMartin
        while martinStep <= fatherPos + steps * velFather:
            martinSet.add(martinStep)
            martinStep += velMartin
        # set intersection, get the size; get the velocity
        commonSet = martinSet.intersection(fatherSet)    
        if len(commonSet) > maxCommon:
            maxCommon = len(commonSet)
            maxVelMartin = velMartin
        elif len(commonSet) == maxCommon:
            maxVelMartin = max(maxVelMartin, velMartin)
    return (maxCommon, maxVelMartin)

from math import gcd
'''
Optimal solution
'''
def commonFootsteps(fatherPos, martinPos, velFather, steps):
    d = fatherPos - martinPos
    g = gcd(d, velFather)

    maxCommon = 0
    maxVelMartin = 0

    start = 0 if d > 0 else 1
    for i in range(start, steps + 1):
        velMartin = d + i * velFather

        common = 1 + ((steps - i) * g) // velMartin

        if common > maxCommon:
            maxCommon = common
            maxVelMartin = velMartin
        elif common == maxCommon:
            maxVelMartin = max(maxVelMartin, velMartin)
    return maxCommon, maxVelMartin

if __name__=="__main__":
    print(commonFootsteps(3,2,2,20)) # 21 1
    print(commonFootsteps(3,3,2,20)) # x1 = x2, 20, 2
    print(commonFootsteps(3,0,2,20)) # 