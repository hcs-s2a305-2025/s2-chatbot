from fastapi import APIRouter
import file_utils

router = APIRouter()


@router.get("/log_output/", tags=["log_output"], summary="記録メッセージ出力 API")
async def output():
  """
  ファイルに記録されているメッセージを返す API エンドポイント。

  Returns:
  dict: ファイルに記録されている最後の 3 つのメッセージを含む辞書。{"result": ["メッセージ 1",
  "メッセージ 2", "メッセージ 3"]}

  Example:
  レスポンス:{"result": ["メッセージ 1", "メッセージ 2", "メッセージ 3"]}
  """

  file_path = "./data/record.txt"

  lines = file_utils.file_readlines(file_path)

  try:
    result = lines[-3:]
  except IndexError as inderr:
    result = [inderr]

  return {'result': result}

