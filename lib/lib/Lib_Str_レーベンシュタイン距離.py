#title#
# レーベンシュタイン距離
#subtitle#
# Levenshtein: 削除・挿入・変更により文字列を一致させる最小の手順回数

#name#
# レーベンシュタイン距離
#description#
# Lib_レーベンシュタイン距離
#body#
#####################################
# レーベンシュタイン距離 文字列の近似度
# 文字削除・挿入・変更により文字列を一致させる最小の手順回数
#####################################
# https://algo-method.com/tasks/315
# https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_E

class Levenshtein:
    def __init__(self, S, T) -> None:
        self.Type = type(S)
        if self.Type == str:
            S = list(S)
            T = list(T)
        self.S = S
        self.T = T
        self.ls = len(S)
        self.lt = len(T)
        self.dp = [[10**10]*(self.lt+1) for _ in range(self.ls+1)]
        dp = self.dp
        for i in range(self.ls):
            dp[i][0] = i
        for j in range(self.lt):
            dp[0][j] = j
        for i in range(self.ls):
            for j in range(self.lt):
                if S[i] == T[j]:
                    dp[i+1][j+1] = min(dp[i][j]  , dp[i+1][j]+1, dp[i][j+1]+1)
                else:
                    dp[i+1][j+1] = min(dp[i][j]+1, dp[i+1][j]+1, dp[i][j+1]+1)
        self.length = self.dp[self.ls][self.lt]


    def restore(self):
        # 復元
        ret = []
        i, j = self.ls, self.lt
        dp = self.dp
        while i and j:
            # (i-1, j) -> (i, j) と更新されていた場合
            if dp[i][j] == dp[i-1][j]:
                i-=1   # DP の遷移を遡る
            # (i, j-1) -> (i, j) と更新されていた場合
            elif dp[i][j] == dp[i][j-1]:
                j-=1   # DP の遷移を遡る
            # (i-1, j-1) -> (i, j) と更新されていた場合
            else:
                ret.append(self.S[i-1])
                # このとき s[i-1] == t[j-1] なので、t[j-1] + res でも OK
                i-=1
                j-=1   # DP の遷移を遡る
        ret = ret[::-1]
        if self.Type == str: ret = ''.join(ret)
        return ret


#####################

s = input()
t = input()

ldiff = Levenshtein(s, t)
print(ldiff.length)

#prefix#
# Lib_Str_レーベンシュタイン距離_Levenshtein_distance#
#end#
