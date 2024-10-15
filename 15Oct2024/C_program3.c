#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define MAX 32

void reverse_a_bin_number(int number)
{
    uint8_t *bin_data = (uint8_t *)calloc(MAX,sizeof(uint8_t)); // 32 *1 Byte
    uint8_t *reverse_bin_data =   (uint8_t *)calloc(MAX,sizeof(uint8_t)); // 32 *1 Byte

    // assuming this is a 32bit
    for (int i=31; i>=0;i--)
    {
        if (number & (1<<i))
            *(bin_data-i+31) = 1;
        else
            *(bin_data-i+31) = 0;
    }

    printf("Binary of number: %d\n",number);

    for (int i=0;i<32;i++)
    {
        printf("%u ",*(bin_data + i));
    }

    memcpy(reverse_bin_data,bin_data,MAX*sizeof(uint8_t));


    printf("\n\n\nReverse Binary of number: %d\n",number);
    int temp;
    for (int i=0;i<32;i++)
    {   
        temp = *( uint8_t *)(bin_data + i);
        *(reverse_bin_data + i) =  *( uint8_t *)(bin_data + 31-i);
        *(reverse_bin_data + 31-i) = temp;

        // printf("%u ",*(reverse_bin_data + i));
    }

    for (int i=0;i<32;i++)
    {   
        printf("%u ",*(reverse_bin_data + i));
    }

    return;
}

int main()
{
    int number = 181;
    reverse_a_bin_number(number);
}