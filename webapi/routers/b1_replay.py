from fastapi import APIRouter

router = APIRouter()

@router.get("/replay/", tags=["replay"])
async def replay(message: str):
    """
    与えられたメッセージに対する適切な返信を生成して返すAPIエンドポイント。

    Parameters:
    - message (str): ユーザーからの質問や挨拶などのメッセージ。

    Returns:
    dict: 生成された返信を含む辞書。{"result": "生成された返信のメッセージ", "image_idx": 画像のインデックス}

    Example:
    クエリパラメータ message="おはよう" に対してのリクエスト：
    レスポンス：{"result": "おはよう！！",image_idx": 1}

    """

    result = ""
    image_idx = 0

    message_list = {
        "名前":["飯野 和真です", 0],
        "おはよう":["おはよう!!", 7],
        "こんにちは":["こんにちは!!", 7],
        "やっぱりお前は":["うんこだなぁ", 9],
        "これって":["それってさぁ", 3],
        "見せてもらおうか":["連邦のモビルスーツの性能とやらを", 2],
        "りゅうじ":["信じてるからな", 7],
        "ジャパネット":["0120-441-222", 4],
        "やばい":["何してんの？", 8],
        "ああああ":["大丈夫そう？", 6]
    }


    if message in message_list:
        result = message_list[message][0]
        image_idx = message_list[message][1]
    else:
        result = "何言ってるか良くわからないなぁ"
        image_idx = 5

    return {
        "result": result, 
        "image_idx": image_idx
        }
