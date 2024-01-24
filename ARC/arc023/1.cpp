#include <bits/stdc++.h>
using namespace std;

int main() {
    int y,m,d;
    cin >> y >> m >> d;
    if (m==1 || m==2) {
        y--;
        m+=12;
    }
    int ret = 365*y + y/4 - y/100 + y/400 + 306*(m+1)/10 + d - 429;
    cout << 735369 - ret << endl;
}
