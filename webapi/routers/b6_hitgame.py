from fastapi import APIRouter

router = APIRouter()


# 数当てAPI
@router.get("/hitgame/", tags=["hitgame"], summary="数当てAPI")
async def play_hit_game(answer: int, no: int):
    """
    指定された answer と no の当たり判定結果を返す API エンドポイント。

    Parameters:
    - answer (int): 当たりの数値。
    - no (int): 判定対象の数値。

    Returns:
    dict: 当たり判定の結果を含む辞書。{"result": 結果コード}

    Result Codes:
    - 0: 完全一致(当たり)
    - 1: 近似値(±2 の範囲内)
    - 2: 判定対象の数値が、当たりより小さい
    - 3: 判定対象の数値が、当たりより大きい

    Example:
    クエリパラメータ answer=5, no=5 に対してのリクエスト:
    レスポンス:{"result": 0}
    """
    sa = answer - no

    if sa == 0:
        result = 0
    elif 2 >= sa > 0 :
        result = 1
    elif -2 <= sa < 0:
        result = 2
    elif answer < no:
        result = 3
    elif answer > no:
        result = 4
    else:
        result = 5


    return {"result": result}
