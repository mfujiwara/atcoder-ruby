#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> array(6);
    for (int i=0;i<6;i++) {
        cin>>array[i];
    }
    sort(array.begin(), array.end());
    cout << array[3] << endl;
}
