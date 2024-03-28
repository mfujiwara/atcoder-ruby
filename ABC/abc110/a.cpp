#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> abc(3);
    cin >> abc[0] >> abc[1] >> abc[2];
    sort(abc.begin(), abc.end());
    cout << abc[0]+abc[1]+abc[2]*10 << endl;
}
