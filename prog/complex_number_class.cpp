#include <iostream>
#include <cmath>

using namespace std;

class Complex {
    private:
        //initialising the real and imaginary part
        double real;
        double imag;
    
    public:
        //Default constructor (0+0i)
        Complex() {
            real = 0.0;
            imag = 0.0;
        }

        //Constructor with arguments
        Complex(double r, double i) {
            real = r;
            imag = i;
        }

        //To get the real and imaginary values
        double getReal() const {
            return real;
        }
        double getImag() const {
            return imag;
        }

        //To set the real and imaginary values
        void setImag(double i) {
            imag = i;
        }
        void setReal(double r) {
            real = r;
        }

        //Defining the operation for complex numbers class
        Complex operator+(const Complex& other) const {
            return Complex(real + other.real, imag + other.imag); //sum of real and sum of Imag
        }
        Complex operator-(const Complex& other) const {
            return Complex(real - other.real, imag - other.imag); //Difference of real and Imag respectively
        }
        Complex operator*(const Complex& other) const {
            return Complex((real*other.real - imag*other.imag), (real*other.imag + imag*other.real)); //(ac-bd) + i(ad+bc)
        }

        //To display the complex values
        void print() const{
            if (imag >= 0){
                cout << real << " + " << imag << "i" << endl;
            }
            else{
                cout << real << " - " << abs(imag) << "i" << endl;
            }
        }
};

int main() {
    //defining two complex number using class
    Complex c1(3.0, 4.0); //3+4i
    Complex c2(1.0,2.0); ///1+2i

    //doing the addition, subtraction and multiplication of c1 and c2
    Complex sum = c1 + c2;
    Complex diff = c1 - c2;
    Complex mult = c1 * c2;

    //Displaying the values of the above varibles
    cout << "c1: "; c1.print(); 
    cout << "c2: "; c2.print();
    cout << "------------------------" << endl;
    cout << "Addition: "; sum.print();
    cout << "Difference: "; diff.print();
    cout << "Multiplication: "; mult.print();

    return 0;
}