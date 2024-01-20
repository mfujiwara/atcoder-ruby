#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,a;
    cin >> N;
    int ret = 0;
    for (int i=0;i<N;i++) {
        cin >> a;
        while (a%2==0 || a%3==2) {
            a--;
            ret++;
        }
    }
    cout << ret << endl;
}
