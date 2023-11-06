/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    s = s.trim();
    s = s.split(' ');
    var lastWord = s[s.length - 1];
    var s_length = lastWord.length;
    return s_length;
};