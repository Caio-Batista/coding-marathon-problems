#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    string a,b;
    cin >> a;
    cin >> b;
    std::transform(a.begin(), a.end(),a.begin(), ::tolower);
    std::transform(b.begin(), b.end(),b.begin(), ::tolower);
    int resp = 0;
    for(int i=0; i < a.size(); i++){
		if ((int)a[i] > (int) b[i]){
		    resp = 1;
		    break;	
		}else if((int)a[i] < (int) b[i]){
		    resp = -1;
		    break;	
		}
		
		
		
	}
    
    cout << resp;




    return 0;
}
