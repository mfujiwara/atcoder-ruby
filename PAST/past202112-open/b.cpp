#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    int ret = 0;
    for (int i=0;i<N;i++) {
        int A,B;
        cin >> A >> B;
        B-=A;
        if (B%100>=50) {
            ret+=1;
        }
        if (B%10>=5) {
            ret+=1;
        }
    }
    cout << ret << endl;
}
