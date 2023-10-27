#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    if (N%10<=6) {
        cout << N/10*100+N%10*15 << endl;
    } else {
        cout << (N/10+1)*100 << endl;
    }
}
