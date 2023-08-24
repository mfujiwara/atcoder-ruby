#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> array(4);
    int tmp;
    for (int i=0;i<6;i++) {
        cin>>tmp;
        array[tmp-1]++;
    }
    for (int i=0;i<4;i++) {
        if (array[i] == 0 || array[i] > 2) {
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;
}
