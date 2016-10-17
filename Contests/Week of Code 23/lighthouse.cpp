#include <iostream>

int** input(){
	int n = 5;
	int arr[n][n]= {
		{1,1,1,1,1},
		{1,1,1,1,1},
		{1,1,1,1,1},
		{1,1,1,1,1},
		{1,1,1,1,1}};
	
	return &arr;
}

int** computeOnes(int arr[][],int n){
	int score[n][n] = {0};
	for(int i =1;i<n-1;i++){
		for(int j=1;i<n-1;i++){
			if(arr[i][j]==1 && arr[i-1][j]==1 && arr[i+1][j]==1 && arr[i][j-1]==1 && arr[i][j+1]==1){
				score[i][j]+=1;
			}else{
				score[i][j]=0;
			}
		}
	}
}
/*
int computeMaxRadius(int score[][],int n){
}*/


int main(void){
	int [5][5] result =  computeOnes(input(),5);
	
	
}
