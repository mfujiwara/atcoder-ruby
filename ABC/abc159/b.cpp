#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int N = S.size();
    string S1 = S.substr(0, (N-1)/2);
    string S2 = S.substr((N+3)/2-1,N);
    string Sr = S;
    reverse(Sr.begin(), Sr.end());
    string S1r = S1;
    reverse(S1r.begin(), S1r.end());
    string S2r = S2;
    reverse(S2r.begin(), S2r.end());
    if (S == Sr && S1 == S1r && S2 == S2r) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
