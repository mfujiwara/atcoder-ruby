#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,Q;
    cin >> N >> Q;
    vector<int> A(N+2);
    for (int i=0;i<N+2;i++) {
        A[i] = i;
    }
    set<int> s;
    for (int i=0;i<Q;i++) {
        int t,x,y;
        cin >> t >> x >> y;
        if (t==1) {
            swap(A[x],A[x+1]);
            if (A[x]>A[x+1]) {
                s.insert(x);
            } else {
                s.erase(x);
            }
            if (A[x-1]>A[x]) {
                s.insert(x-1);
            } else {
                s.erase(x-1);
            }
            if (A[x+1]>A[x+2]) {
                s.insert(x+1);
            } else {
                s.erase(x+1);
            }
        } else {
            set<int> ns;
            while (!s.empty()) {
                int j = *s.begin();
                s.erase(j);
                if (x<=j && j<y) {
                    swap(A[j],A[j+1]);
                    if (A[j]>A[j+1]) {
                        s.insert(j);
                    } else {
                        s.erase(j);
                    }
                    if (A[j-1]>A[j]) {
                        s.insert(j-1);
                    } else {
                        s.erase(j-1);
                    }
                    if (A[j+1]>A[j+2]) {
                        s.insert(j+1);
                    } else {
                        s.erase(j+1);
                    }
                } else {
                    ns.insert(j);
                }
            }
            s = ns;
        }
    }
    for (int i=1;i<=N;i++) {
        cout << A[i];
        if (i<N) {
            cout << " ";
        }
    }
    cout << endl;
}
