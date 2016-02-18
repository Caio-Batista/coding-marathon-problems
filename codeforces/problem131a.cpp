#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	string line;
	cin >> line;
	bool flag1 = false, flag2 = true;
	if(islower(line[0])){
	    flag1 = true;
	    flag2 = false;	
	}
	
	for (int i = 1; i < line.size(); i++){
	    if(islower(line[i])){
	        flag1 = false;
	        flag2 = false;
	    }    	
	}
	
	if(flag1){
		std::transform(line.begin(), line.end(), line.begin(), ::tolower);
		line[0] = toupper(line[0]);
	}
	if(flag2){
	    std::transform(line.begin(), line.end(), line.begin(), ::tolower);
	}
	
	cout << line;
    return 0;
}
