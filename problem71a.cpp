#include <iostream>
#include <string>
#include <boost>

using namespace std;

int main()
{
	string strfinal;
	int q;
	cin >> q;
	while(true){
		string palavra;
	    getline(cin, palavra);
	    string f,l,aux;
	    string num; 
	    num = boost::lexical_cast<string>(palavra.length() - 2);
	    
	    if(palavra.length() < 11){
		    strfinal.append(palavra);
		}else{
		    f = palavra[0];
		    l = palavra[palavra.length() - 1];
		    aux.append(f);
		    aux.append(num);
		    aux.append(l);
		    
		}
	}
	
    /*cout << "Hello World!";*/
    return 0;
}
