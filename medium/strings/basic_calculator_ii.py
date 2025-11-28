import math
class Solution:
    def calculate(self, s: str) -> int:
        # i: valid expression
        # o: evaluate expression
        # +-*/

        # replace spaces
        s = s.replace(" ", "")

        # evaluate divide/multi immediately
        # , push addition/subtraction on stack
        # keep track of previous operator
        st = []
        i = 0
        prev_op = '+'
        while i < len(s):
            num = ""
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1

            # based on last operator, do logic
            if prev_op == '-':
                st.append(-1 * int(num))
            elif prev_op == '+':
                st.append(int(num))
            elif prev_op == '/':
                t = st.pop()
                st.append(math.trunc(t / int(num)))
            elif prev_op == '*':
                t = st.pop()
                st.append(t * int(num))
            
            # read operator now
            if i < len(s):
                prev_op = s[i]
                i += 1
        
            # print(st)


        return sum(st)
        