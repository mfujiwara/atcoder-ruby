#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    set<int> st;
    int a;
    for (int i=0;i<N;i++) {
        cin>>a;
        st.insert(a);
    }
    if (st.size()==N) {
        cout<<"YES"<<endl;
    } else {
        cout<<"NO"<<endl;
    }
}
