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

    double getRandom() {
        seed = (a * seed + c) % m;
        return static_cast<double>(seed) / static_cast<double>(m);
    }
};

// Electron-Positron Pair Structure
struct ParticlePair {
    double E_electron; // Energy of electron in MeV
    double E_positron; // Energy of positron in MeV
    double x_fraction; // Fractional energy x = E_e / E_gamma
};

// Bethe-Heitler distribution f(x) = 1 - (4/3)*x*(1-x)
double betheHeitlerPDF(double x) {
    return 1.0 - (4.0 / 3.0) * x * (1.0 - x);
}

int main() {
    CustomLCG rng(55555);

    const double m_e = 0.511; // Electron rest mass in MeV
    const double E_gamma = 100.0; // Photon Energy in MeV (E_gamma > 2*m_e)
    const int NUM_EVENTS = 100000;

    if (E_gamma < 2 * m_e) {
        std::cerr << "Error: Photon energy below pair production threshold (1.022 MeV)!\n";
        return 1;
    }

    double x_min = m_e / E_gamma;
    double x_max = 1.0 - (m_e / E_gamma);
    double f_max = 1.0; // Maximum value of f(x) on [0, 1]

    std::vector<ParticlePair> generated_pairs;
    generated_pairs.reserve(NUM_EVENTS);

    int trials = 0;

    while (generated_pairs.size() < NUM_EVENTS) {
        trials++;

        // 1. Uniform sample in [x_min, x_max]
        double x_cand = x_min + (x_max - x_min) * rng.getRandom();

        // 2. Uniform sample in [0, f_max]
        double y = f_max * rng.getRandom();

        // 3. Accept/Reject condition
        if (y <= betheHeitlerPDF(x_cand)) {
            double E_e = x_cand * E_gamma;
            double E_p = E_gamma - E_e;
            generated_pairs.push_back({E_e, E_p, x_cand});
        }
    }

    std::cout << "=== PAIR PRODUCTION MONTE CARLO SIMULATION ===\n";
    std::cout << "Photon Energy (E_gamma) : " << E_gamma << " MeV\n";
    std::cout << "Generated Events         : " << NUM_EVENTS << "\n";
    std::cout << "Acceptance Efficiency   : " << (static_cast<double>(NUM_EVENTS) / trials) * 100.0 << "%\n\n";

    // Binning analysis for energy distribution
    const int NUM_BINS = 10;
    std::vector<int> bin_counts(NUM_BINS, 0);

    for (const auto& pair : generated_pairs) {
        int bin = static_cast<int>(pair.x_fraction * NUM_BINS);
        if (bin >= 0 && bin < NUM_BINS) {
            bin_counts[bin]++;
        }
    }

    std::cout << "Energy Fraction (x)\tElectron E Range (MeV)\tSimulated Fraction\n";
    std::cout << "-------------------------------------------------------------------\n";
    for (int i = 0; i < NUM_BINS; ++i) {
        double x_start = i * 0.1;
        double x_end = (i + 1) * 0.1;
        double frac = (static_cast<double>(bin_counts[i]) / NUM_EVENTS) * 100.0;

        std::cout << "[" << std::fixed << std::setprecision(1) << x_start << " - " << x_end << ")\t\t"
                  << std::setprecision(1) << x_start * E_gamma << " - " << x_end * E_gamma << "\t\t"
                  << std::setprecision(2) << frac << "%\n";
    }

    return 0;
}