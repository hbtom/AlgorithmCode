#include<iostream>
using namespace std;

// search x in a within range [left, right], return the index
int BS1(int a[], int x, int left, int right){
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

int BS2(int a[], int x, int left, int right){
	while(left <= right){
		int mid = left + (right-left)/2;
		if(a[mid] < x){
			left = mid+1;}
		else if(a[mid]>x){
			right = mid -1;}
		else
			return mid;
	}
	return -1;
}

int main(){
	int a[]={1,2,3,4,5,6,7};
	int x = 7;
	int start = 0;
	int end = 6;
	cout << BS1(a, x,start, end) << endl;
	cout << BS2(a, x,start, end) << endl;
	return 1;
}