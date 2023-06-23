#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    string S;
    cin >> N >> S;
    for (int i=0;i<S.size();i++) {
        S[i] = (S[i] - 'A' + N) % 26 + 'A';
    }
    cout << S << endl;
}
