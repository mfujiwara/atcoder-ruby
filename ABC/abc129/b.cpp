#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> sums(N+1);
    sums[0]=0;
    for (int i=1;i<=N;i++) {
        int w;
        cin>>w;
        sums[i]=sums[i-1]+w;
    }
    int ret=1000000000;
    for (int i=1;i<=N;i++) {
        int s1=sums[i];
        int s2=sums[N]-sums[i];
        ret=min(ret,abs(s1-s2));
    }
    cout << ret << endl;
}
