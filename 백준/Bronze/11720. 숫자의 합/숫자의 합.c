#include <stdio.h>
#include <stdlib.h>

int main(){
    int N;
    scanf("%d", &N);

    char arr[N];
    scanf("%s", arr);

    int answer = 0;
    for (int i=0; i<N; i++){
        answer += arr[i] - '0';
    }

    printf("%d\n", answer);
    return 0;
}