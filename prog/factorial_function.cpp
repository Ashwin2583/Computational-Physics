#include <iostream>
using namespace std;

//factorial function
long long factorial(int n){
    if(n<=1)
        return 1;
    return n*factorial(n-1); //Recursion 
}

int main(){
    int input, fact;
    
    //Input
    std :: cout << "Enter the number: ";
    std :: cin >> input;
    
    //Output
    std :: cout << "Factorial is: "<< factorial(input);
    return 0;
}