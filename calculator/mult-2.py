def mult(num1, num2): 
    len1 = len(num1) 
    len2 = len(num2)
    cache={0:["0"] * len2} 
    if len1 == 0 or len2 == 0: return "0"
    result = ["0"] * (len1 + len2) 
    i_n1 = 0
    i_n2 = 0
    print([1,1]+[2,2])
    for i in range(len1 - 1, -1, -1): 
        carry = 0
        n1 = int(num1[i])

        i_n2 = 0
        cache_result = cache.get(n1,"0")
        if cache_result!="0":
            print(n1,"geba")
            result[i_n1 + i_n2:len2] = cache_result
            i_n1+=1
            continue
        for j in range(len2 - 1, -1, -1): 
            
            n2 = int(num2[j])
            summ = n1 * n2 + int(result[i_n1 + i_n2]) + carry 
  
            carry = summ // 10
  
            result[i_n1 + i_n2] = str(summ % 10)
            i_n2 += 1
        cache[n1]=result[i_n1:i_n1+i_n2]
        if (carry > 0): 
            result[i_n1 + i_n2] =  str(int(result[i_n1 + i_n2]) + carry) 
        i_n1 += 1
          
        print(result) 
  
    while len(result)>1 and  result[-1] == "0": 
        result=result[:-1]
    i = len(result) - 1
    s = "" 
    while (i >= 0): 
        s += str(result[i]) 
        i -= 1
    return s
  
# Driver code 
# str1 = "1235421415454545454545454544"
# str2 = "1714546546546545454544548544544545"
  
# if((str1[0] == '-' or str2[0] == '-') and 
#    (str1[0] != '-' or str2[0] != '-')): 
#     print("-", end = '') 
  
  
# if(str1[0] == '-' and str2[0] != '-'): 
#     str1 = str1[1:] 
# elif(str1[0] != '-' and str2[0] == '-'): 
#     str2 = str2[1:] 
# elif(str1[0] == '-' and str2[0] == '-'): 
#     str1 = str1[1:] 
#     str2 = str2[1:] 
# print(multiply(str1, str2)) 
  
# This code is contributed by ankush_953
# number ="1" + str("0"*1000000)
# print("mult started")
# file = open("mult.txt","w")
# file.write(multiply(number,number))
# file.close()

print(mult("333","333"))