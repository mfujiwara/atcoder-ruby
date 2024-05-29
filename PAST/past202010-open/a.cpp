#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    vector<pair<int, string>> A(3);
    for (int i=0;i<3;i++) {
        cin >> A[i].first;
    }
    A[0].second = "A";
    A[1].second = "B";
    A[2].second = "C";
    sort(A.begin(),A.end());
    cout << A[1].second << endl;
}
