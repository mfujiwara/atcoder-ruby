#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,K;
    cin >> N >> K;
    vector<long> array(N);
    for (int i=0;i<N;i++) {
        cin>>array[i];
    }
    sort(array.begin(), array.end());
    for (int i=N-1;i>-1&&K>0;i--) {
        array[i] = 0;
        K--;
    }
    long sum = 0;
    for (int i=0;i<N;i++) {
        sum += array[i];
    }
    cout << sum << endl;
}
