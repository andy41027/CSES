/*******************************************************
 * Question set:     Introductory Problems
 * Question :        Increasing Array
 * Author:           andy41027
 * Date Created:     2025-01-09
 * Description:      make sequence non decrease
 * Constraints:      n: [1,2e5]
 *                   x: [1,1e9]
 * Notes:            use ll for ans
 *******************************************************/

#include<bits/stdc++.h>

using namespace std;

int n;
int main() {
    cin >> n;
    long long int ans = 0;
    vector<int> arr(n+1);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i-1]){
            ans += arr[i-1] - arr[i];
            arr[i] = arr[i-1];
        } 
    }
    cout << ans << endl;
    return 0;
}
