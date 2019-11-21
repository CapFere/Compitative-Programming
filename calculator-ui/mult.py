'''
    This function adds the single operations for the multiplication
    Arguments 
        firstNumber: previous multiplication result
        secondNumber: current multiplication result
        index: where to start adding the two numbers

    returns
        sum of the two number base on the index
'''
def add(firstNumber,secondNumber,index):

    #set the sum to index value of the firstnumber to the end
    sum = firstNumber[index+1:]
    firstNumber=firstNumber[:index+1]
    overflow = 0

    #check which of the two number is greater
    if(len(firstNumber)<len(secondNumber)):
        firstNumber,secondNumber = secondNumber,firstNumber
    count =0

    #set a variable to find elements in the second number
    second=len(secondNumber) - 1
    for digit in range(len(firstNumber)-1,-1,-1):
        subtotal = 0

        #check wheather the second number is ended or not
        if(count<len(secondNumber)):
            subtotal = int(firstNumber[digit]) + int(secondNumber[second]) + overflow
            overflow = subtotal//10 #result of the integer divison is overflow or carry
            subtotal = subtotal % 10 #the reminder is the subtotal
            sum = str(subtotal) + sum
            second = second - 1
        else:
            subtotal = int(firstNumber[digit])  + overflow
            overflow = subtotal//10
            subtotal = subtotal % 10
            sum = str(subtotal) + sum
        count=count + 1
    sum = str(overflow) + sum

    #return the sum value
    return sum

def mult(firstNumber,secondNumber):
    firstNumber,secondNumber = str(firstNumber),str(secondNumber)
    product = ""
    index = 1
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
    #multiplication starts here
    for firstDigit in range(len(firstNumber)-1,-1,-1):
        oveflow = 0
        subProduct = 0
        currentProduct = ""
        for secondDigit in range(len(secondNumber)-1,-1,-1):
            #find the single line product as we did in elementary class
            singleProuct = int(firstNumber[firstDigit]) * int(secondNumber[secondDigit]) + oveflow
            if secondDigit != 0: 
                oveflow = singleProuct // 10
                singleProuct = singleProuct % 10
            currentProduct = str(singleProuct) + currentProduct
        #if this is not the first time do the addtion
        if product!="":
            product = add(product,currentProduct,len(product)-index)
        #if its the first time set the product to the current value
        else:
            product = currentProduct
        index = index + 1
    #remove preceding zeros
    while len(product)>1 and product[0] == "0":
        product = product[1:]
    #remove negative sign if the result is zero
    if isNegative and product!="0": product = "-" + product

    #print the result
    return product
            