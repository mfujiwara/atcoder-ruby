#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int calc() {
    int N,A,M;
    cin >> N >> A >> M;
    vector<int> days(M);
    vector<int> sums = {0};
    int i = 1;
    int ret = 0;
    while (i<=N) {
        int t = (-A*i%M+M)%M;
        if (days[t] != 0) {
            break;
        } else {
            days[t] = i;
            ret += t;
            sums.push_back(ret);
        }
        i+=1;
    }
    if (i>N) {
        cout << ret << endl;
        return 0;
    }
    int j = days[(-A*i%M+M)%M]; // j日目とi日目が同じ
    int k = i-j; // k日間の繰り返し
    int l = (N-j)/k; // l回繰り返す
    int diff = ret-sums[j-1];
    ret = sums[j-1] + diff*l;
    i = j+l*k;
    while (i<=N) {
        int t = (-A*i%M+M)%M;
        ret += t;
        i+=1;
    }
    cout << ret << endl;
    return 0;
}

int main() {
    int T;
    cin >> T;
    for (int i=0;i<T;i++) {
        calc();
    }
}
