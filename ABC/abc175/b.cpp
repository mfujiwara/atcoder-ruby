#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> L(N);
    for (int i=0;i<N;i++) {
        cin>>L[i];
    }
    int ret=0;
    for (int i=0;i<N-2;i++) {
        for (int j=i+1;j<N-1;j++) {
            if (L[i]==L[j]) continue;
            for (int k=j+1;k<N;k++) {
                if (L[i]==L[k] || L[j]==L[k]) continue;
                if (L[i]<L[j]+L[k] && L[j]<L[i]+L[k] && L[k]<L[i]+L[j]) ret++;
            }
        }
    }
    cout << ret << endl;
}
