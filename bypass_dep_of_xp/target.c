#include<stdio.h>
/*
main is 40143d
CalcAverage is 401334
printf is 401cec
buffer is : 22eaf0
2000
*/
void CalcAverage(int str)
{
    char buffer[1024];
    int size=0x12345678;
    FILE* F;
    F = fopen("hack_toy.txt", "rb");
    fseek(F, 0, SEEK_END);
    size = ftell(F);
    fseek(F, 0, SEEK_SET);
    printf("%d\n",size);
    printf("%x\n",buffer);
    fread(buffer, 1, size, F);
    int j=1;
    //printf("%s\n",buffer);
}

int main(int argc, char* argv[])
{
    int wastesomestackspace[1024];
    printf("main is %x\n", (int)main);
    printf("CalcAverage is %x\n", (int)CalcAverage);
    printf("printf is %x\n", (int)printf);
    CalcAverage(1);
    return 0;
}
