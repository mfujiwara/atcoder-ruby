#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,A,B;
    cin >> N >> A >> B;
    if (N%(A+B) <= A && N%(A+B) != 0) {
        cout << "Ant" << endl;
    } else {
        cout << "Bug" << endl;
    }
}
