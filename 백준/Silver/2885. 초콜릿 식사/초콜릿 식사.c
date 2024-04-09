#include <stdio.h>

int main(){
    int k;
    long long choco = 1L;
    int cnt;

    scanf("%d", &k);

    //k보다 큰 2의 N승 수 choco 찾기
    cnt = 1;
    while (k > choco){
        choco = 1<<cnt; //비트연산자 이용
        cnt++;
    }

    printf("%lld ", choco);
    //answer는 2로 나눠가면서 가장 작은 한 덩이 뺐을 때 크기를 만족하는지 검사하기


    int tmp = 0;

    if (choco == k){
        printf("0\n");
    }
    else{
        while(k > 0){
            if (k >= choco){
                k -= choco;
            }
            else {
                choco = choco / 2;
                tmp += 1;
            }
        }
        printf("%d\n", tmp);
    }

}