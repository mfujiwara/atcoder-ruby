#include <bits/stdc++.h>
using namespace std;

int main() {
    int H,W;
    cin >> H >> W;
    string tmp;
    string ret;
    for (int i=0;i<H;i++) {
        for (int j=0;j<W;j++) {
            cin >> tmp;
            if (tmp == "snuke") {
                ret=(char)('A'+j) + to_string(i+1);
            }
        }
    }
    cout << ret << endl;
}
