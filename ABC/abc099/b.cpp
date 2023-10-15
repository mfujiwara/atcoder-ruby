#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,b;
    cin >> a >> b;
    int diff = b-a;
    int B=(1+diff)*diff/2;
    cout << B-b << endl;
}
