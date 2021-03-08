import random

# phase 1 Zookeeper guesses 2% margin of error (moe)
def replicate():
    moe = 0.02

# 1/3rd of the time, there's at least one elephant in the pen

    tierce = 1/3
    tierceLower = tierce - moe
    tierceUpper = tierce + moe

#  1/6th of the time the other elephant is in there as well

    halfTierce = 1 / 6
    halfTierceLower = halfTierce - moe
    halfTierceUpper = halfTierce + moe

# Phase 2 establish scenarios 1/6 probability
    minimum = 0
    both = 0

# Phase 3 Replicate scenario 100k times

    for i in range(100000):
        elphOne = random.randint(1, 6)
        elphTwo = random.randint(1, 6)
        zkpr = random.randint(1, 6)

    if elphOne == zkpr or elphTwo == zkpr:
        minimum = minimum + 1

    if elphOne == zkpr and elphTwo == zkpr:
        both = both + 1

# Phase 4 Get percents/proportions

    prop1 = (minimum * 100) / 100000
    prop2 = (both * 100) / 100000

    print("What percent of the time a single elephant is in a pen :%.2f" % prop1, "%")
    print("What percent of the time a two elephants are in a pen :%.2f" % prop2, "%")
    if (prop1 >= tierceLower and prop2 <= tierceUpper) and (prop2 >= halfTierceLower and prop2 <= halfTierceUpper):
        print("Zookeeper is right ")
    else:
        print("Custodian is right")

    run = input("Repeat experiment? (yes or no):")
    if run == "no":
        replicate()


