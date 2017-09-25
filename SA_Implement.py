import random
from sys import float_info

def fungsi(x,y):
    fx = ((4-2.1*x1**2+(x1**4/3))*x1**2)+(x1*x2)+(-4+4*x2**2)*x2**2
    return fx

def probabilitasP(dE,T):
    return float_info.epsilon**(-dE/T)

if __name__=='__main__':
    x1 = random.uniform((-10-0.000000000192), (10-0.000000000192)) + 0.000000000192
    x2 = random.uniform((-10-0.000000000192), (10-0.000000000192)) + 0.000000000192
    T = 100000

    curr_state = fungsi(x1, x2)
    BEST_SO_FAR = curr_state

    i = 0
    for i in range(1, 1200000):
        x1 = random.uniform((-10-0.000000000192), (10-0.000000000192)) + 0.000000000192
        x2 = random.uniform((-10-0.000000000192), (10-0.000000000192)) + 0.000000000192
        # print x1,x2, T, fungsi(x1, x2)
        new_state = fungsi(x1, x2)
        DeltaE = curr_state - new_state
        print curr_state,i
        # print DeltaE

        if (DeltaE > 0):
            curr_state = new_state
            BEST_SO_FAR = curr_state
            # print BEST_SO_FAR
            # print i
        else:
            p = probabilitasP(DeltaE, T)
            if (p >= random.random()):
                curr_state = new_state
        T = T * 0.9

print('Bestever : '+str(BEST_SO_FAR))