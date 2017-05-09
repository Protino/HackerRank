#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
int main()
{
char password[10];
printf("Type your password : ");
scanf("%s",password);
for(int i=0;i<=10;i++)
{
	if(!isalpha(password[i])){
		printf("Bad Password");
		i=-1;
		break;
	}
}
if (i==-1){
	printf("Good Password");
}
return 0;
}
