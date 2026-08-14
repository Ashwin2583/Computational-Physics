#include <stdio.h>
#include <stdint.h>

//To print the binary 32-bit word
void print_binary(uint32_t word)
{
    for (int i = 31; i >= 0; i--){
        printf("%u", (word >> i) & 1);
        if (i % 4 == 0){
            printf(" ");
        }
    }
    printf("\n");
}

int main(void)
{
    //Inputs
    int cellU = 12;
    int cellV = 7;
    int waferU = -15;
    int waferV = 23;
    int layer = 8;
    
    //Display the inputs
    printf("\nInput values:\n");
    printf("CellU = %d\n", cellU);
    printf("CellV = %d\n", cellV);
    printf("WaferU = %d\n", waferU);
    printf("WaferV = %d\n", waferV);
    printf("Layer = %d\n", layer);
    printf("\n");

    //Word storage in 32-bit
    uint32_t word;

    //Offsetting the wafer coordinated to unsigned values
    int waferU_stored = waferU + 40; /*add the maximum values of wafer value to the inputs to remove the neagtive values*/
    int waferV_stored = waferV + 40;

    //Packing 
    word = 0;
    word |= (uint32_t)cellU;
    word |= (uint32_t)cellV << 5;
    word |= (uint32_t)waferU_stored << 10;
    word |= (uint32_t)waferV_stored << 17;
    word |= (uint32_t)layer << 24;

    //Display the output
    printf("Packed word = ");
    print_binary(word);

    //Unpacking
    int cellU_unpacked = word & 0x1F; //Mask is added with the word
    int cellV_unpacked = (word >> 5) & 0x1F; //Mask is added with the word after right shift of 5
    int waferU_unpacked = ((word >> 10) & 0x7F) - 40; //Mask is added with the word after right shift of 10 and offseted back
    int waferV_unpacked = ((word >> 17) & 0x7F) - 40; //Mask is added with the word after right shift of 17 and offseted back
    int layer_unpacked = (word >> 24) & 0x3F; //Mask is added with the word after right shift of 24

    //Display the unpacked values
    printf("\nUnPacked values:\n");
    printf("Cell U = %d\n", cellU_unpacked);
    printf("Cell V = %d\n", cellV_unpacked);
    printf("Wafer U = %d\n", waferU_unpacked);
    printf("Wafer V = %d\n", waferV_unpacked);
    printf("Layer = %d\n", layer_unpacked);

    return 0;
}