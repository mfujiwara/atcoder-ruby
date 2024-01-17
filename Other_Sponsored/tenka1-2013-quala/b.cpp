#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int ret = 0;
    for (int i=0;i<N;i++) {
        int sum = 0;
        for (int j=0;j<5;j++) {
            int a;
            cin >> a;
            sum += a;
        }
        if (sum < 20) {
            ret++;
        }
    }
    cout << ret << endl;
}
