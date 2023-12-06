#include <bits/stdc++.h>
using namespace std;

int main() {
    set<int> s;
    for (int i=0;i<6;i++) {
        int tmp;
        cin >> tmp;
        s.insert(tmp);
    }
    int b;
    cin >> b;
    int c=0;
    bool bonus=false;
    for (int i=0;i<6;i++) {
        int tmp;
        cin >> tmp;
        if (s.count(tmp)) c++;
        if (tmp==b) bonus=true;
    }
    if (c==6) cout << 1 << endl;
    else if (c==5 && bonus) cout << 2 << endl;
    else if (c==5) cout << 3 << endl;
    else if (c==4) cout << 4 << endl;
    else if (c==3) cout << 5 << endl;
    else cout << 0 << endl;
}
