def nom_nom(l):
    i=0
    while i<len(l)-1:
        if l[i]>l[i+1]:
            l[i]=l[i]+l[i+1]
            del l[i+1]
        else:
            i+=1
    return l
    
tests = [
    [5, 3, 7],
    [5, 3, 9],
    [1, 2, 3],
    [2, 1, 3],
    [8, 5, 9],
    [6, 5, 6, 100]
]

for t in tests:
    print(f"nom_nom({t})\nOutput = {nom_nom(t)}\n")
