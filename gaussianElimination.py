def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def findpivots(a):
    d = []
    for i in range(len(a)):
        for j in range(c):
            if (a[i][j] != 0):
                d.append((j, a[i]))
                break
    return d

def sortmatrix(d):
    d = sorted(d, key = lambda s: s[0])
    a = [i[1] for i in d]
    l = sorted([i[0] for i in d])
    return a, l

def reduce(a):
    w = 1

def pr():
    for i in range(r):
        print(a[i])

def eliminate(a, l):
    ind = 0
    reduceable = []
    nonreduceable = []
    ans = 0
    for i in a:
        if(l[ind] == l[0]):
            ans+=1
            reduceable.append(i)
        else:
            nonreduceable.append(i)
        ind+=1
    assert len(reduceable) >=1, "No Solution or Infinitely Many Solutions"
    t = reduceable[0][l[0]]
    for i in range(len(reduceable[0])):
        if(_ == 1):
            reduceable[0][i]*=modinv(t%mod, mod)
            reduceable[0][i]%=mod
        else:
            reduceable[0][i]/=t
    for j in range(1, len(reduceable)):
        kl = reduceable[j][l[0]]
        for i in range(0, len(reduceable[0])):
            reduceable[j][i]-=reduceable[0][i]*kl
    return ans,reduceable[0], reduceable[1:]+nonreduceable

def backwards(a):
    for i in range(c-2,0,-1):
        for j in range(0, i):
            kl = a[j][i]
            for k in range(c):
                a[j][k]-=a[i][k]*kl
    return a

print("Not Mod or Mod?")
_ = input()
assert _ == "Not Mod" or _ == "Mod", "Type \'Not Mod\' or \'Mod\'"
_ = 0 if _ == "Not Mod" else 1
if(_ == 1):
    print("Rows, Columns, Modulo:")
    temp = input().split()
    r, c, mod = int(temp[0][:-1]), int(temp[1][:-1]), int(temp[2])
else:
    print("Rows, Columns:")
    temp = input().split()
    r, c= int(temp[0][:-1]), int(temp[1])
a = [[0 for i in range(c)] for j in range(r)]
print("Array: ")
for i in range(r):
    t = input().split()
    asd = 0
    for j in t:
        a[i][asd] = int(j)/1.0
        asd+=1

final = []
print("")
print("Undergoing Gaussian Elimination...")
for v in a:
    print(v)
print(' |')
print(' \\/')


for i in range(r):
    d = findpivots(a)
    a, l = sortmatrix(d)
    skip, temp, h = eliminate(a, l)
    final+=[temp]
    a = h
    if(skip == 1):
        continue
    for v in (final+h):
        print(v)
    print(' |')
    print('\\/')
final = backwards(final)
for i in final:
    print([k%mod if _ == 1 else k for k in i])
print("")
print("Solutions:")
for i in final:
    print(int(i[c-1])%mod if _ == 1 else i[c-1])
