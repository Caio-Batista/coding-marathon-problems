#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int main()
{
    int n, num = 0, inc, dec, maior = 0;	
	cin >> n;
	cin.ignore();
	string line;
	int r;
	while( n--){
		vector<int> array;
        getline(cin,line);
        stringstream ss(line);
        while (ss >> r){
           array.push_back(r);
        }   
        dec = array[0];
        //cout << dec << "\n";
        inc = array[1];
        //cout << inc << "\n";
        num -= dec;
        num += inc;
        if(num > maior){
           maior = num;    
        }            
	}
	cout << maior;

    return 0;	
	
}
