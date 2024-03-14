#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> primes;
    for (int i=2;i<n;i++) {
        bool isPrime = true;
        for (int j=0;j<primes.size();j++) {
            if (i%primes[j]==0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            primes.push_back(i);
        }
    }
    cout << primes.size() << endl;
}
