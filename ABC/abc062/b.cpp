#include <bits/stdc++.h>
using namespace std;

int main() {
    int H,W;
    cin >> H >> W;
    string tmp;
    cout << string(W+2,'#') << endl;
    for (int i=0;i<H;i++) {
        cin >> tmp;
        cout << "#" << tmp << "#" << endl;
    }
    cout << string(W+2,'#') << endl;
}
