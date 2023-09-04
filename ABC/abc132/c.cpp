#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> array(N);
    for (int i=0;i<N;i++) {
        cin >> array[i];
    }
    sort(array.begin(), array.end());
    cout << array[N/2] - array[N/2-1] << endl;
}
