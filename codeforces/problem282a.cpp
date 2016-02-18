#include <iostream>
#include <string>
using namespace std;

int main()
{
	char m = '-';
	char p = '+';
	int n, val=0;
	cin >> n;
	string mystr;
	while(n--){
		cin >> mystr;
		if (mystr[1] == p)
		    val++;
		else
		    val--;    
		
	}
    
    cout << val;

    return 0;
}
