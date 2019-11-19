#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
    int input = 1;
    while (input != 0)
    {
        printf("Number of astrik: ");
        scanf("%d", &input);
        for (int i = 0; i < input; i++)
        {
            for (int j = 0; j <= i; j++)
            {
                printf("*");
            }
            printf("\n");
        }
    }
}