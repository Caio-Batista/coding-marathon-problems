#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main(){
    string line;
    getline(cin, line);
    stringstream stream(line);
    /*
    std::vector<int> values;
    int n;
    while(stream >> n){
        values.push_back(n);
    }
    */
    
    string str = "102:330:3133:76531:451:000:12:44412";
	for (int i=0; i < line.length(); i++)
	{
		if (line[i] == ':')
			line[i] = ' ';
	}

	vector<int> array;
	stringstream ss(line);
	int temp;
	while (ss >> temp)
		array.push_back(temp);
		
    //cout << values[1] << endl;
    /*  
    int arr[2];
    int i = 0;
    stringstream ssin(line);
    while (ssin.good() && i < 2){
        ssin >> arr[i];
        ++i;
    }
    */
    
    for(int i = 0; i < array.size(); i++){
        cout << array[i] << endl;
    }
}
