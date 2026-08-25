#include <iostream>

using namespace std;

//Global varibales
int global_a = 10;
double global_b = 3.14;

int main() {
    //Local varibales
    int local_x = 5;
    double local_y = 2.71;

    //Printing values and memory addresses using '&'
    cout << "Global Variables" << endl;
    cout << "Global_a address: " << &global_a << endl;
    cout << "Global_b address: " << &global_b << endl;

    cout << "Local Variables"  << endl;
    cout << "Local_x address: " << &local_x << endl;
    cout << "Local_y address: " << &local_y << endl;

    return 0;
}