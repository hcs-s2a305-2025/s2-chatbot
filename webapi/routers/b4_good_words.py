from fastapi import APIRouter
import random

router = APIRouter()


# 名言取得API
@router.get("/good_words/", tags=["good_words"], summary="名言取得API")
async def good_words():
    """
    名言をランダムに選んで返す API エンドポイント。
    Returns:
    dict: ランダムに選ばれた名言を含む辞書。{"result": "選ばれた名言"}
    
    Example:
    レスポンス:{"result": "夢は近づくと目標に変わる"}
    """
    choiceid = random.randint(1,8)

    if choiceid == 1:
        goodWord = "わが生涯に一片の悔いなし"
    elif choiceid == 2:
        goodWord = "あきらめたらそこで試合終了ですよ。"
    elif choiceid == 3:
        goodWord = "あまり強い言葉を遣うなよ\n弱く見えるぞ"
    elif choiceid == 4:
        goodWord = "だが断る"
    elif choiceid == 5:
        goodWord = "選択は2つだ。 \n必死に生きるか、\n必死に死ぬかだ。"
    elif choiceid == 6:
        goodWord = "俺か、俺以外か。"
    elif choiceid == 7:
        goodWord = "うちのコース４年に１回名前を\n書かなくて落ちるやつがいるんだよね。\nそのうちの一人が荒木先生。"
    elif choiceid == 8:
        goodWord = "エッッッッッッッッッド\n江戸（えど） は、東京の旧称であり、1603年から1867年まで\n江戸幕府が置かれていた都市である。現在の東京都区部に位置し、\nその前身及び原型に当たる。"
    else :
        goodWord = "うまくいきませんでした。"

    return {"result":goodWord}
