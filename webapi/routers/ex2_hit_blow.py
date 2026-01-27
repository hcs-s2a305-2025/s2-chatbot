from fastapi import APIRouter

router = APIRouter()


# 数当てAPI
from fastapi import APIRouter

router = APIRouter()


# 数当てAPI
@router.get("/hit_blow/", tags=["hit_blow"], summary="Hit & Blow ゲームAPI")
async def play_hit_blow(number: str,answer: str, count: int):
  """
  4 桁の数字を用いた Hit & Blow ゲームの判定結果を返す API エンドポイント。
  Parameters:
  - number (str): プレイヤーが予想する 4 桁の数字。
  - answer (str): 正解となる 4 桁の数字。
  Returns:
  dict: Hit & Blow ゲームの結果を含む辞書。{"hit": ヒット数, "blow": ブ
  ロー数}
  Example:
  クエリパラメータ number="1234", answer="1243" に対してのリクエスト:
  レスポンス:{"hit": 2, "blow": 2}
  """
  correct = 0
  hitcount = 0
  blowcount = 0
  sameflg = True

  if len(number) != 4:
    sameflg = False
  else:
    for i in range(4):
      for j in range(4):
        if i == j:
          continue
        elif number[i] == number[j]:
          sameflg = False
        else:
          continue
  
  if sameflg:
    for i in range(4):
      if answer[i] == number[i]:
        hitcount += 1
      else:
        for j in range(4):
          if answer[i] == number[j]:
            blowcount += 1
  
  if hitcount == 4:
    correct = 1
    result = "せいか～い\n{}回で当たったよ。\nまた遊んでね。".format(count)
  elif sameflg == False :
    correct == 2
    result = "重複のない4桁の数字を入力してね。"
  else:
    correct = 0
    result = "ヒット{}&ブロー{}だよ".format(hitcount,blowcount)

  return {"result": result, "correct": correct}
