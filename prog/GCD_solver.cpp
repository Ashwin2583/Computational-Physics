#include <iostream>
using namespace std;

//Euclidean ALgorithm
//Unsigned variables a and b
unsigned int gcd(unsigned int a, unsigned int b){
    if (a == 0)
        return b;
    return gcd(b % a, a);
}
int main(){
    unsigned int a,b;

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