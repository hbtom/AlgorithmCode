#include <iostream>
using namespace std;

class myvector{
private:
	int vsize;		// vector size
	int maxsize;	// maximum memory
	int *array;		// using array to generate vector
	void alloc_new();
public:
	// (1)constructor and deconstructor
	myvector();		// constructor with default
	myvector(int);	// constructor with maxsize as input
	myvector(const myvector&);	// copy construtor
	~myvector();	// deconstructor
	
	// (2)function
	void push_back(int);	// add element
	void display();
	int size();				// get the size of the vector
	int at(int);			// get an entry

	
	// (3)overload
	int &operator[](int);			// get an entry, & in the front allows assigning value to the selected entry
	myvector& operator+=(int);		// add element to the vector
	myvector& operator=(const myvector&);
};
// (0)
void myvector::alloc_new(){
	maxsize = vsize*2;
	int *tmp = new int[maxsize];
	for(int i=0; i<vsize;i++)
		tmp[i]=array[i];
	delete [] array;
	array = tmp;
}

// (1)
myvector::myvector(){
	maxsize=20;
	array=new int[maxsize];
	vsize=0;
}
myvector::myvector(int i){
	maxsize=i;
	array=new int[maxsize];
	vsize=0;
}
myvector::myvector(const myvector &v){
	maxsize = v.maxsize;
	vsize = v.vsize;
	array = new int[maxsize];
	for(int i=0; i<v.vsize; i++)
		array[i]=v.array[i];
}
myvector::~myvector(){
	delete[] array;
}

// (2)
void myvector::push_back(int i){
	if(vsize+1>maxsize)
		alloc_new();
	array[vsize]=i;
	vsize++;
}
void myvector::display(){
	for(int i=0; i< vsize; i++)
		cout << array[i] << ',';
	cout << endl;
}
int myvector::size(){
	return vsize;
}
int myvector::at(int i){
	if(i<vsize)
		return array[i];
	throw 10;
}

//(3)
int &myvector::operator[](int i){
	return array[i];
}
myvector& myvector::operator+=(int i){
	this->push_back(i);
	return *this;
}
myvector& myvector::operator=(const myvector& v){
	if(this != &v){
		maxsize = v.maxsize;	// copy parameter
		vsize = v.vsize;		// copy parameter
		delete [] array;		// remove and copy array
		array = new int[maxsize];
		for(int i=0; i< v.vsize; i++)
			array[i]=v.array[i];
	}
	return *this;
}

int main(){
	myvector vec20;
	myvector vec2(2);
	
	vec20.push_back(1);vec20.push_back(2);vec20.push_back(3);
	vec20.display();

	myvector vecC(vec20);
	vecC.push_back(5); 
	vecC[0]=10;
	vecC.display();
	
	myvector vecE=vecC;
	vecE.display();
	vecE+=(10);
	vecE.display();
}









