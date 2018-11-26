import sys
import itertools

INS = 1
DEL = 1
SUB = 2

def edit_distance(src, dst):
    dp = [[float('inf') for i in range(1+len(dst))] for j in range(1+len(src))]
    for i in range(1+len(dst)):
        dp[0][i] = i

    for j in range(1+len(src)):
        dp[j][0] = j

    for i, j in itertools.product(range(1, 1+len(src)), range(1, 1+len(dst))):
        dp[i][j] = min(
            dp[i-1][j] + INS,
            dp[i][j-1] + DEL,
            dp[i-1][j-1] if src[i-1] == dst[j-1] else dp[i-1][j-1] + SUB
        )

    return dp[len(src)][len(dst)]


def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        src, dst = line.split(" ")
        print('src: {}, dst: {}'.format(src, dst))
        distance = edit_distance(src, dst)
        print('\tdistance: {}'.format( distance))

if __name__ == '__main__':
    main()
