#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    int h;
    cin >> N;
    int maxi=0;
    int ret=0;
    for (int i=0;i<N;i++) {
        cin >> h;
        if (h>=maxi) {
            ret+=1;
            maxi=h;
        }
    }
    cout << ret << endl;
}
