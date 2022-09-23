class Solution(object):
    def fullJustify(self, words, maxWidth):
        
        res, curr, num_of_letters = [], [], 0
        
        for w in words:
            if num_of_letters + len(w) + len(curr) > maxWidth:
                num_of_spaces = maxWidth - num_of_letters
                words_amout = len(curr) - 1 or 1
                for i in range(num_of_spaces):
                    curr[i % words_amout] += ' '
                
                res.append(''.join(curr))
                curr, num_of_letters = [], 0
            curr += [w]
            num_of_letters += len(w)
        return res + [' '.join(curr).ljust(maxWidth)]
