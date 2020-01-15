def main():
    size=eval(input())
    user_input = input().split()
    prev_count = 1
    current_count = 1
    removed_count = 0
    removed_index = 0
    i = 0
    twice = 0
    start_index = 0 
    cheked = 0
    while i < size-1:
        print(user_input[i])
        print(removed_index,removed_count,current_count,prev_count,i)
        if (i==0 or i != removed_index)  and (int(user_input[i]) < int(user_input[i+1])):
            current_count += 1
        elif i == removed_index and (int(user_input[i-1]) < int(user_input[i])):
            print("geba",int(user_input[i-1]),int(user_input[i]))
            current_count += 1
        
        else:
            if removed_count != 0 and current_count>prev_count:
                prev_count = current_count
                current_count = 1
                if twice != 0:
                    i = start_index
                    twice = 0
                    cheked = 1
                else:
                    i = removed_index - 1
                    start_index = i
                removed_index = 0
                removed_count = 0
            elif removed_count != 0 and current_count<=prev_count:
                current_count = 1
                if twice != 0:
                    i = start_index
                    twice = 0
                    cheked = 1
                else:
                    i = removed_index - 1
                    start_index = i
                removed_count = 0
                removed_index = 0
            else:
                if twice==0 and cheked!=1:
                    removed_index = i + 1
                    removed_count += 1
                    twice += 1
                else:
                    removed_index = i
                    removed_count += 1
        print(removed_index,removed_count,current_count,prev_count,i)
        i+=1
    if current_count > prev_count: prev_count = current_count
    print(prev_count)
        
main()