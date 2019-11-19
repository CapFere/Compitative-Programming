#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void printSpace(int row, int column);
void printTriangle(int column);
void main()
{
    int row = 1;
    while (row != 0)
    {
        printf("Number of astrik: ");
        scanf("%d", &row);
        for (int column = 0; column < row; column++)
        {
            printSpace(row, column);
            printTriangle(column);
            printf("\n");
        }
    }
}

void printTriangle(int column)
{
    for (int j = 0; j <= column; j++)
    {

        printf("*");
    }
    for (int l = 0; l < column; l++)
    {
        printf("*");
    }
}

void printSpace(int row, int column)
{
    for (int k = (row - column); k > 0; k--)
    {
        printf(" ");
    }
}