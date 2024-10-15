#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

void find_the_power(double base, double exponent)
{
    double power=1.0;
    if (exponent < 0)
    {
        /*
            If we have 2^-3
            it equates (1/ (2^3)) = (1/8)
        */
        base = 1/base;  
        exponent = -exponent;
    }

    for (int i=0; i < exponent; i++)
    {
        power *= base;
    }

    printf("exponent %.4f\n",power);
    return;
}

int main()
{

    double base = -2.5,exponent = -4;

    find_the_power(base,exponent);
    return 0;
}