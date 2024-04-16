#include <stdio.h>

int main(){
    // 피사노 주기 - 피보나치 수를 m으로 나눈 나머지가 주기를 이루는 것

    int fibo [1500000];

    long long int n;
    scanf("%lld", &n);

    fibo[0] = 0;
    fibo[1] = 1;

    for (int i=2; i<1500000; i++)
    {
        fibo[i] = (fibo[i-1]+fibo[i-2]) % 1000000;
    }

    printf("%d\n", fibo[n%1500000]);
    return 0;
}