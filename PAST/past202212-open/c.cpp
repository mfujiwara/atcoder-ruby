#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i=0;i<N;i++) {
        cin>>A[i];
    }
    set<int> s;
    for (int i=0;i<N-2;i++) {
        for (int j=i+1;j<N-1;j++) {
            for (int k=j+1;k<N;k++) {
                s.insert(A[i]*A[j]*A[k]);
            }
        }
    }
    cout << s.size() << endl;
}
