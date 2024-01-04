#include <bits/stdc++.h>
using namespace std;

int main() {
    string S = "DiscoPresentsDiscoveryChannelProgrammingContest2016";
    int W;
    cin >> W;
    int i = 0;
    while (i < S.size()) {
        cout << S.substr(i, W) << endl;
        i += W;
    }
}
