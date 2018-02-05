#include<iostream>
using namespace std;

// search x in a within range [left, right], return the index
int BS(int a[], int x, int left, int right){
	while(left < right){
		int mid = left + (right-left)/2;
		if(a[mid] < x){
			left = mid+1;}
		else if(a[mid]>x){
			right = mid -1;}
		else
			return mid;
	}
	return a[left]==x? left : -1;
}

int main(){
	int a[]={1,2,3,4,5,6,7,8,9};
	int x = 5;
	cout << BS(a, x,0, 8) << endl;
	return 1;
}