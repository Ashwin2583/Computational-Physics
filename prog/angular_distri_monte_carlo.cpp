#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

// Custom LCG Random Generator from Question 1
class CustomLCG {
private:
    unsigned long long seed;
    const unsigned long long a = 1664525;
    const unsigned long long c = 1013904223;
    const unsigned long long m = 4294967296;

public:
    CustomLCG(unsigned long long init_seed = 123456789) : seed(init_seed) {}

    double getRandom() {
        seed = (a * seed + c) % m;
        return static_cast<double>(seed) / static_cast<double>(m);
    }
};

// Target distribution PDF: f(x) = 1 + x^2
double targetPDF(double x) {
    return 1.0 + x * x;
}

int main() {
    CustomLCG rng(987654321);
    const int NUM_ACCEPTED_SAMPLES = 100000;
    const double f_max = 2.0; // Maximum value of f(x) = 1 + x^2 on [-1, 1]

    std::vector<double> accepted_samples;
    accepted_samples.reserve(NUM_ACCEPTED_SAMPLES);

    int total_trials = 0;

    // Acceptance-Rejection Monte Carlo Loop
    while (accepted_samples.size() < NUM_ACCEPTED_SAMPLES) {
        total_trials++;

        // 1. Generate candidate x in [-1, 1]
        double x_cand = -1.0 + 2.0 * rng.getRandom();

        // 2. Generate y in [0, f_max]
        double y = f_max * rng.getRandom();

        // 3. Accept/Reject condition
        if (y <= targetPDF(x_cand)) {
            accepted_samples.push_back(x_cand);
        }
    }

    // Verification: Divide [-1, 1] into 10 bins and compute normalized counts
    const int NUM_BINS = 10;
    std::vector<int> bin_counts(NUM_BINS, 0);

    for (double x : accepted_samples) {
        int bin = static_cast<int>((x + 1.0) / 2.0 * NUM_BINS);
        if (bin >= 0 && bin < NUM_BINS) {
            bin_counts[bin]++;
        }
    }

    std::cout << "=== MONTE CARLO ANGULAR DISTRIBUTION f(cos theta) ~ 1 + cos^2(theta) ===\n";
    std::cout << "Target Accepted Samples: " << NUM_ACCEPTED_SAMPLES << "\n";
    std::cout << "Total Trials Required  : " << total_trials << "\n";
    std::cout << "Acceptance Efficiency  : " << (static_cast<double>(NUM_ACCEPTED_SAMPLES) / total_trials) * 100.0 << "% (Theoretical: 66.67%)\n\n";

    std::cout << "cos(theta) Bin Range\tSimulated Density\tTheoretical Density\n";
    std::cout << "-------------------------------------------------------------------\n";

    // Normalization constant for integral of (1 + x^2) dx from -1 to 1 = 8/3
    double bin_width = 2.0 / NUM_BINS;
    double norm_factor = 3.0 / 8.0; 

    for (int i = 0; i < NUM_BINS; ++i) {
        double bin_center = -1.0 + (i + 0.5) * bin_width;
        double sim_density = (static_cast<double>(bin_counts[i]) / NUM_ACCEPTED_SAMPLES) / bin_width;
        double theo_density = norm_factor * targetPDF(bin_center);

        std::cout << "[" << std::setw(5) << std::fixed << std::setprecision(1) << -1.0 + i * bin_width
                  << " to " << std::setw(4) << -1.0 + (i + 1) * bin_width << ")\t\t"
                  << std::setprecision(4) << sim_density << "\t\t\t" << theo_density << "\n";
    }

    return 0;
}