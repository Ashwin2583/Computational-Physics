#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

// Custom LCG Random Generator
class CustomLCG {
private:
    unsigned long long seed;
    const unsigned long long a = 1664525;
    const unsigned long long c = 1013904223;
    const unsigned long long m = 4294967296;

public:
    CustomLCG(unsigned long long init_seed = 123456789) : seed(init_seed) {}

    // Generates uniform random double in (0, 1] to avoid log(0)
    double getRandom() {
        seed = (a * seed + c) % m;
        double u = static_cast<double>(seed) / static_cast<double>(m);
        return (u == 0.0) ? 1e-10 : u; // Protection against log(0)
    }
};

int main() {
    CustomLCG rng(12345);
    const int NUM_SAMPLES = 100000;
    const double lambda = 5.0;

    std::vector<double> samples;
    samples.reserve(NUM_SAMPLES);

    double sum = 0.0;
    double sum_sq = 0.0;

    // Inverse Transform Sampling
    for (int i = 0; i < NUM_SAMPLES; ++i) {
        double u = rng.getRandom();
        double x = - (1.0 / lambda) * std::log(u); // x = -1/5 * ln(u)
        
        samples.push_back(x);
        sum += x;
        sum_sq += x * x;
    }

    double mean = sum / NUM_SAMPLES;
    double variance = (sum_sq / NUM_SAMPLES) - (mean * mean);

    std::cout << "=== EXPONENTIAL DISTRIBUTION GENERATION [f(x) ~ exp(-5x)] ===\n";
    std::cout << "Total Samples Generated: " << NUM_SAMPLES << "\n\n";

    // Binning analysis
    const int NUM_BINS = 8;
    const double bin_width = 0.2;
    std::vector<int> bin_counts(NUM_BINS, 0);

    for (double x : samples) {
        int bin = static_cast<int>(x / bin_width);
        if (bin >= 0 && bin < NUM_BINS) {
            bin_counts[bin]++;
        }
    }

    std::cout << "x Interval\tSimulated Count\tSimulated Density\tTheoretical Density\n";
    std::cout << "-------------------------------------------------------------------------\n";
    for (int i = 0; i < NUM_BINS; ++i) {
        double x_start = i * bin_width;
        double x_end = (i + 1) * bin_width;
        double x_mid = (x_start + x_end) / 2.0;

        double sim_density = (static_cast<double>(bin_counts[i]) / NUM_SAMPLES) / bin_width;
        double theo_density = lambda * std::exp(-lambda * x_mid);

        std::cout << "[" << std::fixed << std::setprecision(1) << x_start << " - " << x_end << ")\t"
                  << bin_counts[i] << "\t\t"
                  << std::setprecision(4) << sim_density << "\t\t\t" << theo_density << "\n";
    }

    std::cout << "-------------------------------------------------------------------------\n";
    std::cout << "Sample Mean    : " << std::setprecision(5) << mean << " (Theoretical = 1/lambda = 0.20000)\n";
    std::cout << "Sample Variance: " << std::setprecision(5) << variance << " (Theoretical = 1/lambda^2 = 0.04000)\n";

    return 0;
}