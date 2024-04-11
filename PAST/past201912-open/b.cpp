#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int now;
    int next;
    cin >> now;
    for (int i=1;i<N;i++) {
        cin >> next;
        if (now == next) {
            cout << "stay" << endl;
        } else if (now < next) {
            cout << "up " << next-now << endl;
        } else {
            cout << "down " << now-next << endl;
        }
        now = next;
    }
}
