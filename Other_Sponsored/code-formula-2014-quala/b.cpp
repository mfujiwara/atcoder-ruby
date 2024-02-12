#include <bits/stdc++.h>
using namespace std;

int main() {
    int a,b;
    cin >> a >> b;
    vector<string> array(10,"x");
    int tmp;
    for (int i=0;i<a;i++) {
        cin>>tmp;
        array[tmp] = ".";
    }
    for (int i=0;i<b;i++) {
        cin>>tmp;
        array[tmp] = "o";
    }
    cout << array[7] << " " << array[8] << " " << array[9] << " " << array[0] << endl;
    cout << " " << array[4] << " " << array[5] << " " << array[6] << endl;
    cout << "  " << array[2] << " " << array[3] << endl;
    cout << "   " << array[1] << endl;
}
