
def sum(firstNumber,secondNumber):
    firstNumber,secondNumber = str(firstNumber),str(secondNumber)
    isNegative = False
    overflow = 0
    sum = ""
    if(firstNumber.find("-")!=-1 and secondNumber.find("-")!=-1):
        firstNumber= firstNumber[1:]
        secondNumber=secondNumber[1:]
        if(len(firstNumber)>len(secondNumber)):
            count =0
            second=len(secondNumber) - 1
            for digit in range(len(firstNumber)-1,-1,-1):
                subtotal = 0
                if(count<len(secondNumber)):
                    subtotal = int(firstNumber[digit]) + int(secondNumber[second]) + overflow
                    overflow = subtotal//10
                    subtotal = subtotal % 10
                    sum = str(subtotal) + sum
                    second = second - 1
                else:
                    subtotal = int(firstNumber[digit])  + overflow
                    overflow = subtotal//10
                    subtotal = subtotal % 10
                    sum = str(subtotal) + sum
                count=count + 1
            sum = str(overflow) + sum
        else:
            firstNumber,secondNumber = secondNumber,firstNumber
            count =0
            second=len(secondNumber) - 1
            for digit in range(len(firstNumber)-1,-1,-1):
                subtotal = 0
                if(count<len(secondNumber)):
                    subtotal = int(firstNumber[digit]) + int(secondNumber[second]) + overflow
                    overflow = subtotal//10
                    subtotal = subtotal % 10
                    sum = str(subtotal) + sum
                    second = second - 1
                else:
                    subtotal = int(firstNumber[digit])  + overflow
                    overflow = subtotal//10
                    subtotal = subtotal % 10
                    sum = str(subtotal) + sum
                count=count + 1
            sum = str(overflow) + sum
        isNegative= True
    elif(firstNumber.find("-")!=-1):
        firstNumber,secondNumber = secondNumber,firstNumber
        secondNumber = secondNumber[1:]
        print(secondNumber)
        if(len(firstNumber)>len(secondNumber) or (len(firstNumber)==len(secondNumber) and firstNumber>secondNumber)):
            count =0
            second=len(secondNumber) - 1
            for digit in range(len(firstNumber)-1,-1,-1):
                subtotal = 0
                if(count<len(secondNumber)):
                    if(int(firstNumber[digit])<int(secondNumber[second])):
                        temp=""
                        for numb in firstNumber:
                            temp=temp+numb+" "
                        firstNumber = temp.split()
                        for i in range(0,len(firstNumber)):
                            if i == digit:
                                for j in range(digit-1,-1,-1):
                                    if int(firstNumber[j])>0:
                                        firstNumber[digit]=str(int(firstNumber[digit]) + 10 - int(secondNumber[second]))
                                        firstNumber[j] = str(int(firstNumber[j]) - 1)
                                        for k in range(j+1,digit):
                                            firstNumber[k]=str(int(firstNumber[k]) + 9)
                                        break
                                        
                        firstNumber = "".join(firstNumber)
                        subtotal = int(firstNumber[digit])
                        sum = str(subtotal) + sum
                    else:
                        subtotal = int(firstNumber[digit]) - int(secondNumber[second])
                        sum = str(subtotal) + sum
                    second = second - 1
                else:
                    subtotal = int(firstNumber[digit])
                    sum = str(subtotal) + sum
                count=count + 1
        else:
            firstNumber,secondNumber=secondNumber,firstNumber
            count =0
            second=len(secondNumber) - 1
            for digit in range(len(firstNumber)-1,-1,-1):
                subtotal = 0
                if(count<len(secondNumber)):
                    if(int(firstNumber[digit])<int(secondNumber[second])):
                        temp=""
                        for numb in firstNumber:
                            temp=temp+numb+" "
                        firstNumber = temp.split()
                        for i in range(0,len(firstNumber)):
                            if i == digit:
                                for j in range(digit-1,-1,-1):
                                    if int(firstNumber[j])>0:
                                        firstNumber[digit]=str(int(firstNumber[digit]) + 10 - int(secondNumber[second]))
                                        firstNumber[j] = str(int(firstNumber[j]) - 1)
                                        for k in range(j+1,digit):
                                            firstNumber[k]=str(int(firstNumber[k]) + 9)
                                        break
                                        
                        firstNumber = "".join(firstNumber)
                        subtotal = int(firstNumber[digit])
                        sum = str(subtotal) + sum
                    else:
                        subtotal = int(firstNumber[digit]) - int(secondNumber[second])
                        sum = str(subtotal) + sum
                    second = second - 1
                else:
                    subtotal = int(firstNumber[digit])
                    sum = str(subtotal) + sum
                count=count + 1
            isNegative = True
    elif(secondNumber.find("-")!=-1):
        secondNumber = secondNumber[1:]
        if(len(firstNumber)>len(secondNumber) or (len(firstNumber)==len(secondNumber) and firstNumber>secondNumber)) :
            count =0
            second=len(secondNumber) - 1
            for digit in range(len(firstNumber)-1,-1,-1):
                subtotal = 0
                if(count<len(secondNumber)):
                    if(int(firstNumber[digit])<int(secondNumber[second])):
                        temp=""
                        for numb in firstNumber:
                            temp=temp+numb+" "
                        firstNumber = temp.split()
                        for i in range(0,len(firstNumber)):
                            if i == digit:
                                for j in range(digit-1,-1,-1):
                                    if int(firstNumber[j])>0:
                                        firstNumber[digit]=str(int(firstNumber[digit]) + 10 - int(secondNumber[second]))
                                        firstNumber[j] = str(int(firstNumber[j]) - 1)
                                        for k in range(j+1,digit):
                                            firstNumber[k]=str(int(firstNumber[k]) + 9)
                                        break
                                        
                        firstNumber = "".join(firstNumber)
                        subtotal = int(firstNumber[digit])
                        sum = str(subtotal) + sum
                    else:
                        subtotal = int(firstNumber[digit]) - int(secondNumber[second])
                        sum = str(subtotal) + sum
                    second = second - 1
                else:
                    subtotal = int(firstNumber[digit])
                    sum = str(subtotal) + sum
                count=count + 1
        else:
            firstNumber,secondNumber=secondNumber,firstNumber
            count =0
            second=len(secondNumber) - 1
            for digit in range(len(firstNumber)-1,-1,-1):
                subtotal = 0
                if(count<len(secondNumber)):
                    if(int(firstNumber[digit])<int(secondNumber[second])):
                        temp=""
                        for numb in firstNumber:
                            temp=temp+numb+" "
                        firstNumber = temp.split()
                        for i in range(0,len(firstNumber)):
                            if i == digit:
                                for j in range(digit-1,-1,-1):
                                    if int(firstNumber[j])>0:
                                        firstNumber[digit]=str(int(firstNumber[digit]) + 10 - int(secondNumber[second]))
                                        firstNumber[j] = str(int(firstNumber[j]) - 1)
                                        for k in range(j+1,digit):
                                            firstNumber[k]=str(int(firstNumber[k]) + 9)
                                        break
                                        
                        firstNumber = "".join(firstNumber)
                        subtotal = int(firstNumber[digit])
                        sum = str(subtotal) + sum
                    else:
                        subtotal = int(firstNumber[digit]) - int(secondNumber[second])
                        sum = str(subtotal) + sum
                    second = second - 1
                else:
                    subtotal = int(firstNumber[digit])
                    sum = str(subtotal) + sum
                count=count + 1
            isNegative = True
    else:
        if(len(firstNumber)>len(secondNumber)):
            count =0
            second=len(secondNumber) - 1
            for digit in range(len(firstNumber)-1,-1,-1):
                subtotal = 0
                if(count<len(secondNumber)):
                    subtotal = int(firstNumber[digit]) + int(secondNumber[second]) + overflow
                    overflow = subtotal//10
                    subtotal = subtotal % 10
                    sum = str(subtotal) + sum
                    second = second - 1
                else:
                    subtotal = int(firstNumber[digit])  + overflow
                    overflow = subtotal//10
                    subtotal = subtotal % 10
                    sum = str(subtotal) + sum
                count=count + 1
            sum = str(overflow) + sum
        else:
            firstNumber,secondNumber = secondNumber,firstNumber
            count =0
            second=len(secondNumber) - 1
            for digit in range(len(firstNumber)-1,-1,-1):
                subtotal = 0
                if(count<len(secondNumber)):
                    subtotal = int(firstNumber[digit]) + int(secondNumber[second]) + overflow
                    overflow = subtotal//10
                    subtotal = subtotal % 10
                    sum = str(subtotal) + sum
                    second = second - 1
                else:
                    subtotal = int(firstNumber[digit])  + overflow
                    overflow = subtotal//10
                    subtotal = subtotal % 10
                    sum = str(subtotal) + sum
                count=count + 1
            sum = str(overflow) + sum
    while len(sum)>1 and sum[0] == "0":
        sum = sum[1:]
    if(isNegative and sum!="0"): sum = "-" + sum
    return sum
