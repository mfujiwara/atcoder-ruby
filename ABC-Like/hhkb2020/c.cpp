#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    set<int> p;
    int tmp;
    int ret = 0;
    for (int i=0;i<N;i++) {
        cin >> tmp;
        p.insert(tmp);
        while (p.find(ret) != p.end()) {
            ret++;
        }
        cout << ret << endl;
    }
}
