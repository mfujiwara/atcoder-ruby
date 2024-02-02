#include <bits/stdc++.h>
using namespace std;

int main() {
    string N;
    cin >> N;
    int sum = 0;
    vector<int> counts(3, 0);
    for (int i=0;i<N.size();i++) {
        int num = N[i] - '0';
        sum += num;
        counts[num%3]++;
    }
    sum %= 3;
    if (sum == 0) {
        cout << 0 << endl;
    } else if (sum == 1) {
        if (counts[1] >= 1 && N.size() > 1) {
            cout << 1 << endl;
        } else if (counts[2] >= 2 && N.size() > 2) {
            cout << 2 << endl;
        } else {
            cout << -1 << endl;
        }
    } else {
        if (counts[2] >= 1 && N.size() > 1) {
            cout << 1 << endl;
        } else if (counts[1] >= 2 && N.size() > 2) {
            cout << 2 << endl;
        } else {
            cout << -1 << endl;
        }
    }
}
