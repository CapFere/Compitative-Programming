def main():
    user_input = input().split()
    n,m,a = int(user_input[0]),int(user_input[1]),int(user_input[2])
    row = a
    column = a
    if a>=n or a>=m: flagstones = 1
    else: flagstones = 2
    while row < n or column < m:
        column = column + a
        row = row + a
        flagstones = flagstones + 2
    print(flagstones)

    
main()