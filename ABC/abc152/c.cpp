#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int tmp;
    int min = 1000000000;
    int ret=0;
    for (int i=0;i<N;i++) {
        cin >> tmp;
        if (tmp<=min) {
            ret++;
            min = tmp;
        }
    }
    cout << ret << endl;
}
