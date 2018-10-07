#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <algorithm>

using namespace std;

int main (int argc, char *argv[])
{

	string amountOfLetters = argv[2];
	string letter = argv[1];

	if((strspn(argv[1], "abcdefghijklmnopqrstuwxyzåäö") == strlen(argv[1])) && (strspn(argv[2], "01234556789") == strlen(argv[2]))) {
		ifstream file;
		file.open ("cities.txt");
		string line;
		while(getline(file, line)) {
			int j = 0;
			transform(line.begin(), line.end(), line.begin(), ::tolower);
			
			for (int i = 0; i < line.size(); i++) {
				if(line[i] == letter[0]) {
					++j;
				}
			}
			string count = to_string(j);
			if((amountOfLetters.compare(count)) == 0){
				cout << line << "\n";
			}
		}
		file.close();			
	}
	else {
		cout << "Usage\nFirst argument - The letter you're looking for \nSecond argument - The amount of letters\n";
		return 0;
	}
	return 0;
}
