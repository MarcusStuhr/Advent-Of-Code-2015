from itertools import groupby


ATOMIC_ELEMENTS =  ("1112",
                    "1112133",
                    "111213322112",
                    "111213322113",
                    "1113",
                    "11131",
                    "111311222112",
                    "111312",
                    "11131221",
                    "1113122112",
                    "1113122113",
                    "11131221131112",
                    "111312211312",
                    "11131221131211",
                    "111312211312113211",
                    "111312211312113221133211322112211213322112",
                    "111312211312113221133211322112211213322113",
                    "11131221131211322113322112",
                    "11131221133112",
                    "1113122113322113111221131221",
                    "11131221222112",
                    "111312212221121123222112",
                    "111312212221121123222113",
                    "11132",
                    "1113222",
                    "1113222112",
                    "1113222113",
                    "11133112",
                    "12",
                    "123222112",
                    "123222113",
                    "12322211331222113112211",
                    "13",
                    "131112",
                    "13112221133211322112211213322112",
                    "13112221133211322112211213322113",
                    "13122112",
                    "132",
                    "13211",
                    "132112",
                    "1321122112",
                    "132112211213322112",
                    "132112211213322113",
                    "132113",
                    "1321131112",
                    "13211312",
                    "1321132",
                    "13211321",
                    "132113212221",
                    "13211321222113222112",
                    "1321132122211322212221121123222112",
                    "1321132122211322212221121123222113",
                    "13211322211312113211",
                    "1321133112",
                    "1322112",
                    "1322113",
                    "13221133112",
                    "1322113312211",
                    "132211331222113112211",
                    "13221133122211332",
                    "22",
                    "3",
                    "3112",
                    "3112112",
                    "31121123222112",
                    "31121123222113",
                    "3112221",
                    "3113",
                    "311311",
                    "31131112",
                    "3113112211",
                    "3113112211322112",
                    "3113112211322112211213322112",
                    "3113112211322112211213322113",
                    "311311222",
                    "311311222112",
                    "311311222113",
                    "3113112221131112",
                    "311311222113111221",
                    "311311222113111221131221",
                    "31131122211311122113222",
                    "3113112221133112",
                    "311312",
                    "31132",
                    "311322113212221",
                    "311332",
                    "3113322112",
                    "3113322113",
                    "312",
                    "312211322212221121123222113",
                    "312211322212221121123222112",
                    "32112")

def matrixMult(A, B, MOD = None):
    """
    Multiplies two (assumed) square matrices A and B
    """
    heightAB, widthAB = len(A), len(B[0])
    AB = [[0 for y in xrange(widthAB)] for x in xrange(heightAB)]
    for i in xrange(heightAB):
        for j in xrange(widthAB):
            for k in xrange(len(B)):
                AB[i][j] += A[i][k] * B[k][j]
                if MOD != None: AB[i][j] %= MOD
    return AB


def matrixPow(M, k, MOD = None):
    """
    Computes the kth power of matrix M using exponentiation by squaring
    """
    if k==1:
        return M
    if k%2==0:
        A = matrixPow(M, k/2, MOD)
        return matrixMult(A, A, MOD)
    if k%2==1:
        return matrixMult(M, matrixPow(M, k-1, MOD), MOD)


def look_and_say(input_string):
    """
    Applies the Look-And-Say algorithm to input_string one time
    """
    return ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])


def verify_atoms(s,atoms):
    """
    Verifies that the string s will evolve in the same manner as the supplied atoms
    """
    new_atoms = atoms[:]
    for i in xrange(4):
        if s != ''.join(new_atoms):
            return False
        s = look_and_say(s)
        new_atoms = [look_and_say(atom) for atom in new_atoms]
    return True


def atomize_rec(s):
    if s in ATOMIC_ELEMENTS:
        yield [s]
    else:
        for i in xrange(1,len(s)):
            first, rest = s[:i], s[i:]
            if first in ATOMIC_ELEMENTS:
                for atoms in atomize_rec(rest):
                    yield [first] + atoms

def atomize(s):
    """
    Decomposes string s into Conway's atomic elements
    """
    for atoms in atomize_rec(s):
        if verify_atoms(s, atoms):
            return atoms
    raise Exception("String {} cannot be atomized into individual components".format(s))



def len_look_and_say(input_string, num_iterations, MOD = None):
    """
    Computes the length of the input_string after applying the Look-And-Say
    algorithm to it num_iterations times, modulo MOD if applicable.

    1. Uses a transition matrix detailing the evolution of Conway's atomic elements.

    2. Decomposes ("atomizes") the input_string into its corresponding elements

    3. Exponentiates the matrix, which will then describe, for a given element,
    how many of each OTHER element it would contain after num_iterations steps

    4. With that information, determine which elements are present in the
    evolution of input_string's atoms and sum up all the corresponding lengths.
    """
    n = len(ATOMIC_ELEMENTS)
    transition_matrix = [[0 for i in xrange(n)] for j in xrange(n)]
    atom_counts = [[0] for i in xrange(n)]

    for i in xrange(n):
        for atom in atomize(look_and_say(ATOMIC_ELEMENTS[i])):
            transition_matrix[i][ATOMIC_ELEMENTS.index(atom)]+=1

    for atom in atomize(input_string):
        atom_counts[ATOMIC_ELEMENTS.index(atom)][0] += 1

    exponentiated_mat = matrixPow(transition_matrix, num_iterations, MOD)
    sum_lens = 0

    for row in xrange(n):
        for col in xrange(n):
            sum_lens += len(ATOMIC_ELEMENTS[col]) * atom_counts[row][0] * exponentiated_mat[row][col]

    if MOD != None: sum_lens%=MOD
    return sum_lens



def main():
    initial_string = "1113122113"
    print "Answer to part 1: {}".format(len_look_and_say(initial_string, 40))
    print "Answer to part 1: {}".format(len_look_and_say(initial_string, 50))


if __name__ == "__main__":
    main()