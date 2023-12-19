#include <bits/stdc++.h>
using namespace std;

int main() {
    string A,B;
    cin >> A >> B;
    string C = A + B;
    int ret = stoi(C);
    cout << ret*2 << endl;
}
