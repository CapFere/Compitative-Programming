def main():
    weight = int(input())
    found = False
    division = 1
    while division<=weight//2:
        if division % 2==0 and (weight-division) %2 == 0:
            print("YES")
            found = True
            break
        division = division + 1
    if not found:
        print("NO")
    
main()