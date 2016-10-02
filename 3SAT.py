import numpy as np

hoge = (True,False)

def RANDOM_WALK_3SAT(f,n,R):
    """
    f is a 3-CNF
    each raw(= a clause) contains 3 literals and raws presents clauses
    - example
        f = [[1,2,3],[-1,4,-2]]
        this means (x1 or x2 or x3) and ('not x1' or x4 or 'not x2')
    n = # valuables
    """
    r = 1
    while r <= R:
        a = np.random.choice(hoge,n)
        # a is a list containing booleans x1 x2 x3,...
        k = 1
        while k <= 3*n:
            # SATISFIED return false if a satisfies f, else return the valuable in a which doesn't match f
            test = SATISFIED(f,a)
            if (type(test) == bool ):
                return a
            a = test
            k += 1
        r += 1
    return False

def Or(f):
    m = 0
    for boolean in f:
        m += int(boolean)
    if m > 0:
        return True
    else :
        return False

def SATISFIED(clauses,a):
    # if a satisfies clauses, return a itself otherwise return modified a
    for clause in clauses:
        b = []
        """
        - example
            clauses = [[1,2,3],[-2,3,4]]
            clause = [1,2,3]
            a = [True, False, True, True]
        """
        for i in clause:
            """
            - example
                i is in {1,2,3,...n}, represents the index number
                a[i-1] = True or False
            """
            if i > 0:
                b.append(a[i-1])
            else :
                i = i*(-1)
                b.append((not a[i-1]))
        """
        example : b = [True False True]
        each clause must be True for all clauses being True
        if all clauses is True, then each clause should be True
        if Or(b) is false, change one of the false valuables and return it
        """
        if not(Or(b)):
            # temp contains false valuables
            temp = [i for i in xrange(3) if (not b[i])]
            hoho = np.random.choice(temp)
            a[abs(clause[hoho])-1] = not a[abs(clause[hoho])-1]
            return a
    return True

# F = [[1,2,3],[4,2,-3],[-1,3,4],[-1,-4,2],[-4,-2,3],[-1,-2,-3],[1,-4,-3],[1,4,-2]]
# A = [True,False,False,True]
#
# print SATISFIED(F,A)
# print RANDOM_WALK_3SAT(F,4,10)
