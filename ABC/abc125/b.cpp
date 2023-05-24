#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;
    cin>>N;
    vector<int> v_array(N);
    vector<int> c_array(N); 
    for (int i=0;i<N;i++) {
        cin>>v_array[i];
    }
    for (int i=0;i<N;i++) {
        cin>>c_array[i];
    }
    int ret=0;
    for (int i=0;i<N;i++) {
        if (v_array[i]>c_array[i]) {
            ret+=v_array[i]-c_array[i];
        }
    }
    cout<<ret<<endl;
}
