#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int tmp = N;
    int n=0;
    while (tmp>0) {
        n += tmp%10;
        tmp /= 10;
    }
    if (N%n==0) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
