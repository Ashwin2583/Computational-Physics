#include <iostream>
#include <string>
using namespace std;

//Uppercasing function
string toUppercase(string str){
    for (int i=0; i < str.length(); i++){
        if (str[i] >= 'a' && str[i] <= 'z') {
            str[i] = str[i] - 32; //subtraction of 32 of the ASCII of the string values
        }
    }
    return str;
}

int main(){
    
    //Lower case words
    string test1 = "hello world";
    string test2 = "computer programming lab";

    //Display of the original and modified
    cout << "Test 1 Original: " << test1 << endl;
    cout << "Test 1 Modified: " << toUppercase(test1) << endl;

    cout << "Test 2 Original: " << test2 << endl;
    cout << "Test 2 Modified: " << toUppercase(test2) << endl;

    return 0;
}

