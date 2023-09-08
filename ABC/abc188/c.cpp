#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A1(1<<(N-1));
    vector<int> A2(1<<(N-1));
    for (int i=0;i<(1<<(N-1));i++) {
        cin>>A1[i];
    }
    for (int i=0;i<(1<<(N-1));i++) {
        cin>>A2[i];
    }
    int max1 = 0;
    int max2 = 0;
    int max1_index = 0;
    int max2_index = 0;
    for (int i=0;i<(1<<(N-1));i++) {
        if (max1 < A1[i]) {
            max1 = A1[i];
            max1_index = i;
        }
        if (max2 < A2[i]) {
            max2 = A2[i];
            max2_index = i;
        }
    }
    if (max1 < max2) {
        cout << max1_index+1 << endl;
    } else {
        cout << max2_index+(1<<(N-1))+1 << endl;
    }
}
