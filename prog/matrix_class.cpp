#include <iostream>

using namespace std;

class Matrix {
    private:
        int r; //Number of rows
        int c; //Number o columns 
        int* data; // 1D array storing row-major grid
    public:
        //Parametrized Constructor
        Matrix(int rows, int cols) {
            r = rows;
            c = cols;
            data = new int[r * c];
            for (int i = 0; i < r*c; i++) {
                data[i] = 0;
            }
        }
        //Destructor to free the dynamically allocated memory 
        ~Matrix() {
            delete[] data;
        }

        //Copy Constructor 
        Matrix (const Matrix& other) {
            r = other.r;
            c = other.c;
            data = new int[r * c];
            for (int i = 0; i < r * c; i++) {
                data[i] = other.data[i];
            }
        }
        // Overloading operator () for accessing elements
        int& operator()(int row, int col) {
            return data[row * c + col];
        }

        //overloading assignment operator (=)
        Matrix& operator=(const Matrix& other) {
            if (this != &other) {
                delete[] data;
                r = other.r;
                c = other.c;
                data = new int[r * c];
                for (int i = 0; i < r * c; i++) {
                    data[i] = other.data[i];
                }
            }
            return *this;
        }

        // Overloading addition operator (=)
        Matrix& operator+=(const Matrix& other) {
            if (r == other.r && c == other.c) {
                for(int i = 0; i < r*c; i++) {
                    data[i] += other.data[i];
                }
            }
            else {
                cout << "Error: Matrix dimensions do not match for addition!" << endl;
            }
            return *this;
        }

        //Method to fill matrx values row by row from left to right 
        void inputRowBYRow() {
            cout << "Enter " << r * c << " elements (" << r << "x" << c << " matrix, row-by-row):" << endl;
            for (int i = 0; i < r; i++) {
                cout << " Row " << i + 1 << ": ";
                for (int j = 0; j < c; j++) {
                    cin >> data[i * c + j];
                }
            }
        }

        //Friend function to display matrix ouput
        friend ostream& operator << (ostream& os, const Matrix& m) {
            for (int i = 0; i < m.r; i++) {
                os << " | ";
                for (int j = 0; j < m.c; j++) {
                    os << m.data[i * m.c + j] << " ";
                }
                os << "|" << endl;
            }
            return os;
        }
};

int main() {
    //Matrix 2x3 and adding the matrix elements
    Matrix A(2,3);
    A.inputRowBYRow();

    //Accessing and modifying the elemets using operation()
    cout << "\nInitial Matrix A:" << endl << A << endl;
    cout << "Accessing element A(0,1): " << A(0,1) << endl;

    //Setting value using operator ()
    A(0,1) = 99;
    cout << "After Ececuting A(0 ,1) = 99:" << endl << A << endl;

    //Testing Assignment operator (=)
    Matrix B(2, 3);
    B = A; 
    cout << "Matrix B (Assigned from A using '='):" << endl << B << endl;
    
    //Testing Addition Assignment operator (+=)
    Matrix C(2,3);
    cout << "Add values for another matrix C: " << endl;
    C.inputRowBYRow();

    cout << "\nMatrix C: " << endl << C << endl;

    B += C; //Adds C into B

    return 0;
}