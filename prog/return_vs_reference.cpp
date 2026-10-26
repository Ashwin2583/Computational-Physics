#include <iostream>
#include <string>
#include <cstring>
#include <tuple>

// 1. Struct Definition
typedef struct {
    char str_val[100];
    double dbl_val1;
    double dbl_val2;
    int int_val1;
    int int_val2;
    int int_val3;
} DataContainer;


// =======================================================
// EXERCISE 1: STRUCT IMPLEMENTATION
// =======================================================

// Construct Struct and Return BY VALUE
DataContainer createContainerByValue(const char *str, double d1, double d2, int i1, int i2, int i3) {
    DataContainer data;
    
    // Copy the string into the array field
    strcpy(data.str_val, str);
    
    data.dbl_val1 = d1;
    data.dbl_val2 = d2;
    data.int_val1 = i1;
    data.int_val2 = i2;
    data.int_val3 = i3;
    
    return data;
}

DataContainer globalStructData;

// Construct Struct and Return BY REFERENCE
const DataContainer& createContainerByRef(const char *str, double d1, double d2, int i1, int i2, int i3) {
    strcpy(globalStructData.str_val, str);
    globalStructData.dbl_val1 = d1;
    globalStructData.dbl_val2 = d2;
    globalStructData.int_val1 = i1;
    globalStructData.int_val2 = i2;
    globalStructData.int_val3 = i3;
    
    return globalStructData;
}


// =======================================================
// EXERCISE 2: TUPLE IMPLEMENTATION
// =======================================================

// Alias matching the tuple signature: <std::string, double, double, int, int, int>
using DataTuple = std::tuple<std::string, double, double, int, int, int>;

// Construct Tuple and Return BY VALUE
DataTuple createTupleByValue(const std::string &str, double d1, double d2, int i1, int i2, int i3) {
    return std::make_tuple(str, d1, d2, i1, i2, i3);
}

// Global instance to allow safe reference returning
DataTuple globalTupleData;

// Construct Tuple and Return BY REFERENCE
const DataTuple& createTupleByRef(const std::string &str, double d1, double d2, int i1, int i2, int i3) {
    globalTupleData = std::make_tuple(str, d1, d2, i1, i2, i3);
    return globalTupleData;
}

int main() {
    // --- Accessing Struct Members ---
    std::cout << "--- 1. STRUCT ACCESS ---" << std::endl;

    // By Value
    DataContainer sVal = createContainerByValue("Sample Struct Value", 3.14, 2.71, 10, 20, 30);
    std::cout << "[Value] string: " << sVal.str_val << "\n";
    std::cout << "[Value] doubles: " << sVal.dbl_val1 << ", " << sVal.dbl_val2 << "\n";
    std::cout << "[Value] ints: " << sVal.int_val1 << ", " << sVal.int_val2 << ", " << sVal.int_val3 << "\n\n";

    // By Reference
    const DataContainer& sRef = createContainerByRef("Sample Struct Reference", 1.41, 1.73, 1, 2, 3);
    std::cout << "[Reference] string: " << sRef.str_val << "\n";
    std::cout << "[Reference] doubles: " << sRef.dbl_val1 << ", " << sRef.dbl_val2 << "\n";
    std::cout << "[Reference] ints: " << sRef.int_val1 << ", " << sRef.int_val2 << ", " << sRef.int_val3 << "\n\n";


    // --- Accessing Tuple Elements ---
    std::cout << "--- 2. TUPLE ACCESS ---" << std::endl;

    // By Value using std::get<N>()
    DataTuple tVal = createTupleByValue("Sample Tuple Value", 9.81, 6.02, 100, 200, 300);
    std::cout << "[Value] string: " << std::get<0>(tVal) << "\n";
    std::cout << "[Value] doubles: " << std::get<1>(tVal) << ", " << std::get<2>(tVal) << "\n";
    std::cout << "[Value] ints: " << std::get<3>(tVal) << ", " << std::get<4>(tVal) << ", " << std::get<5>(tVal) << "\n\n";

    // By Reference using Structured Binding
    const DataTuple& tRef = createTupleByRef("Sample Tuple Reference", 8.84, 1.61, 7, 8, 9);
    auto [str, d1, d2, i1, i2, i3] = tRef;
    std::cout << "[Reference] string: " << str << "\n";
    std::cout << "[Reference] doubles: " << d1 << ", " << d2 << "\n";
    std::cout << "[Reference] ints: " << i1 << ", " << i2 << ", " << i3 << std::endl;

    return 0;
}