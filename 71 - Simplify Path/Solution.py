#36ms, 13.8MB

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [x for x in path.split("/") if x != '']
        finals = []
        
        while stack:
            top = stack.pop()
            if top == '..':
                nRemoves = 1
                while nRemoves > 0 and stack:
                    nxt = stack.pop()
                    if nxt == '..':
                        nRemoves += 1
                    elif nxt == '.':
                        pass
                    else:
                        nRemoves -= 1
            elif top == '.':
                pass
            else:
                finals.insert(0,top)
        return "/" + "/".join(finals)