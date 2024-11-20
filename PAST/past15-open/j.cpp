#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    long long M;
    cin >> N >> M;
    map<long long,long long> memo;
    long long ret = 0;
    for (int i=0;i<N;i++) {
        long long a,b;
        int x;
        cin >> a >> b >> x;
        if (x==0) {
            if (b>1) {
                memo[-a] += b-1;
                ret += a*(b-1);
            }
        } else {
            if (b==1) {
                memo[-a] += 1;
                ret += a;
            } else {
                memo[-a*2] += 1;
                ret += a*2;
                if (b>2) {
                    memo[-a] += b-2;
                    ret += a*(b-2);
                }
            }
        }
    }
    while (ret>0 && M>0) {
        auto it = memo.begin();
        long long a = -it->first;
        long long b = it->second;
        if (b>M) {
            ret -= a*M;
            M = 0;
        } else {
            ret -= a*b;
            M -= b;
            memo.erase(it);
        }
    }
    cout << ret << endl;
}
