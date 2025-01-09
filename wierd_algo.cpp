/*******************************************************
 * Question set:     Introductory Problems
 * Question :        Weird Algorithms
 * Author:           andy41027
 * Date Created:     2025-01-09
 * Description:      looping 
 * Notes:            i/o boost, unsigned ll
 *******************************************************/

# include<bits/stdc++.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;

ull n;
int main(){
    std::cin.tie(0);
    std::ios_base::sync_with_stdio(0);
    cin >> n;
    while (n!=1){
        printf("%llu ", n);
        if (n&1) n = 3*n+1;
        else n >>= 1;
    }
    printf("1\n");
    return 0;
}