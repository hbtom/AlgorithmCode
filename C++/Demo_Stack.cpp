#include <iostream>
#include <string>
using namespace std;

// using node to generate Stack
struct Node{
	string data;
	Node *next;
};

class Stack{
public:
	// (1) constructor and deconstructor
	Stack();	// constructor
	~Stack();	// deconstructor

	// (2) function
	void push(string);	// add a node
	string pop();		// remove a node and return
	string toString();	// display stack contents
	bool isEmpty();		// check
private:
	Node *top;
};
// (1)
Stack::Stack(){
	top = NULL;
}
Stack::~Stack(){
	while( !isEmpty() )
		pop();
}
// (2)
void Stack::push(string s){
	Node *tp = new Node();
	tp->data = s;
	tp->next = top;
	top = tp;
}
string Stack::pop(){
	if( !isEmpty() ){
		string res = top->data;
		Node *TBD = top;
		top = top->next;
		delete TBD;		// release memory
		return res;
	}
	else{
		cout << "Can not pop empty stack" << endl;
		exit(1);
	}
}
string Stack::toString(){
	string res = "(top->bottom)";
	if(isEmpty())
		res+= "NULL";
	else{
		Node *cur = top;
		while(cur != NULL){
			res += cur->data +"->";
			cur=cur->next;
		}
		res+="(end)";
	}
	return res;
}
bool Stack::isEmpty(){
	return top == NULL;
}

int main(){
	Stack *s = new Stack();
	cout << s->toString() << endl;
	s->push("Hello");
	s->push("world");
	s->push("!");
	cout << s->toString() << endl;
	delete s;
	return 1;
}














