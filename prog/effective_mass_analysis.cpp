#include <iostream> 
#include <vector> 
#include <cmath> 
#include <algorithm> 
#include <fstream> 
 
using namespace std; 
 
struct Jet { 
    double E, theta, phi, beta, m; 
}; 
 
void evaluateConstraints(const vector<Jet>& jets, double E_beam, vector<double>& f) { 
    double E_tot = 0.0, Px_tot = 0.0, Py_tot = 0.0, Pz_tot = 0.0; 
    for (int i = 0; i < 4; ++i) { 
        E_tot  += jets[i].E; 
        Px_tot += jets[i].beta * jets[i].E * sin(jets[i].theta) * cos(jets[i].phi); 
        Py_tot += jets[i].beta * jets[i].E * sin(jets[i].theta) * sin(jets[i].phi); 
        Pz_tot += jets[i].beta * jets[i].E * cos(jets[i].theta); 
    } 
    double E12  = jets[0].E + jets[1].E; 
    double Px12 = jets[0].beta * jets[0].E * sin(jets[0].theta) * cos(jets[0].phi) + jets[1].beta * 
jets[1].E * sin(jets[1].theta) * cos(jets[1].phi); 
    double Py12 = jets[0].beta * jets[0].E * sin(jets[0].theta) * sin(jets[0].phi) + jets[1].beta * 
jets[1].E * sin(jets[1].theta) * sin(jets[1].phi); 
    double Pz12 = jets[0].beta * jets[0].E * cos(jets[0].theta) + jets[1].beta * jets[1].E * 
cos(jets[0].theta); 
    double M12_sq = E12 * E12 - (Px12 * Px12 + Py12 * Py12 + Pz12 * Pz12); 
 
    double E34  = jets[2].E + jets[3].E; 
    double Px34 = jets[2].beta * jets[2].E * sin(jets[2].theta) * cos(jets[2].phi) + jets[3].beta * 
jets[3].E * sin(jets[3].theta) * cos(jets[3].phi); 
    double Py34 = jets[2].beta * jets[2].E * sin(jets[2].theta) * sin(jets[2].phi) + jets[3].beta * 
jets[3].E * sin(jets[3].theta) * sin(jets[3].phi); 
    double Pz34 = jets[2].beta * jets[2].E * cos(jets[2].theta) + jets[3].beta * jets[3].E * 
cos(jets[3].theta); 
    double M34_sq = E34 * E34 - (Px34 * Px34 + Py34 * Py34 + Pz34 * Pz34); 
 
    f[0] = E_tot - 2.0 * E_beam; f[1] = Px_tot; f[2] = Py_tot; f[3] = Pz_tot; f[4] = M12_sq - M34_sq; 
} 
 
void computeJacobian(const vector<Jet>& jets, vector<vector<double>>& fm) { 
    for (int i = 0; i < 4; ++i) { 
        int col = i * 3; 
        double E = jets[i].E, th = jets[i].theta, ph = jets[i].phi, b = jets[i].beta; 
        fm[0][col] = 1.0; fm[0][col+1] = 0.0; fm[0][col+2] = 0.0; 
        fm[1][col] = b*sin(th)*cos(ph); fm[1][col+1] = b*E*cos(th)*cos(ph); fm[1][col+2] = -b*E*sin(th)*sin(ph); 
        fm[2][col] = b*sin(th)*sin(ph); fm[2][col+1] = b*E*cos(th)*sin(ph); fm[2][col+2] = 
b*E*sin(th)*cos(ph); 
        fm[3][col] = b*cos(th); fm[3][col+1] = -b*E*sin(th); fm[3][col+2] = 0.0; 
    } 
    for (int i = 0; i < 4; ++i) { 
        int col = i * 3; 
        double sign = (i < 2) ? 1.0 : -1.0; 
        fm[4][col] = sign * 2.0 * jets[i].E; 
        fm[4][col+1] = sign * (-2.0 * jets[i].beta * jets[i].E * sin(jets[i].theta)); 
        fm[4][col+2] = 0.0; 
    } 
} 
 
double calculateMass(const Jet& j1, const Jet& j2) { 
    double E  = j1.E + j2.E; 
    double Px = j1.beta * j1.E * sin(j1.theta) * cos(j1.phi) + j2.beta * j2.E * sin(j2.theta) * 
cos(j2.phi); 
    double Py = j1.beta * j1.E * sin(j1.theta) * sin(j1.phi) + j2.beta * j2.E * sin(j2.theta) * sin(j2.phi); 
    double Pz = j1.beta * j1.E * cos(j1.theta) + j2.beta * j2.E * cos(j2.theta); 
    return sqrt(max(0.0, E * E - (Px * Px + Py * Py + Pz * Pz))); 
} 
 
int main() { 
    double E_beam = 80.5; 
    vector<Jet> jets = { 
        {45.0, 1.2, 0.5, 0.99, 5.0}, {40.0, 2.0, 3.1, 0.99, 5.0}, 
        {42.0, 0.8, -1.5, 0.99, 5.0}, {38.0, 2.3, 1.8, 0.99, 5.0} 
    }; 
    vector<vector<double>> V_m_inv(12, vector<double>(12, 0.0)); 
    for (int i = 0; i < 12; ++i) V_m_inv[i][i] = 1.0; 
 
    vector<double> m0(12), m_nu(12); 
    for (int i = 0; i < 4; ++i) { 
        m0[i * 3]     = jets[i].E; 
        m0[i * 3 + 1] = jets[i].theta; 
        m0[i * 3 + 2] = jets[i].phi; 
    } 
    m_nu = m0; 
    vector<Jet> current_jets = jets; 
 
    // Open output data file 
    ofstream datafile("fit_output.dat"); 
    datafile << "# Iteration M12 M34\n"; 
 
    for (int iter = 0; iter < 10; ++iter) { 
        for (int i = 0; i < 4; ++i) { 
            current_jets[i].E     = m_nu[i * 3]; 
            current_jets[i].theta = m_nu[i * 3 + 1]; 
            current_jets[i].phi   = m_nu[i * 3 + 2]; 
            current_jets[i].beta  = sqrt(max(0.0, 1.0 - (current_jets[i].m * current_jets[i].m) / 
(current_jets[i].E * current_jets[i].E))); 
        } 
 
        double m12 = calculateMass(current_jets[0], current_jets[1]); 
        double m34 = calculateMass(current_jets[2], current_jets[3]); 
        datafile << (iter + 1) << " " << m12 << " " << m34 << "\n"; 
 
        vector<double> f_nu(5); 
        evaluateConstraints(current_jets, E_beam, f_nu); 
        vector<vector<double>> fm(5, vector<double>(12, 0.0)); 
        computeJacobian(current_jets, fm); 
 
        vector<vector<double>> S(5, vector<double>(5, 0.0)); 
        for (int i = 0; i < 5; ++i) 
            for (int j = 0; j < 5; ++j) 
                for (int k = 0; k < 12; ++k) 
                    for (int l = 0; l < 12; ++l) 
                        S[i][j] += fm[i][k] * V_m_inv[k][l] * fm[j][l]; 
 
        vector<double> R(5, 0.0); 
        for (int i = 0; i < 5; ++i) { 
            R[i] = f_nu[i]; 
            for (int j = 0; j < 12; ++j) R[i] += fm[i][j] * (m0[j] - m_nu[j]); 
        } 
 
        vector<vector<double>> S_inv(5, vector<double>(5, 0.0)); 
        for (int i = 0; i < 5; ++i) S_inv[i][i] = 1.0 / (S[i][i] + 1e-12); 
 
        vector<double> lambda(5, 0.0); 
        for (int i = 0; i < 5; ++i) 
            for (int j = 0; j < 5; ++j) 
                lambda[i] += S_inv[i][j] * R[j]; 
 
        vector<double> m_next = m0; 
        for (int i = 0; i < 12; ++i) 
            for (int j = 0; j < 5; ++j) 
                for (int k = 0; k < 12; ++k) 
                    m_next[i] -= V_m_inv[i][k] * fm[j][k] * lambda[j]; 
 
        m_nu = m_next; 
    } 
 
    datafile.close(); 
    cout << "Data saved to fit_output.dat successfully!" << endl; 
    return 0; 
}