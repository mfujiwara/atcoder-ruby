#include <bits/stdc++.h>
using namespace std;

int main() {
    long long a,b;
    cin >> a >> b;
    if (a<=0 && 0<=b) {
        cout << "Zero" << endl;
    } else if (b<0 && (b-a)%2==0) {
        cout << "Negative" << endl;
    } else {
        cout << "Positive" << endl;
    }
}
