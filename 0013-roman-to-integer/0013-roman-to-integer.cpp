class Solution {
public:
    int romanToInt(string s) {
        int total = 0;
        std::map<char, int> numerals;
        numerals['I'] = 1;
        numerals['V'] = 5;
        numerals['X'] = 10;
        numerals['L'] = 50;
        numerals['C'] = 100;
        numerals['D'] = 500;
        numerals['M'] = 1000;
        for(int pos = 0; pos < s.size() - 1; ++pos) {
            if(numerals[s[pos]] < numerals[s[pos + 1]])
                total -= numerals[s[pos]];
            else 
                total += numerals[s[pos]];
        }
        total += numerals[s[s.size()-1]];
        return total;
    }
};