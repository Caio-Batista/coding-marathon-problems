#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main()
{
	int n, num, array[5] = {0};
	cin >> n;
	cin.ignore();
	
	string line;
	getline(cin, line);
	stringstream ss(line);
	int temp;
	while(ss >> temp)
	{
	     array[temp] += 1;	
	}
	num = array[4] + array[3] + (array[2] / 2);
	array[1] -= array[3];
	if (array[2] % 2 != 0){
		num++;
		array[1] -= 2;
	}
	
	if (array[1] > 0){
	    num += (array[1] + 3) / 4;
	}
	
	cout << num;
	

    return 0;
}
