def main():
    number_of_input = eval(input())
    count = 0
    while count < number_of_input:
        user_input = input().split()
        a,b,c,r = int(user_input[0]),int(user_input[1]),int(user_input[2]),int(user_input[3])
        if a > b: a,b = b,a
        left = 0
        right = 0
        c_left = c - r 
        c_right = c + r
        if c > a and c_left > a and c < b and c_right < b:
            if c_right < b:
                right = abs(c_right - b)
            if c_left > a:
                left = abs(c_left - a)
        elif c <= a and c_right < a:
            right =  abs(a-b)
        elif c <= a and c_right >=a and c_right <= b:
            right = abs(c_right - b)
        elif c >= b and c_left > b:
            left =  abs(a - b) 
        elif c >=b and c_left <= b and c_left >= a:
            left = abs(a - c_left)
        else:
            pass
        time = left + right
        print(time)
        count += 1

main()
