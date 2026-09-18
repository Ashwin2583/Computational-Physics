#include <iostream>
using namespace std;

class Rational {
    private:
        int numerator;
        int denominator;
    public:
        Rational() {
            numerator = 0;
            denominator= 1;
        }

        Rational(int p, int q) {
            numerator = p;
            denominator = (q != 0) ? q : 1;
        }

        //Accessors
        int num() const {return numerator; }
        int den() const {return denominator; }

        Rational operator+(const Rational& other) const {
            int num = (numerator * other.denominator) + (denominator * other.numerator);
            int den = denominator * other.denominator;
            return Rational(num, den);
        }
        Rational operator-(const Rational& other) const {
            int num = (numerator * other.denominator) - (denominator * other.numerator);
            int den = denominator * other.denominator;
            return Rational(num, den);
        }
        Rational operator*(const Rational& other) const {
            int num = numerator * other.numerator;
            int den = denominator * other.denominator;
            return Rational(num, den);
        }

        Rational operator/(const Rational& other) const {
            int num = numerator * other.denominator;
            int den = other.numerator * denominator;
            return Rational(num, den);
        }

        friend ostream& operator<<(ostream& os, const Rational& r);
};

ostream& operator<<(ostream& os, const Rational& r) {
    os << r.num() << "/" << r.den();
    return os;
}

int main() {
    Rational r1(1,2);
    Rational r2(3,4);

    Rational sum = r1 + r2;
    Rational diff = r1 - r2;
    Rational prod = r1 * r2;
    Rational quot = r1 / r2;

    cout << "r1 = " << r1 << endl;
    cout << "r2 = " << r2 << endl;

    cout << "Addition (r1 + r2): " << sum << endl;
    cout << "Difference (r1 - r2): " << diff << endl;
    cout << "Product (r1 * r2): " << prod << endl;
    cout << "Division (r1 / r2): " << quot << endl;

    return 0;
}