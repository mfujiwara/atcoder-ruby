#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int A,B,C,D;
    cin >> A >> B >> C >> D;
    cout << min(A+B-C,D) << endl;
}
