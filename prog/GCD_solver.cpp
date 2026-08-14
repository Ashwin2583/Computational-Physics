#include <iostream>
using namespace std;

//GCD Function
int gcd(int a, int b){
    if(a==0 || b ==0) //Checking for the zero inputs
        return max(a,b);

    //Minimum factor algorithm
    int result = min(a,b); //Extract minimum values
    while (result>0){
        if (a % result == 0 && b % result == 0){
            break;
        }
        result--;
    }
    return result;
}

int main(){
    int a,b;

    //The input
    std::cout << "Enter number a: ";
    std::cin >> a;
    std::cout << "Enter number b: ";
    std::cin >> b;

    //The ouput
    std::cout <<"The GCD of "<< a << " and " << b << " is: ";
    std::cout << gcd(a,b);

    return 0;
}