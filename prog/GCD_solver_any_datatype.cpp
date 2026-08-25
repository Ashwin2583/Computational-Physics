#include <iostream>
using namespace std;

//Euclidean Algorithm
template <class T>
T gcd(T a, T b){
    if (a == 0)
        return b; //After one a becomes 0, b is the GCD(a,b)
    return gcd(static_cast<T>(b % a ), a);
}

int main() {
    //Works for unsigned short
    unsigned short s1 = 4,s2=6;
    std:: cout << "GCD for unsigned short values of "<< s1 << " and " << s2 << ": "<< gcd(s1,s2) << std::endl;

    //Works for unsigned int
    unsigned int i1 = 6, i2=21;
    std:: cout << "GCD for unsigned int values of "<< i1 << " and " << i2 << ": "<< gcd(i1,i2) << std::endl;

    //Works for unsigned long
    unsigned long l1 = 15, l2=20;
    std:: cout << "GCD for unsigned long values of "<< l1 << " and " << l2 << ": "<< gcd(l1,l2) << std::endl;

    return 0;
}