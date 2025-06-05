class Solution:
    def reverseWords(self, s: str) -> str:
        # ec: 1 word, no space cases

        res = []
        ind_of_space = 0
        while True:
            if ' ' in s:
                ind_of_space = s.index(' ')
            else:
                # if reached end of string
                if len(s) == 0:
                    break

                curr_string = s[0:]
                res.append(curr_string.strip())
                break
            curr_string = s[0:ind_of_space]

            # don't add single spaces
            # str[0:0] returns ''
            if ind_of_space != 0:
                res.append(curr_string.strip())
            s = s[ind_of_space+1:]
        
        # construct resulting string
        res.reverse()
        res_str = ""
        for k in range(len(res)):
            res_str += res[k]
            if k != len(res) -1:
                res_str += " "

        return res_str