#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    if (N<=59) {
        cout << "Bad" << endl;
    } else if (N<=89) {
        cout << "Good" << endl;
    } else if (N<=99) {
        cout << "Great" << endl;
    } else {
        cout << "Perfect" << endl;
    }
}
