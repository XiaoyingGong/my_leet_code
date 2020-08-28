# author: 龚潇颖(Xiaoying Gong)
# date： 2020/8/28 15:34  
# IDE：PyCharm 
# des:
# input(s)：
# output(s)：
from collections import Counter
class Solution:
    def judgeCircle(self, moves):
        y_count = 0
        x_count = 0
        for move in moves:
            if move == 'U':
                y_count += 1
            elif move == 'D':
                y_count -= 1
            elif move == 'L':
                x_count += 1
            else:
                x_count -= 1
        return True if x_count == 0 and y_count == 0 else False

    def judgeCircle_2(self, moves):
        x = Counter(moves)
        return True if x['U'] == x['D'] and x['L'] == x['R'] else False

    def judgeCircle_3(self, moves):
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

if __name__ == '__main__':
    moves = "UD"
    sol = Solution()
    print(sol.judgeCircle(moves))
    print(sol.judgeCircle_2(moves))
    print(sol.judgeCircle_3(moves))
