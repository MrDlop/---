#include <bits/stdc++.h>

using namespace std;

double f(double x){
    return x*x*x > 10000 ? 0 : x*x*x;
}

bool arr[1000][1000];
signed main()
{
    double s = 0;
    double dy = 1e9;
    int max_y = 100;
    for(double i =-50; i < 50; ++i){
        dy = min(dy, f(i) - f(i - 1));
    }
    for(int i = -50; i < 50; ++i){
        arr[max_y / 2 - int(f(i) / dy)][i+50] = true;
    }
    for(int i = 0; i <= max_y; ++i){
        for(int j = 0; j <= 150; ++j){
            if(arr[i][j]) cout << "*";
            else if(i == max_y / 2 || j == max_y / 2) cout << "+";
            else cout << " ";
        }
        cout << '\n';
    }
    return 0;
}
