#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> R(N); 
    for (int i=0;i<N;i++) {
        cin >> R[i];
    }
    sort(R.begin(), R.end(), greater<int>());
    int ret = 0;
    for (int i=0;i<N;i++) {
        if (i%2==0) {
            ret += R[i]*R[i];
        } else {
            ret -= R[i]*R[i];
        }
    }
    cout << fixed << setprecision(10);
    cout << ret*M_PI << endl;
}
