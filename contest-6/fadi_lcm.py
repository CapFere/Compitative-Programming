def main():
    x = eval(input())
    has_prev = False
    p = 1
    q = 1
    for b in range(1,x+1):
        for t in range(b+1,x+1):
            if lcm(b,t) == x and has_prev:
                print('d',b,t)
                if q > t:
                    p = b
                    q = t
            elif lcm(b,t) == x and not has_prev:
                p = b
                q = t
                has_prev = True
    print(p,q)

def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 

def lcm(a,b): 
    return (a*b) / gcd(a,b)
main()