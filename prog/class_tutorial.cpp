#include <iostream>
using namespace std;

class Rectangle {
    private:
        double width;
        double height;
    public:
        Rectangle() {
            width = 1;
            height = 1;
        }
        Rectangle(double w, double h) {
            width = w;
            height = h;
        }
        void setWidth(double w){
            width = w;
        }
        void setHeight(double h){
            height = h;
        }
        double getWidth() const{
            return width;
        }
        double getHeight() const{
            return height;
        }
        double area() const{
            return width*height;
        }
        double perimeter() const {
            return 2*(width + height);
        }
        void print() const {
            cout << "Width: " << width
                << ", Height: " << height
                << ", Area: " << area()
                << ", Perimeter: "<< perimeter() << endl;
        }
};

int main() {
    Rectangle r1;
    cout << "Rectangle 1 (Default): "<<endl;
    r1.print();

    cout << endl;

    Rectangle r2(4.5, 2.0);
    cout << "Rectangle 2 (custom): "<<endl;
    r2.print();

}
