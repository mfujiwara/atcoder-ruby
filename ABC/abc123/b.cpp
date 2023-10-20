#include <bits/stdc++.h>
using namespace std;

int main() {
    int loss=0;
    int ret=0;
    for (int i=0;i<5;i++) {
        int tmp;
        cin>>tmp;
        if (tmp%10==0) {
            ret+=tmp;
        } else {
            ret+=tmp+(10-tmp%10);
            loss=max(loss,10-tmp%10);
        }
    }
    cout<<ret-loss<<endl;
}
