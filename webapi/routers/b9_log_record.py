from fastapi import APIRouter
from pydantic import BaseModel
import requests
import file_utils

router = APIRouter()


class Item(BaseModel):
    message: str


@router.post("/log_record/", tags=["log_record"], summary="メッセージ記録 API")
async def record(item: Item):
    """
  送られてきたメッセージをファイルに保存する API エンドポイント。

  Parameters:
  - item (Item): 保存するメッセージを含むデータクラス。

  Returns:
  dict: 保存が成功した旨の結果を含む辞書。{"result": "保存しました"}

  Example:
  """

    file_utils.file_append("./data/record.txt", item)

    return {"result": "保存しました。"}
