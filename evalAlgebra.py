def evalAlgebra(s):
    y=s[s.index('=')+2:]
    x=s[:s.index('=')]
    for i in range(0,len(s)):
        if s[i]=='x':
            if i>(s.index('+') or s.index('-')):
                a=s[:i-2]
            else:
                a=s[i:s.index('=')-2]
    if '+' in s:
        return int(y)-int(a)
    elif '-' in s:
        if (s.index('-')>s.index('x')):
            return int(y)+int(a)
        else:
            return -(int(y)+int(a))
    
print(evalAlgebra("2 + x = 19"))
print(evalAlgebra("-23 + x = -20"))
print(evalAlgebra("10 + x = 5"))
            
