#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

int count_set_bit(int value){

    if (!value)
        return 0;

    int total_set_bits = 0;
    
    while(value>0 || value !=-1) // we check value !=-1 in case of a negative number since MSB is always 1 for negative number
    {
        if (value & 1)
            total_set_bits+=1;

        value >>=1;
    }

    return total_set_bits;
}

int main()
{
    int value = -145128;
    printf("Total set bits for value: %d is %d\n" ,value,count_set_bit(value));
    return 0;
}