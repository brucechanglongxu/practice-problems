   def solveNQueens(self, n):
        
        def recurse(queens, xy_dif, xy_sum):
            # check if we places all queens
            p = len(queens)
            if p == n: 
                result.append(queens)
            else:
              # let's check all available variants
              for q in xrange(n):
                  # if we have not checked all variants - give it a shot
                  if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                      recurse(queens + [q], xy_dif + [p-q], xy_sum + [p + q])
        
        result = []
        
        recurse([],[],[])
        
        return [["." * i + "Q" +"." * (n - i - 1) for i in res] for res in result]
