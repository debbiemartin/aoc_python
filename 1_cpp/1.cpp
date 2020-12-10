#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int
str_to_int (string numstr) 
{
    int            x;
    stringstream   ss(numstr); 
   
    ss >> x; 
  
    return x; 
}

vector<int>
read_from_file (int *len) 
{
    ifstream     myfile("aoc/inputs/1.txt", ios::in);
    string       line;
    vector<int>  numlist;
    int          num;
    int          len_int = 0;
   
    while(myfile.is_open() && myfile >> line) {
        numlist.push_back(str_to_int(line));
        len_int++;
    }
    
    *len = len_int;
    myfile.close();
    
    return numlist;
}


int 
main () 
{
    vector<int> numlist;
    int         len, i, j, k;
    
    numlist = read_from_file(&len);
    
    /*
     * Iterate pairwise until we find the 
     */   
    for (i = 0; i < len; i++) {
        for (j = 0; j < i; j++) {
            if (numlist[i] + numlist[j] == 2020) {
                cout << "Part 1: " << numlist[i] * numlist[j] << "\n";
            }
            for (k = 0; k < j; k++) {
                if (numlist[i] + numlist[j] + numlist[k] == 2020) {
                    cout << "Part 2: " << numlist[i] * numlist[j] * numlist[k] << "\n";
                } 
            }
        }
    }
}