// Implement strStr().

// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

// Clarification:

// What should we return when needle is an empty string? This is a great question to ask during an interview.

// For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

// Example 1:

// Input: haystack = "hello", needle = "ll"
// Output: 2
// Example 2:

// Input: haystack = "aaaaa", needle = "bba"
// Output: -1
 

// Constraints:

// 1 <= haystack.length, needle.length <= 104
// haystack and needle consist of only lowercase English characters.

// ababaca
// bba
// bb
function buildPrefix(str) {
    const prefixs = [0];

    let prefix = 0;
    for (let i = 1; i < str.length; i++) {
        while (str[prefix] !== str[i] && prefix > 0) {
            prefix = prefixs[prefix - 1];
        }

        if (str[prefix] === str[i]) {
            prefix++;
        }

        prefixs.push(prefix);
    }
}

function kmp(t, p) {
    const prefixs = buildPrefix(p);
    let prefix = 0;
    for (let i = 0; i < t.length; i++) {
        while(p[prefix] !== t[i] && prefix > 0) {
            prefix = prefixs[prefix - 1];
        }

        if (p[prefix] === t[i]) {
            prefix++;
        }

        if (prefix === (p.length)) {
            return i + 1 - prefix;
        }
    }

    return -1;
}

console.log(kmp('abab', 'abab'));