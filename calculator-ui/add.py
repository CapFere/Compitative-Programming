
def add(firstNumber,secondNumber):
    firstNumber,secondNumber = str(firstNumber),str(secondNumber)
    overflow = 0
    sum = ""
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
    while sum[0] == "0":
        sum = sum[1:]
    return sum


