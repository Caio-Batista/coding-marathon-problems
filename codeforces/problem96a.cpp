#include <iostream>
#include <string>
using namespace std;

int main()
{
	string mystr, bla = "0000000";
	cin >> mystr;
	 
    if (mystr.find("0000000") != std::string::npos) {
        std::cout << "YES";
    }else if(mystr.find("1111111") != std::string::npos){	
		std::cout << "YES";
	}else{
	    std::cout << "NO";	
	}    

    return 0;
}
