from fastapi import APIRouter

router = APIRouter()


# 給料計算API
@router.get("/payroll/", tags=["payroll"], summary="給料計算API")
async def payroll(x: int = 0, y: int = 0):
    """
    指定された労働時間と時給から給料を計算して返す API エンドポイント。

    Parameters:
    - x (int): 労働時間(時間単位)を表す整数
    - y (int): 時給を表す整数
    Returns:
    dict: 計算された給料を含む辞書。{"result": x * y}
    Example:
    クエリパラメータ x=40, y=1000 に対してのリクエスト:
    レスポンス:{"result": 40000}
    """
    return {"result": x * y}
