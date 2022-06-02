'''
-Hard-

Given a string representing a code snippet, you need to implement a tag validator to parse the 
code and return whether it is valid. A code snippet is valid if all the following rules hold:

The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>. Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.
A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters until the next > should be parsed as TAG_NAME (not necessarily valid).
The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of CDATA_CONTENT is defined as the characters between <![CDATA[ and the first subsequent ]]>.
CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters.
Valid Code Examples:
Input: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"

Output: True

Explanation: 

The code is wrapped in a closed tag : <DIV> and </DIV>. 

The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata. 

Although CDATA_CONTENT has unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as tag.

So TAG_CONTENT is valid, and then the code is valid. Thus return true.


Input: "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"

Output: True

Explanation:

We first separate the code into : start_tag|tag_content|end_tag.

start_tag -> "<DIV>"

end_tag -> "</DIV>"

tag_content could also be separated into : text1|cdata|text2.

text1 -> ">>  ![cdata[]] "

cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"

text2 -> "]]>>]"


The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.
Invalid Code Examples:
Input: "<A>  <B> </A>   </B>"
Output: False
Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.

Input: "<DIV>  div tag is not closed  <DIV>"
Output: False

Input: "<DIV>  unmatched <  </DIV>"
Output: False

Input: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
Output: False

Input: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
Output: False

Input: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
Output: False
Note:
For simplicity, you could assume the input code (including the any characters mentioned 
above) only contain letters, digits, '<','>','/','!','[',']' and ' '.


'''


'''
TagTail
TagHead
Text
Cdata
'''

import re

re_head = re.compile(r'<([A-Za-z0-9]*)>')
re_tail = re.compile(r'<\/([A-Za-z0-9]*)>')
re_cdata = re.compile(r'<\!\[CDATA\[(.*?)\]\]>')
re_valid_head = re.compile(r'^[A-Z]{1,9}$')
re_invalid_text = re.compile(r'<')


class Token:
    HEAD = 0
    TAIL = 1
    CDATA = 2
    TEXT = 3


def lexer(s):
    pos = 0
    while pos < len(s):
        cdata_match = re_cdata.match(s, pos)
        if cdata_match:
            yield Token.CDATA, None  # don't care cdata content
            pos += len(cdata_match.group(0))
            continue
        head_match = re_head.match(s, pos)
        if head_match:
            yield Token.HEAD, head_match.group(1)
            pos += len(head_match.group(0))
            continue
        tail_match = re_tail.match(s, pos)
        if tail_match:
            yield Token.TAIL, tail_match.group(1)
            pos += len(tail_match.group(0))
            continue
        # non of these match, must be text, it++
        yield Token.TEXT, s[pos]
        pos += 1


def parser(tokens):
    stack = []
    done = False
    for typ, content in tokens:
        if done:
            # if already done, but comes more tokens, return False
            return False
        # print(typ, content)
        if typ == Token.HEAD:
            if not re_valid_head.match(content):
                return False
            stack.append(content)
        else:
            if not stack:
                return False  # no other tokens in naked env
            if typ == Token.TAIL:
                if stack[-1] != content:
                    return False
                stack.pop()
            elif typ == Token.TEXT:
                if re_invalid_text.match(content):
                    return False
            else:  # cdata, always ok
                pass
        # after one token, check if had done
        if not stack:
            done = True
    return done


class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        return parser(lexer(code))
    
    def isValid2(self, code: str) -> bool:
        stack = []
        i, n = 0, len(code)
        while i < n:
            if i>0 and not stack:
                return False
            if code.startswith('<![CDATA[', i):
                j = i+9
                try:
                    i = code.index(']]>', j)
                except ValueError:
                    return False
                i += 3
            elif code.startswith('</', i):
                j = i+2
                try:
                    i = code.index('>', j)
                except ValueError:
                    return False
                if i == j or i - j > 9:
                    return False
                for k in range(j, i):
                    if not code[k].isupper():
                        return False
                s = code[j:i]
                if not stack or stack.pop() != s:
                    return False
                i += 1
            elif code.startswith('<',i):
                j = i + 1
                try:
                    i = code.index('>',j)
                except ValueError:
                    return False
                if i == j or i - j > 9:
                    return False
                for k in range(j, i):
                    if not code[k].isupper():
                        return False
                s = code[j:i]
                stack.append(s)
                i += 1
            else:
                i += 1
        return not stack

    def isValidStateMachine(self, code):
        """
        :type code: str
        :rtype: bool
        """
        stack = []
        
        state = ["plain", "open", "close", "cdata"]
        curr = "plain"        
        
        open_tag = []
        close_tag = []
        
        idx = 0
        
        while idx < len(code):
            ch = code[idx]
                        
            if curr == "plain":
                if not stack and idx != 0:
                    # code is not in a closed tage
                    print('code is not in a closed tage')
                    return False
                
                if code[idx:idx+9] == "<![CDATA[":
                    curr = "cdata"
                    idx += 9
                    continue
                elif code[idx:idx+2] == '</':
                    curr = 'close'
                    idx += 2
                    continue
                elif ch == '<':
                    curr = "open"
                
            elif curr == "open":
                if ch == '>':
                    if len(open_tag) > 9 or len(open_tag) < 1:
                        print('open tag name length not valid')
                        return False
                    
                    stack.append("".join(open_tag))
                    open_tag = []
                    curr = 'plain'
                    idx += 1
                    continue
                
                if not ch.isupper():
                    print('open tag is not upper', ch)
                    return False
                
                open_tag.append(ch)
            
            elif curr == 'close':
                if ch == '>':
                    if len(close_tag) > 9 or len(close_tag) < 1:
                        print('close tag name length not valid')
                        return False
                    
                    close_tag_str = "".join(close_tag)
                    if not stack or close_tag_str != stack[-1]:
                        print('tag no match')
                        return False
                    else:
                        stack.pop()
                    
                    close_tag = []
                    curr = 'plain'
                    idx += 1
                    continue
                    
                if not ch.isupper():
                    print('close tag is not upper')
                    return False
                
                close_tag.append(ch)
                    
            elif curr == "cdata":
                if code[idx:idx+3] == ']]>':
                    idx += 3
                    curr = "plain"
                    continue
                    
            idx += 1
            
        #print(curr)
                    
        if stack or curr != "plain":
            return False
        
        return True


def main():
    tests = [
        '<DIV>This is the first line <![CDATA[<div>]]></DIV>',
        '<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>',
        '<A>  <B> </A>   </B>',
        '<DIV> closed tags with invalid tag name  <b>123</b> </DIV>',
        "<A></A><B></B>",
        '<![CDATA[<div>]>]]>',
        "<DIV>  unmatched <  </DIV>"
    ]
    for test in tests:
        print(Solution().isValid(test))
        print(Solution().isValidStateMachine(test))

    


if __name__ == '__main__':
    main()
