MARSHALL   = 1
GENERAL    = 2
COLONEL    = 3
MAJOR      = 4
CAPTAIN    = 5
LIEUTENANT = 6
SERGEANT   = 7
MINER      = 8
SCOUT      = 9
SPY        = 10
BOMB       = 11
FLAG       = 12

attacker = CAPTAIN
defender = BOMB

ATTACKER = 1
DEFENDER = 2
TIE      = 3
NONSENSE = 4

def attack(attacker, defender):
    if attacker == SPY and defender == MARSHALL:
        return ATTACKER
    if attacker == BOMB or attacker == FLAG:
        return NONSENSE
    if defender == BOMB and attacker == MINER:
        return ATTACKER
    if defender == BOMB:
        return DEFENDER
    if attack == defender:
        return TIE
    if attacker < defender:
        return ATTACKER
    if defender < attacker:
        return DEFENDER
    return TIE
    
#=======================================================================================
TEST_CASES = [(MARSHALL, SCOUT,    ATTACKER),
              (MINER,    SCOUT,    ATTACKER),
              (SCOUT,    MARSHALL, DEFENDER),
              (SCOUT,    MINER,    DEFENDER),
              (GENERAL,  MARSHALL, DEFENDER),
              (MARSHALL, MARSHALL, TIE),
              (SCOUT,    SCOUT,    TIE),
              (MARSHALL, BOMB,     DEFENDER),
              (MINER,    BOMB,     ATTACKER),
              (SCOUT,    SPY,      ATTACKER),
              (SPY,      SCOUT,    DEFENDER),
              (SPY,      MARSHALL, ATTACKER),
              (MARSHALL, SPY,      ATTACKER),
              (BOMB,     MARSHALL, NONSENSE),
              (FLAG,     BOMB,     NONSENSE)
              ]

def testAttack():
    success = True
    for testCase in TEST_CASES:
        attacker = testCase[0]
        defender = testCase[1]
        expected = testCase[2]
        actual   = attack(attacker, defender)
        if (expected != actual):
            success = False
            print("attack() failed: ", attacker, "attacked", defender,
                  "and I expected", expected, "but your code returned", actual)
    if (success):
        print("All tests passed!")

if __name__ == '__main__':
    testAttack()    
