#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

class CustomLCG {
private:
    unsigned long long seed;
    const unsigned long long a = 1664525;
    const unsigned long long c = 1013904223;
    const unsigned long long m = 4294967296; // 2^32

public:
    CustomLCG(unsigned long long init_seed = 123456789) : seed(init_seed) {}

    // Generates a uniform random double in [0, 1)
    double getRandom() {
        seed = (a * seed + c) % m;
        return static_cast<double>(seed) / static_cast<double>(m);
    }
};

int main() {
    CustomLCG rng(42); // Initialize with seed
    const int NUM_SAMPLES = 1000000;
    const int NUM_BINS = 10;
    std::vector<int> bin_counts(NUM_BINS, 0);

    double sum = 0.0;
    double sum_sq = 0.0;

    for (int i = 0; i < NUM_SAMPLES; ++i) {
        double u = rng.getRandom();
        sum += u;
        sum_sq += u * u;

        int bin = static_cast<int>(u * NUM_BINS);
        if (bin >= 0 && bin < NUM_BINS) {
            bin_counts[bin]++;
        }
    }

    double mean = sum / NUM_SAMPLES;
    double variance = (sum_sq / NUM_SAMPLES) - (mean * mean);

    std::cout << "=== UNIFORM RANDOM NUMBER GENERATOR DEMONSTRATION ===\n";
    std::cout << "Total Samples Generated: " << NUM_SAMPLES << "\n\n";

    std::cout << "Bin Interval\tFrequency\tPercentage\n";
    std::cout << "-------------------------------------------\n";
    for (int i = 0; i < NUM_BINS; ++i) {
        double bin_start = i * 0.1;
        double bin_end = (i + 1) * 0.1;
        double percentage = (static_cast<double>(bin_counts[i]) / NUM_SAMPLES) * 100.0;
        std::cout << "[" << std::fixed << std::setprecision(1) << bin_start << " - " 
                  << bin_end << ")\t" << bin_counts[i] << "\t\t" 
                  << std::setprecision(2) << percentage << "%\n";
    }

    std::cout << "-------------------------------------------\n";
    std::cout << "Sample Mean     : " << std::setprecision(5) << mean << " (Theoretical = 0.50000)\n";
    std::cout << "Sample Variance : " << std::setprecision(5) << variance << " (Theoretical = 0.08333 [1/12])\n";

    return 0;
}