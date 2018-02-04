// Ref: http://www.cnblogs.com/grandyang/p/6992403.html
#include <iostream>
#include <vector>

using namespace std;
//O(M+N)
vector<int> getNext(string p) {
    int n = p.size(), k = -1, j = 0;
    vector<int> next(n, -1);
    while (j < n - 1) {
        if (k == -1 || p[j] == p[k]) {
            ++k; ++j;next[j] = k;//(p[j] != p[k]) ? k : next[k];
        } else {
            k = next[k];
        }
    }
    return next;
}

int kmp(string s, string p) {
    int m = s.size(), n = p.size(), i = 0, j = 0;
    vector<int> next = getNext(p);
    while (i < m && j < n) {
        if (j == - 1 || s[i] == p[j]) {
            ++i; ++j;
        } else {
            j = next[j];
        }
    }
    return (j == n) ? i - j : -1;
}

int main() {
    vector<int> tp = getNext("ABCDABDE");
    for(int i=0; i<tp.size();i++ )
        cout << tp[i] << ',';
    cout << endl;
    cout << kmp("BBC_ABCDAB_ABCDABCDABDE", "ABCDABD") << endl; // Output: 15
}
