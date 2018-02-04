#include <iostream>
using namespace std;
// 									BaseClass 				DerivedClass
// 									private 		  =>    can't be visited
//public inheritance: 				public, protected =>	public, protected
//protected inheritance: 			public, protected => 	protected
//private inheritance: 				public, protected => 	private
//virtual function: 				when there are more than 2 function inherited, some ambiguous problem (multi-copies)


class BaseClass{
public:
	BaseClass(){}
	void f(char *s = "unknown"){
		cout << "Function f() in BaseClass claled from " << s << endl;
		h();
	}
protected:
	void g(char *s = "unknown"){
		cout << "Function g() in BaseClass called from " << s << endl;
	}
private:
	void h(){
		cout << "Function h() in BasedClass\n";
	}
};

class Derived1Level1: public virtual BaseClass{
public:
	void f(char *s = "unknown"){
		cout << "Function f() in Derived1Level1 called from " << s << endl;
		g("Derived1Level1");
		h("Derived1Level1");
	}

	void h(char*s = "unknown"){
		cout << "Function h() in Derived1Level1 called from " << s << endl;
	}
};

class Derived2Level1: public virtual BaseClass{
public:
	void f(char *s = "unknown"){
		cout << "Function f() in Derived2Level1 called from " << s << endl;
		g("Derived2Level1");
		//h();
	}
};

class DerivedLevel2: public Derived1Level1, public Derived2Level1{
public:
	void f(char *s = "unknown"){
		cout << "Function f() in DerivedLevel2 called from " << s << endl;
		g("DerivedLevel2");
		Derived1Level1::h("DerivedLevel2");
		BaseClass::f("DerivedLevel2");
	}
};

int main(){
	BaseClass bc;
	Derived1Level1 d1l1;
	Derived2Level1 d2l1;
	DerivedLevel2 dl2;
	bc.f("main(1)");
	//bc.g(); protected function is not accessible
	//bc.h(); private function is not accessible

	d1l1.f("main(2)");
	//d1l1.g();
	d1l1.h("main(3)");

	d2l1.f("main(4)");
	//d2l1.g();
	//d2l1.h();

	dl2.f("main(5)");
	//dl2.g();
	dl2.h();
}




