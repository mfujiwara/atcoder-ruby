#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    string S;
    cin >> S;
    int left = -1;
    int right = -1;
    int pre = -1;
    int maxDiff = 0;
    for (int i=0;i<N;i++) {
        if (S[i] == '#') {
            if (left==-1) {
                left = i;
                right = N-1-i;
            } else {
                right = N-1-i;
                maxDiff = max(maxDiff, i-pre-1);
            }
            pre = i;
        }
    }
    if (left+right < maxDiff) {
        left += maxDiff - (left+right);
    }
    cout << left << " " << right << endl;
}
