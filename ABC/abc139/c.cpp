#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> H(N);
    cin >> H[0];
    int ret=0;
    int now=0;
    for (int i=1;i<N;i++) {
        cin>>H[i];
        if (H[i-1]>=H[i]) {
            now++;
        } else {
            ret=max(ret,now);
            now=0;
        }
    }
    ret=max(ret,now);
    cout<<ret<<endl;
}
