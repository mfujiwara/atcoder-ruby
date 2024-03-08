#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    set<long long> A;
    for (int i=0;i<N;i++) {
        long long a;
        cin >> a;
        A.insert(a);
    }
    while (A.size() > 1) {
        long long a = *A.begin();
        long long b = *A.rbegin();
        A.erase(b);
        A.insert(b-a);
    }
    cout << *A.begin() << endl;
}
