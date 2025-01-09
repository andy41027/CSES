/*******************************************************
 * Question set:     Introductory Problems
 * Question :        Missing Number
 * Author:           andy41027
 * Date Created:     2025-01-09
 * Description:      find missing element from [1,n]
 * Notes:            since n small (~2*10^5), using set insert/delete both take O(logn) time, total time: O(2n*logn) would be acceptable
 *******************************************************/

# include<bits/stdc++.h>
using namespace std;

int n;
int main(){
    std::cin.tie(0);
    std::ios_base::sync_with_stdio(0);
    cin >> n;
    set<int> s;
    for (int i = 1; i <= n; i++) {
        s.insert(i);
    }
    for (int i=1; i<n; i++){
        int x;
        cin >> x;
        s.erase(x);
    }
    cout << *s.begin() << endl;
    return 0;
}