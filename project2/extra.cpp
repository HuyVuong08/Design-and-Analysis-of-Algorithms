#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <chrono>
#include <iomanip>
#include <sstream>
#include <functional>
#include <fstream>

// Helper function for comma formatting numbers
std::string format_with_commas(long long n) {
    std::stringstream ss;
    ss.imbue(std::locale(""));
    ss << std::fixed << n;
    return ss.str();
}

class Fibonacci {
public:
    unsigned long long int recursive(unsigned long long int n) {
        if (n <= 1) return n;
        return recursive(n-1) + recursive(n-2);
    }

    unsigned long long int memoizedTopDown(unsigned long long int n, std::map<int, unsigned long long int> M) {
        if (M.find(n) != M.end()) return M[n];
        if (n <= 1) {
            M[n] = n;
            return n;
        }
        M[n] = memoizedTopDown(n-1, M) + memoizedTopDown(n-2, M);
        return M[n];
    }

    unsigned long long int bottomUp(unsigned long long int n) {
        unsigned long long int M1 = 0;
        unsigned long long int M2 = 1;
        if (n == 1) return 0;
        if (n == 2) return 1;
        //std::vector<unsigned long long int> M(n+1, 0);
        
        for (int i = 2; i <= n; i++) {
            unsigned long long int tmp = M2 + M1;
            M1 = M2;
            M2 = tmp;
        }
        return M1;
    }
};

int main() {
    Fibonacci fib;
    std::ofstream outFile("extra_credit.txt");

    // long input = 60;
    // std::cout << "Fibonacci(" << input << ") using recursive: " << std::endl;
    // auto start = std::chrono::high_resolution_clock::now();
    // long long reesult = fib.recursive(input);
    // auto end = std::chrono::high_resolution_clock::now();
    // auto duration = std::chrono::duration_cast<std::chrono::seconds>(end - start).count();
    // std::cout << duration << " seconds" << std::endl;
    // outFile << "Fibonacci(" << input << ") using recursive: " << std::endl;
    // outFile << duration << " seconds" << std::endl;

    // long input = 10000;
    // std::map<int, unsigned long long int> M;
    // std::cout << "Fibonacci(" << input << ") using Memoized Top Down: " << std::endl;
    // auto start = std::chrono::high_resolution_clock::now();
    // long long reesult = fib.memoizedTopDown(input, M);
    // auto end = std::chrono::high_resolution_clock::now();
    // auto duration = std::chrono::duration_cast<std::chrono::seconds>(end - start).count();
    // std::cout << duration << " seconds" << std::endl;
    // outFile << "Fibonacci(" << input << ") using Memoized Top Down: " << std::endl;
    // outFile << duration << " seconds" << std::endl;

    unsigned long long int input = 1000000000;
    std::cout << "Fibonacci(" << input << ") using Bottom Up: " << std::endl;
    auto start = std::chrono::high_resolution_clock::now();
    auto reesult = fib.bottomUp(input);
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::seconds>(end - start).count();
    std::cout << duration << " seconds" << std::endl;
    outFile << "Fibonacci(" << input << ") using Bottom Up: " << std::endl;
    outFile << duration << " seconds" << std::endl;

    return 0;
}