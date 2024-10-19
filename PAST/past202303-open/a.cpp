#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N,S,T;
    cin >> N >> S >> T;
    if ((N+S)%2==T) {
        cout << "Bob" << endl;
    } else {
        cout << "Alice" << endl;
    }
}
