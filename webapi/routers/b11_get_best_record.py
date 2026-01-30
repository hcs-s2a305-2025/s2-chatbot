from fastapi import APIRouter
import file_utils

router = APIRouter()

@router.get("/get_best_record/", tags=["get_best_record"], summary="数あて最高記録取得 API")
async def get_best_record():
    """
  数あてゲームの最高記録を返す API エンドポイント。
  Returns:
  dict: 数あてゲームの最高記録を含む辞書。{"result": 最高記録}
  Example:
  レスポンス:{"result": 99999}
  """

    file_path = "./data/hitgame.txt"

    result = file_utils.file_read(file_path)

    return {'result': result}
