#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<int>> array(N);
    for (int i=0;i<N;i++) {
        int x,y;
        cin >> x >> y;
        array[i]={x,y};
    }
    int ret=0;
    for (int i=0;i<N-1;i++) {
        int x1=array[i][0];
        int y1=array[i][1];
        for (int j=i+1;j<N;j++) {
            int x2=array[j][0];
            int y2=array[j][1];
            if (abs(x2-x1)>=abs(y2-y1)) {
                ret+=1;
            }
        }
    }
    cout << ret << endl;
}
