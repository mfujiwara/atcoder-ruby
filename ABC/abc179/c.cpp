#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    long long ret = 0;
    for (int i=1;i<N;i++) {
        ret += (N-1)/i;
    }
    cout << ret << endl;
}
