/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    s = s.split(' ');
    s = s[-1];
    s_lenght = s.length;
    return s_lenght;
};