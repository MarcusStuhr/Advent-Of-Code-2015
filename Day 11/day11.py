import sys
import re


def next_word(s):
    lenS = len(s)
    if s == "z"*lenS: return "a"*(lenS+1)
    s = map(str,s)
    i = lenS-1
    while i>=0 and s[i] == "z":
        s[i] = "a"
        i-=1
    s[i] = chr(ord(s[i])+1)
    return ''.join(s)


def is_valid_password(password):
    if re.search(r"[iol]",password):
        return False
    
    for i in xrange(len(password)-2):
        if ord(password[i]) == ord(password[i+1])-1 == ord(password[i+2])-2:
            break
    else:
        return False
    
    if len(re.findall(r'(.)\1+', password)) < 2:
        return False

    return True


def get_next_password(password):
    while 1:
        if is_valid_password(password): return password
        password = next_word(password)


def main():
    current_password = "vzbxkghb"
    
    ans_part_1 = get_next_password(current_password)
    ans_part_2 = get_next_password(next_word(ans_part_1))
    
    print "Answer to part 1: {}".format(ans_part_1)
    print "Answer to part 2: {}".format(ans_part_2)

 
if __name__ == "__main__":
    main()