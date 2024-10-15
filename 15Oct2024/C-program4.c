#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

int (*ptr) (int, int);

int add(int,int);
int sub(int,int);
int mul(int,int);

int add(int a ,int b)
{
    return a+b;
}

int sub(int a ,int b)
{
    return a-b;
}

int mul(int a ,int b)
{
    return a*b;
}

int main()
{
    ptr =&add;
    printf("Addition of 10 and 20 :%d\n",ptr(10,20));

    ptr =&sub;
    printf("Subtraction of 10 and 20 :%d\n",ptr(10,20));


    ptr =&mul;
    printf("Multiplication of 10 and 20 :%d\n",ptr(10,20));


    return 0;
}