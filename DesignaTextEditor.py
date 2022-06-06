'''

-Hard-
*Stack*
*Deque*
*Doubly Linked List*

Design a text editor with a cursor that can do the following:

Add text to where the cursor is.
Delete text from where the cursor is (simulating the backspace key).
Move the cursor either left or right.
When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds.

Implement the TextEditor class:

TextEditor() Initializes the object with empty text.
void addText(string text) Appends text to where the cursor is. The cursor ends to the right of text.
int deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
string cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
string cursorRight(int k) Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
 

Example 1:

Input
["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]
Output
[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]

Explanation
TextEditor textEditor = new TextEditor(); // The current text is "|". (The '|' character represents the cursor)
textEditor.addText("leetcode"); // The current text is "leetcode|".
textEditor.deleteText(4); // return 4
                          // The current text is "leet|". 
                          // 4 characters were deleted.
textEditor.addText("practice"); // The current text is "leetpractice|". 
textEditor.cursorRight(3); // return "etpractice"
                           // The current text is "leetpractice|". 
                           // The cursor cannot be moved beyond the actual text and thus did not move.
                           // "etpractice" is the last 10 characters to the left of the cursor.
textEditor.cursorLeft(8); // return "leet"
                          // The current text is "leet|practice".
                          // "leet" is the last min(10, 4) = 4 characters to the left of the cursor.
textEditor.deleteText(10); // return 4
                           // The current text is "|practice".
                           // Only 4 characters were deleted.
textEditor.cursorLeft(2); // return ""
                          // The current text is "|practice".
                          // The cursor cannot be moved beyond the actual text and thus did not move. 
                          // "" is the last min(10, 0) = 0 characters to the left of the cursor.
textEditor.cursorRight(6); // return "practi"
                           // The current text is "practi|ce".
                           // "practi" is the last min(10, 6) = 6 characters to the left of the cursor.
 

Constraints:

1 <= text.length, k <= 40
text consists of lowercase English letters.
At most 2 * 104 calls in total will be made to addText, deleteText, cursorLeft and cursorRight.


'''



class TextEditor:

    def __init__(self):
        self.s = ''
        self.cur = 0
        

    def addText(self, text: str) -> None:
        self.s = self.s[:self.cur] + text + self.s[self.cur:]
        self.cur += len(text)
        # print(self.s, self.cur)

    def deleteText(self, k: int) -> int:
        if k < self.cur:
            ans = k
            if self.cur == len(self.s):
                self.s = self.s[:self.cur-k]
            else:
                self.s = self.s[:self.cur-k] + self.s[self.cur:]
            self.cur -= k
        else:
            ans = self.cur
            self.s = self.s[self.cur:]
            self.cur = 0
        return ans
        

    def cursorLeft(self, k: int) -> str:
        if k < self.cur:
             self.cur -= k
             if self.cur >= 10:
                 ans = self.s[self.cur-10:self.cur]                    
             else:
                 ans = self.s[:self.cur]
        else:
            self.cur = 0
            ans = ''
        return ans
            
                
        

    def cursorRight(self, k: int) -> str:
        if self.cur + k <= len(self.s):
            self.cur += k
            if self.cur >= 10:
                 ans = self.s[self.cur-10:self.cur]                    
            else:
                 ans = self.s[:self.cur]
        else:
            self.cur = len(self.s)
            if self.cur >= 10:
                 ans = self.s[self.cur-10:self.cur]                    
            else:
                 ans = self.s[:self.cur]
        return ans


class TextEditor2:

    def __init__(self):
        self.left = []
        self.right = []
        
        

    def addText(self, text: str) -> None:
        for c in text:
            self.left.append(c)       

    def deleteText(self, k: int) -> int:
        cnt = 0
        while self.left and k > 0:
            self.left.pop()
            cnt += 1
            k -= 1         
        return cnt
        

    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.left:
            self.right.append(self.left.pop())
            k -= 1
        return ''.join(self.left[max(-10, -len(self.left)):])
        
    def cursorRight(self, k: int) -> str:
        while k > 0 and self.right:
            self.left.append(self.right.pop())
            k -= 1
        return ''.join(self.left[max(-10, -len(self.left)):])

        
            

    
textEditor = TextEditor2()# // The current text is "|". (The '|' character represents the cursor)
textEditor.addText("leetcode")# // The current text is "leetcode|".
print(textEditor.deleteText(4))# // return 4
                        #   // The current text is "leet|". 
                        #   // 4 characters were deleted.
textEditor.addText("practice") # The current text is "leetpractice|". 
print(textEditor.cursorRight(3))# // return "etpractice"
                        #    // The current text is "leetpractice|". 
                        #    // The cursor cannot be moved beyond the actual text and thus did not move.
                        #    // "etpractice" is the last 10 characters to the left of the cursor.
print(textEditor.cursorLeft(8)) #/ return "leet"
                        #   // The current text is "leet|practice".
                        #   // "leet" is the last min(10, 4) = 4 characters to the left of the cursor.
print(textEditor.deleteText(10)) # return 4
                        #    // The current text is "|practice".
                        #    // Only 4 characters were deleted.
print(textEditor.cursorLeft(2))# // return ""
                        #   // The current text is "|practice".
                        #   // The cursor cannot be moved beyond the actual text and thus did not move. 
                        #   // "" is the last min(10, 0) = 0 characters to the left of the cursor.
print(textEditor.cursorRight(6)) # return "practi"
                        #    // The current text is "practi|ce".
                        #    // "practi" is the last min(10, 6) = 6 characters to the left of the cursor.