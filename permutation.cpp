#include<bits/stdc++.h>
using namespace std;
int n, ans=0;
vector<int> permutation;
vector<bool> chosen;
void search(){
    if(permutation.size() == n){
       ans++;
    }else{
        for(int i = 1; i <= n; i++){
            if(chosen[i] ) continue;
            if (permutation.size() > 0 && abs(permutation.back() - i) ==1) continue; 
            chosen[i] = true;
            permutation.push_back(i);
            search();
            chosen[i] = false;
            permutation.pop_back();
        }
    }
}
int main(){
    cin >> n;
    chosen.resize(n+1, false);
    search();
    if (ans == 0) cout << "NO SOLUTION\n";
    else cout << ans << endl;
    return 0;
}