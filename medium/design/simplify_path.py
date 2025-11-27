"""Return the simplified canonical path in linux"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        # i: complex unneeded path
        # o: simplified path

        # goal:
        # remove multiple //, handle single and double periods

        # remove /
        things = path.split('/')
        print(things)

        ans = []
        for item in things:
            if item != '' and item != '.':
                if item == '..':
                    if ans:
                        ans.pop() # go back 1 
                else:
                    ans.append(item)

        return "/" + "/".join(ans)