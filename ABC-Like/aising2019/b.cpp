#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,A,B;
    cin >> N >> A >> B;
    vector<int> array(N);
    int tmp;
    int a=0,b=0,c=0;
    for (int i=0;i<N;i++) {
        cin>>tmp;
        if (tmp<=A) {
            a++;
        } else if (tmp<=B) {
            b++;
        } else {
            c++;
        }
    }
    cout << min(a,min(b,c)) << endl;
}
