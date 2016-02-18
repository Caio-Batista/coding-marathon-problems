#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
	string name;
	double a,b;
    cin >> name;
    cin >> a;
    cin >> b;
    cout << setprecision(2) << fixed << "TOTAL = R$ " << 
    a + (15.0 * b)/100 << endl;
    
	

	
    return 0;	
	
}
