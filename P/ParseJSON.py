'''
-Medium-


Give below astring, which is similar to json, with multiple layers. Each next level will have two more empty spaces than the previous level.

 K1:V1
 K2:V2
 K3:
   K31:V31
   K32:
      K321:V321
      K322:V322
    K33:V33
 K4:
   K41:V41
   K42:V42

we need to build a data structure.
get(k1) returns v1
get(k2) returns v2
get(k3)(k31) returns v31.


'''

def convert_json(string_json:str):
    stack = []
    root = dict()
    prev_space = 0
    stack.append(root)
    for line in string_json.split("\n"):
        current_space = len(line) - len(line.lstrip(' '))
        if prev_space - current_space >= 2:
            stack.pop()
        parts = line.strip().split(":")
        if len(parts[1]) > 0:
            stack[-1][parts[0]] = parts[1]
        else:
            new_root = dict()
            stack[-1][parts[0]] = new_root
            stack.append(new_root)
        prev_space = current_space

    return root


if __name__ =='__main__':

    string_json = "K1:V1\n" +\
                "K2:V2\n" +\
                "K3:\n" +\
                "  K31:V31\n" +\
                "  K32:\n" +\
                "    K321:V321\n" +\
                "      K322:V322\n" +\
                "    K333:V333\n" +\
                "K4:\n" +\
                "  K41:V41\n" +\
                "  K42:V42"

    res = convert_json(string_json)
    
    print(res['K1'])    #V1
    print(res['K3']['K31']) #V31