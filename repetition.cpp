/*******************************************************
 * Question set:     Introductory Problems
 * Question :        Repetitions
 * Author:           andy41027
 * Date Created:     2025-01-09
 * Description:      find max length of same symbol in a string 
 * Notes:            single traverse: O(n)
 *******************************************************/

#include <iostream>
#include <string>

using namespace std;
string s;
int main() {
    cin >> s;
    int mxcnt = 0;
    int tmp = 1;
    int l = s.length();
    for (int i = 0; i < l; i++) {
        if (s[i] != s[i+1]) {
            mxcnt = max(mxcnt, tmp); 
            tmp = 1;
        }
        else {
            tmp++;
        }
    }
    cout << mxcnt << endl;
}