def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        p = fibonnaci(n - 1)
        a = fibonnaci(n - 2)
        return p + a
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def compareTo(s1, s2):
    if not s1 == '' and not s2 == '':
        if s1[0] < s2[0]:
            return -1
        if s1[0] == s2[0]:
            return 0
        return 1, compareTo(s1[1:], s2[1:])

if __name__ == '__main__':
    fibresult = fibonnaci(5)
    gcd = gcd(5,4)
    compareTo = compareTo('5','2')
    print('result is: {}'.format(fibresult))
    print('The gcd is: {}'.format(gcd))
    print(compareTo)