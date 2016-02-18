#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
using namespace std;

int main()
{
	/*
    int n, num, dec, inc, maior = 0;
    cin >> n;
    cin.ignore();
    int array[2] = {0};
    string line;
    stringstream ss(line);
    int temp;
    while (n--){
         getline(cin, line);
         for(int i=0; i < 2; i++){
			 ss >> temp;
			 array[i] = temp;
	     }
         dec = array[0];
         inc = array[1];
         num -= dec;
         num += inc;
         if(num > maior){
             maior = num;
         }
    
    }
    
    
    cout << maior;
    */
    
    double n;
    cin >> n;
    cout <<  setprecision(4) << fixed <<"A=" << 3.14159 * (n * n) << endl; 
    
    
    
    
    
     
    return 0;
}
