#include <iostream>
using namespace std;
// ch1.2: c++ class
class C{
public:
	C(char *s="", int i=0, double d=1){
		strcpy(dataMember1, s);
		dataMember2 = i;
		dataMember3 = d;
	}
	
	void memberFunction1(){
		cout << dataMember1 << ' ' << dataMember2 <<' ' << dataMember3 << endl;
	} 	

	void memberFunction2(int i, char *s ="unknown"){
		dataMember2=i;
		cout << i << " received from " << s << endl;
	}

protected:
	char dataMember1[20];
	int dataMember2;
	double dataMember3;
};
// template
template<class T, int size=50>
class genClass{
	T arr[size];
};

template<class T>
void swap1(T& el1, T& el2){
	el1 = el1 + el2;
	el2 = el1 - el2;
	el1 = el1 - el2; 
}

int main(){
	C object1("object1", 100, 2000), object2("object2"), object3;
	object1.memberFunction1();
	object2.memberFunction1();
	object3.memberFunction2(1);

	genClass<int, 100> intObj;

	int el1 = 1, el2 = 2;
	cout << el1 << ',' << el2 << endl;
	swap1(el1, el2);
	cout << el1 << ',' << el2 << endl;
}