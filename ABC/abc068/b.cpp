#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int ret=1;
    while (ret<N && ret*2<=N) {
        ret*=2;
    }
    cout << ret << endl;
}
