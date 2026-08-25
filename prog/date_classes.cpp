#include <iostream>
using namespace std;

class Date {
    //variables
    private:
        int day;
        int month;
        int year;
    public:
        //Default constructor
        Date() {
            day = 1;
            month = 1;
            year = 2000;
        }
        //Parameterized constructor
        Date(int m, int d, int y){
            month = m;
            day = d;
            year = y;
        }
        //Date modification
        void setDate(int m, int d, int y){
            month = m;
            day = d;
            year = y;
        }
        //Display of the data MM/DD/YYYY
        void print() const {
            cout << (month<10 ? "0":"") << month << "/" << (day<10 ? "0":"") << day << "/" << year << endl;
        }
};

int main(){
    //Test 1: Default Constructor
    Date d1;
    cout << "1. Default date (d1): ";
    d1.print();

    //Test 2: Testing parameterized Constructor
    Date d2(8, 23, 2026);
    cout << "2. Parameterized date (d2): ";
    d2.print();

    //Test 3: Testing setDate Method
    d1.setDate(12, 25, 2026);
    cout << "Modifying d1 using setDate" << endl;
    cout <<"3. Modified Date (d1): ";
    d1.print();
    
    return 0;

}