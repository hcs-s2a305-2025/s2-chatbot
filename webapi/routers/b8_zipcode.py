from fastapi import APIRouter
import requests

router = APIRouter()


# 郵便番号取得API
@router.get("/address/", tags=["address"], summary="郵便番号取得API")
async def get_address(code: str='0030806'):
    """
    指定された郵便番号に対応する住所を返す API エンドポイント。

    Parameters:
    - code (str): 検索対象の郵便番号。デフォルトは '0030806'。

    Returns:
    dict: 郵便番号に対応する住所を含む辞書。{"result": "検索結果の住所"}

    Example:
    クエリパラメータ code='1000001' に対してのリクエスト:
    レスポンス:{"result": "東京都千代田区千代田"}
    """

    url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode="

    try:
        response = requests.get(url + code)
        response.raise_for_status()
        data = response.json()

        if data["results"] is None:
            print(f"郵便番号 {code} は見つかりませんでした。")
            result = "見つかりませんでした。"
            return {"result": result}
        
        address_info = data["results"][0]

        pref = address_info["address1"]  # 都道府県
        city = address_info["address2"]  # 市区町村
        town = address_info["address3"]  # 町域

        print(f"郵便番号: {code}")
        print(f"住所: {pref}{city}{town}")

        result = str(pref) + str(city) + str(town)

    except requests.exceptions.RequestException as e:
        print(f"エラーが発生しました: {e}")

    return {"result": result}
