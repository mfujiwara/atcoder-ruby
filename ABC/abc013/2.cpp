#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,b;
    cin >> a >> b;
    int d = abs(a-b);
    cout << min(d, 10-d) << endl;
}
