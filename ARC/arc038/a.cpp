#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> array(N);
    for (int i=0;i<N;i++) {
        cin>>array[i];
    }
    sort(array.begin(), array.end());
    int ret=0;
    for (int i=N-1;i>=0;i-=2) {
        ret+=array[i];
    }
    cout << ret << endl;
}
