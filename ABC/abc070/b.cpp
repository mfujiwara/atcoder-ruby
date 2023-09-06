#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B,C,D;
    cin >> A >> B >> C >> D;
    int c=0;
    for (int i=0;i<=100;i++) {
        if (A<=i && i<B && C<=i && i<D) {
            c++;
        }
    }
    cout << c << endl;
}
