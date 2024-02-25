#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    for (int bit = 0; bit < (1<<3); ++bit) {
        int sum = S[0] - '0';
        string ret = S.substr(0, 1);
        for (int i = 0; i < 3; ++i) {
            if (bit & (1<<i)) {
                sum += S[i+1] - '0';
                ret += '+';
            } else {
                sum -= S[i+1] - '0';
                ret += '-';
            }
            ret += S[i+1];
        }
        if (sum == 7) {
            cout << ret << "=7" << endl;
            return 0;
        }
    }
}
