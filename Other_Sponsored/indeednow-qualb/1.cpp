#include <bits/stdc++.h>
using namespace std;

int main() {
    int x1,y1,x2,y2;
    cin >> x1 >> y1 >> x2 >> y2;
    int x = x2-x1;
    int y = y2-y1;
    cout << abs(x1-x2)+abs(y1-y2)+1 << endl;
}
