#ABC038 D
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
inf = 10**12
dp = [inf]*N#初期化を忘れずに

def check(arg):
    # 条件を満たすかどうか？問題ごとに定義
    pass

def bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok