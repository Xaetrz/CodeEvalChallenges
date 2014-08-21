import sys

def has_substring(s, substring): 
    for i in range(len(s)):
        if match_string(s[i:], substring):
            return True
    return False

# Check if string matches given "regular expression" (here only chars, escape \*, and *)
def match_string(s, exp):
    for i in range(len(exp)):
        if i >= len(s):
            return False
        # Assumes escape character is only used for asterisk; otherwise
        # escape character is treated as a normal character
        if exp[i] == '\\' and len(exp) >= 2 and exp[i+1] == '*':
            if s[i] != '*':
                return False
            else:
                return match_string(s[i+1:], exp[i+2:])
        elif exp[i] == '*':
            # Check if there exists a substring on s from rest of exp; 
            # all previous characters in sub must have matched with s
            return has_substring(s[i:], exp[i+1:])
        elif s[i] != exp[i]:
            return False
    return True
        
        
file = open(sys.argv[1], 'r')

for line in file:
    tokens = line.split(",")
    s = tokens[0]
    substring = tokens[1].strip()
    
    if has_substring(s, substring):
        print('true')
    else:
        print('false')
    
file.close()