from fastapi import APIRouter

router = APIRouter()


# 割り勘API
@router.get("/dutch_treat/", tags=["dutch_treat"], summary="割り勘API")
async def dutch_treat(x: int = 0, y: int = 0):
    """
    指定された金額を指定された人数で均等に割り勘する API エンドポイント。
    Parameters:
    - x (int): 合計金額。
    - y (int): 人数。
    Returns:
    dict: 均等に割り勘した金額と余りを含む辞書。{"result": 0, "diff": 0}
    Example:
    リクエスト:
    /dutch_treat/?x=1000&y=3
    レスポンス:{"result": 330, "diff": 10}
    """
    return {"result": x // y, "diff" : x // y + x % y}
