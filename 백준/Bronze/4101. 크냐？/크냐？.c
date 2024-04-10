#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int main(){
	int a,b;
	int cnt = 0 ;
	char res[100][4] = {""};
	while(1){
		scanf("%d %d",&a,&b);
		if(a==0 && b==0)
			break;
		else if(a>b)
			strcpy(res[cnt++],"Yes");
		else
			strcpy(res[cnt++],"No");
	}
	for(int i = 0 ; i < cnt ; i++){
		printf("%s\n",res[i]);
	}
}