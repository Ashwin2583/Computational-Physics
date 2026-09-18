#include <iostream>

using namespace std;


// Global Variables (Stored in Data Segment)
int global_var1 = 100;
int global_var2 = 200;
double global_scale = 9.81;

// Helper function to show stack frame allocation
void sampleFunction() {
    int func_local = 42;
    cout << "  Address of func_local (inside sampleFunction): " << &func_local << endl;
}

int main() {
    // Local Variables (Stored on the Stack)
    int local_a = 10;
    int local_b = 20;
    double local_c = 3.14;

    cout << "       MEMORY ADDRESS ANALYSIS IN C++            " << endl;

    // 1. Displaying Addresses of Global Variables
    cout << "--- GLOBAL VARIABLES (Data Segment) ---" << endl;
    cout << "  Address of global_var1  : " << &global_var1 << endl;
    cout << "  Address of global_var2  : " << &global_var2 << endl;
    cout << "  Address of global_scale : " << &global_scale << endl;
    cout << endl;

    // 2. Displaying Addresses of Local Variables
    cout << "--- LOCAL VARIABLES (Stack Memory) ---" << endl;
    cout << "  Address of local_a      : " << &local_a << endl;
    cout << "  Address of local_b      : " << &local_b << endl;
    cout << "  Address of local_c      : " << &local_c << endl;
    sampleFunction();
    cout << endl;

    return 0;
}
