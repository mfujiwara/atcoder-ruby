#include <bits/stdc++.h>
using namespace std;

int main() {
    int A1,A2,A3;
    cin >> A1 >> A2 >> A3;
    cout << max({A1,A2,A3})-min({A1,A2,A3}) << endl;
}
