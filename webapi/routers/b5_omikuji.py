from fastapi import APIRouter
import random

router = APIRouter()


# おみくじAPI
@router.get("/omikuji/", tags=["omikuji"], summary="おみくじAPI")
async def omikuji():
    """
    おみくじの結果をランダムに返す API エンドポイント。

    Returns:
    dict: おみくじの結果と結びつく画像のインデックスを含む辞書。
    {"result": "おみくじの結果", "image_idx": 画像のインデックス}

    Example:
    レスポンス:{"result": "大吉", "image_idx": 1}
    """
    choiceid = random.randint(1, 100)

    if choiceid > 90:
        result = "大吉"
        img = 4
    elif choiceid > 70:
        result = "中吉"
        img = 3
    elif choiceid > 40:
        result = "吉"
        img = 7
    elif choiceid > 10:
        result = "末吉"
        img = 1
    elif choiceid > 0:
        result = "凶"
        img = 2
    else:
        result = "大凶"
        img = 8

    return {"result": result, "img_idx": img}
