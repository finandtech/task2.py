import random

# phase 1 Zookeeper inference, 2% margin of error (moe)
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

        minimum = 0
        both = 0

    # Phase 3 Replicate scenario 100k times and get percents/proportions
    # Elephant one: Jane
    # Elephant two Fred

        for probability in range(100000):
            elphOne = random.randint(1, 6)
            elphTwo = random.randint(1, 6)
            zkpr = random.randint(1, 6)

            if elphOne == zkpr or elphTwo == zkpr:
                minimum = minimum + 1

            if elphOne == zkpr and elphTwo == zkpr:
                both = both + 1

        prop1 = (minimum * 100) / float(100000)
        prop2 = (both * 100) / float(100000)

    # Print statements after running simulation

        print("What percentage of the time there is at least one elephant in the pen :%.2f" % prop1, "%")
        print("What percentage of time are both elephants in the pen? :%.2f" % prop2, "%")
        while (prop1 >= tierceLower and prop2 <= tierceUpper) and (prop2 >= halfTierceLower and prop2 <= halfTierceUpper):
            print("Therefore ZOOKEPER is right ")
        else:
            print("Therefore CUSTODIAN is right")

        repeat = input("Repeat simulation? (yes or no):").lower()

        while repeat == "yes":
            replicate()
            break
        else:
            print("Simulation over")



replicate()
