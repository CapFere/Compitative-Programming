#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
    long long int firstNumber;
    int secondNumber;
    printf("Enter First Number: ");
    scanf("%lld", firstNumber);
    printf("Enter Second Number: ");
    scanf("%d", secondNumber);
    printf("The sum is %lld\n", firstNumber + secondNumber);
}