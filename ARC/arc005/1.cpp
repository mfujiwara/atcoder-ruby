#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int ret = 0;
    string s;
    for (int i=0;i<N;i++) {
        cin >> s;
        if (i==N-1) {
            s = s.substr(0, s.size()-1);
        }
        if (s=="TAKAHASHIKUN" || s=="Takahashikun" || s=="takahashikun") {
            ret++;
        }
    }
    cout << ret << endl;
}
