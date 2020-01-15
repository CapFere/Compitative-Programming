def distance(a,b,c):
    return abs(a-b) + abs(a-c) + abs(b-c)
def main():
    q=eval(input())
    count = 0
    while count < q:
        user_input=input().split()
        a=int(user_input[0])
        b=int(user_input[1])
        c=int(user_input[2])
        result = distance(a,b,c)
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    temp_result = distance(a+i,b+j,c+k)
                    if temp_result<result:
                        result = temp_result
        print(result)
        count+=1
main()