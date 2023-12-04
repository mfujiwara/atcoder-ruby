#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    int tmp;
    for (int i=0;i<N-1;i++) {
        cin>>tmp;
        A[tmp-1]++;
    }
    for (int i=0;i<N;i++) {
        cout<<A[i]<<endl;
    }
}
