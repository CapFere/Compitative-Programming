
def add(firstNumber,secondNumber):
    overflow = 0
    sum=""
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
    while sum[0] == "0" and sum !="0":
        sum = sum[1:]
    return sum
def sub(firstNumber,secondNumber):
    count =0
    sum=""
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
    while sum[0] == "0" and sum !="0":
        sum = sum[1:]
    return sum
def div(firstNumber,secondNumber):
    firstNumber,secondNumber = str(firstNumber),str(secondNumber)
    len_second = len(secondNumber)
    quetiont=""
    previousCut = 0
    first_cut = ""
    isNegative = False
    #check if both the number are negative
    if firstNumber.find("-")!=-1 and secondNumber.find("-")!=-1:
        isNegative= False
        firstNumber=firstNumber[1:]
        secondNumber = secondNumber[1:]
    else:
        #check if the first number is negative
        if firstNumber.find("-")!=-1:
            firstNumber=firstNumber[1:]
            isNegative=True
        #check if the second number is negative
        if secondNumber.find("-")!=-1:
            secondNumber = secondNumber[1:]
            isNegative=True
    while previousCut<len(firstNumber):
        first_cut = first_cut + firstNumber[previousCut:previousCut+1]
        while first_cut[0] == "0" and first_cut !="0":
            if first_cut[1]!="0": quetiont= quetiont + "0"
            first_cut = first_cut[1:]
        len_first_cut = len(first_cut)
        if len_first_cut>len_second or (len_first_cut==len_second and first_cut>=secondNumber):
            sub_quetiont = 1
            sub_second = secondNumber
            len_sub_second = len(secondNumber)
            while len_sub_second<len_first_cut or (len_sub_second==len_first_cut and sub_second<first_cut):
                temp = add(sub_second,secondNumber)
                if len(temp)>len_first_cut or (len(temp)==len_first_cut and temp>first_cut):
                    break
                sub_quetiont = sub_quetiont + 1
                sub_second = temp
            quetiont = quetiont + str(sub_quetiont)
            first_cut = sub(first_cut,sub_second)
            if first_cut=="0":
                isAll=True
                for zero in firstNumber[previousCut+1:]:
                    if zero !="0":isAll=False
                if isAll:
                    quetiont = quetiont + firstNumber[previousCut+1:]
                    break
            
        else:
            previousCut=previousCut + 1            
            continue
        previousCut=previousCut + 1
    if first_cut!="0":
        quetiont = quetiont + "." if quetiont!="" else "0."
        previousCut=0
        while len(quetiont[quetiont.find(".")+1:])<3:
            first_cut = first_cut + "0"
            len_first_cut = len(first_cut)
            if len_first_cut>len_second or (len_first_cut==len_second and first_cut>secondNumber):
                sub_quetiont = 1
                sub_second = secondNumber
                len_sub_second = len(secondNumber)
                while len_sub_second<len_first_cut or (len_sub_second==len_first_cut and sub_second<first_cut):
                    temp = add(sub_second,secondNumber)
                    if len(temp)>len_first_cut or (len(temp)==len_first_cut and temp>first_cut):
                        break
                    sub_quetiont = sub_quetiont + 1
                    sub_second = temp
                quetiont = quetiont + str(sub_quetiont)
                first_cut = sub(first_cut,sub_second)
                if first_cut=="0":
                    isAll=True
                    for zero in first_cut[previousCut+1:]:
                        if zero !="0":isAll=False
                    if isAll:
                        quetiont = quetiont + first_cut[previousCut+1:]
                        break
                
            else:
                previousCut=previousCut + 1            
                continue
            previousCut=previousCut + 1
    #remove negative sign if the result is zero
    if isNegative and quetiont!="0": quetiont = "-" + quetiont
    return quetiont  

