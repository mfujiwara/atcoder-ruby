#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> p(N);
    for (int i=0;i<N;i++) {
        cin>>p[i];
    }
    vector<int> p_sorted = p;
    sort(p_sorted.begin(), p_sorted.end());
    int count = 0;
    for (int i=0;i<N;i++) {
        if (p[i] != p_sorted[i]) {
            count++;
        }
    }
    if (count <= 2) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}
