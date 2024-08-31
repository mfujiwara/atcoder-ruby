#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int X,A,B,C;
    cin >> X >> A >> B >> C;
    int a = X*B+C*A*B;
    int b = X*A;
    if (a<b) {
        cout << "Hare" << endl;
    } else if (a>b) {
        cout << "Tortoise" << endl;
    } else {
        cout << "Tie" << endl;
    }
}
