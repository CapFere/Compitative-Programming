import copy
def main():
    t = eval(input())
    while t > 0:
        n = eval(input())
        test_input = input().split()
        data = [int(x) for x in test_input]
        yasser = sum(data)
        result = combinations([],data,yasser,n)
        if result:
            print('YES')
        else:
            print('NO')
        t -= 1
            
def combinations(target,data,yasser,n):
    isYES = True
    for i in range(len(data)):
        new_target = copy.copy(target)
        new_data = copy.copy(data)
        new_target.append(data[i])
        new_data = data[i+1:]
        if len(new_target) != n and yasser <= sum(new_target):
            return False
        if not combinations(new_target,new_data,yasser,n):
            isYES = False
            break
    return isYES

main()