import re


def shift_letter(letter, n):
    """
    Shifts a letter by n characters to the left/right, depending on the sign of n
    """
    return chr(ord(letter)+n)


def next_word_no_stopletters(s):
    """
    Increments the string s to the next string containing no 'i', 'o', or 'l'
    """
    for i in xrange(len(s)):
        if s[i] in "iol":
            return next_word(s[:i+1] + "z"*(len(s)-i-1))
    return s


def next_word(s):
    """
    Increments the string s to the next lexicographic string.
    e.g. "abc" -> "abd", "z" -> "aa"
    """
    lenS = len(s)
    if s == "z"*lenS: return "a"*(lenS+1)
    s = map(str,s)
    i = lenS-1
    while i>=0 and s[i] == "z":
        s[i] = "a"
        i-=1
    s[i] = shift_letter(s[i],1)
    return ''.join(s)


def is_valid_password(password):
    """
    Returns True if the password string is valid, and False otherwise.
    Criteria:
        1. Does not contain any letters 'i', 'o', or 'l'
        2. Has at least one three-letter increasing consecutive straight (e.g. "abc", "pqr", etc)
        3. Has at least two non-overlapping pairs (e.g "aa", "bb", etc).
    """
    if re.search(r"[iol]",password):
        return False

    for i in xrange(len(password)-2):
        if password[i] == shift_letter(password[i+1],-1) == shift_letter(password[i+2],-2):
            break
    else:
        return False

    if len(re.findall(r'(.)\1+', password)) < 2:
        return False

    return True


def get_next_valid_password(password):
    """
    Finds the next valid password by repeatedly incrementing and checking the password.
    """
    password = next_word_no_stopletters(password)
    while 1:
        if is_valid_password(password):
            return password
        password = next_word(password)


def main():
    current_password = "vzbxkghb"
    ans_part_1 = get_next_valid_password(current_password)
    ans_part_2 = get_next_valid_password(next_word(ans_part_1))

    print "Answer to part 1: {}".format(ans_part_1)
    print "Answer to part 2: {}".format(ans_part_2)


if __name__ == "__main__":
    main()