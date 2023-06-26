#include <bits/stdc++.h>
using namespace std;

int group(int x);
int group(int x) {
    if (x==1 || x==3 || x==5 || x==7 || x==8 || x==10 || x==12) {
        return 1;
    } else if (x==4 || x==6 || x==9 || x==11) {
        return 2;
    } else {
        return 3;
    }
}

int main() {
    int x,y;
    cin >> x >> y;
    int gx = group(x);
    int gy = group(y);
    if (gx==gy) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
