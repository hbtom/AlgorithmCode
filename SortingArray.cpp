#include <iostream>
#include <vector>
using namespace std;

void quick_sort(int *p, int n);
void print_array(int *p, int n);
void merge_sort(int *p, int n);

int main(){
	const int n = 10;
	int a[n]={5,4,3,2,1,6,7,8,9,0};
	print_array(a, n);

	//quick_sort(a,n);
	merge_sort(a, n);
	print_array(a,n);
}
// print array
void print_array(int *p, int n){
	for(int i= 0; i< n; i++)
		cout << p[i] << ',';
	cout << endl;
}

// quick_sort
void quick_sort(int *p, int n){
	if(n<=1) return;
	int left=0, right = n-1;
	while(1){
		// find the location where p[left]> p[right] and swap
		while(p[left] <= p[right] && left < right) right--;
		if(left == right) break;
		else	swap(p[left], p[right]);

		while(p[left] <= p[right] && left < right) left++;
		if(left == right) break;
		else	swap(p[left], p[right]);
	}
	quick_sort(p, left);
	quick_sort(p+left+1, n-left-1);
}

// merge_sort
void merge_sort(int *p, int n){
	if(n<=1) return;
	// recursion
	merge_sort(p, n/2);
	merge_sort(p+int(n/2), n-int(n/2));
	// a copy of the original
	vector<int> tmp(n,0);	
	for(int i=0; i<n; i++)
		tmp[i]=p[i];
	// merge 2 sorted array
	int i=0, s1=0, s2=n/2;
	while(s1<n/2 && s2<n){
		if(tmp[s1]<= tmp[s2])
			p[i++]=tmp[s1++];
		else
			p[i++]=tmp[s2++];
	}
	// the resudual merging
	if(s2==n){
		while(i<n)	p[i++]=tmp[s1++];
	}
	else{
		while(i<n)	p[i++]=tmp[s2++];
	}
}

