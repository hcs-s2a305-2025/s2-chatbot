import requests
import random

from chat import Chat
from status import FuncStatus


class ChatLogic:
    """チャットロジッククラス

    チャットコントロールから呼び出され、チャットの各機能を実行する。

    Attributes:
        calc(:obj:Calc): 計算機能
        status(:obj:FuncStatus): 機能継続状態管理
    """

    def __init__(self):
        self.status = FuncStatus()
        # TODO 入力パラメータの追加
        self.x = None
        self.y = None

    def replay(self, message):
        """チャットの応答

        引数で受け取ったmessageにしたがって、戻り値を返す。
        処理の継続が必要な機能の場合は、機能実行状態の更新を行う。

        Args:
            message (str): 処理対象のメッセージ.

        Returns:
            obj:Chat: チャットの応答情報

        """

        chat = Chat()  # 返答用オブジェクト
        # TODO メッセージ分岐（チャット拡張エリア）
        if "足し算" in message:
            self.x, self.y = (None, None)
            self.status.calc_flg = True
            chat.set_replay_data("足したい値は？")
        elif "給料計算" in message:
            self.x, self.y = (None, None)
            self.status.payroll_flg = True
            chat.set_replay_data("時給は？")
        elif "割り勘" in message:
            self.x, self.y = (None, None)
            self.status.dutch_treat_flg = True
            chat.set_replay_data("合計金額は？")
        elif "名言" in message:
            chat = Chat()
            url = "http://127.0.0.1:8000/good_words/"
            res = requests.get(url)
            result = res.json()["result"]
            chat.set_replay_data(result, image_idx=7, init_flg=True)
            return chat
        elif "おみくじ" in message:
            chat = Chat()
            url = "http://127.0.0.1:8000/omikuji/"
            res = requests.get(url)
            result = res.json()["result"]
            image_idx = res.json()["img_idx"]
            chat.set_replay_data(result, image_idx, init_flg=True)
            return chat
        elif "数当て" in message:
            self.hit_answer = random.randint(1, 100)
            self.hit_count = 0
            self.status.hitgame_flg = True
            chat.set_replay_data(
                "1から100の数字を言ってね。\n何回で当たるかな。", image_idx=4
            )
        elif "何時" in message:
            chat = Chat()
            url = "http://127.0.0.1:8000/get_datetime/"
            res = requests.get(url)
            result = res.json()["result"]
            chat.set_replay_data(str(result) + "だよ", image_idx=7, init_flg=True)
            return chat
        elif "郵便番号" in message:
            self.status.zipcode_flg = True
            chat.set_replay_data(
                "検索対象の郵便番号を入力してください。\n（ハイフンなし）"
            )
        elif "追加する機能の処理メッセージ" in message:
            pass
        else:
            # WebAPIリクエストURI
            url = "http://127.0.0.1:8000/replay/"
            param = {"message": message}
            res = requests.get(url, param)
            replay_message = res.json()["result"]
            image_idx = res.json()["image_idx"]
            chat.set_replay_data(replay_message, image_idx, True)

        return chat

    def calc_func(self, message):
        """計算機能

        足し算APIを呼び出し、チャットの応答メッセージを作成する。
        計算処理が終わった場合は、計算クラスのインスタンス、機能実行状態の更新を行う。

        Args:
            message (str): 処理対象のメッセージ.

        Returns:
            Chat: チャットの応答情報

        """
        chat = Chat()
        if self.x == None:
            replay_message1 = "もう一つの値は？"
            self.x = int(message)
            chat.set_replay_data(replay_message1)
        else:
            self.y = int(message)
            url = "http://127.0.0.1:8000/add/"
            param = {"x": self.x, "y": self.y}
            res = requests.get(url, param)
            result = res.json()["result"]
            replay_message2 = "合計は、{0}です。"
            self.status.calc_flg = False
            chat.set_replay_data(
                replay_message2.format(result), image_idx=7, init_flg=True
            )
        return chat

    def payroll_func(self, message):
        """給料計算機能

        給料計算APIを呼び出し、チャットの応答メッセージを作成する。
        計算処理が終わった場合は、計算クラスのインスタンス、機能実行状態の更新を行う。

        Args:
            message (str): 処理対象のメッセージ.

        Returns:
            Chat: チャットの応答情報

        """
        chat = Chat()
        if self.x == None:
            replay_message1 = "何時間働いた？"
            self.x = int(message)
            chat.set_replay_data(replay_message1)
        else:
            self.y = int(message)
            url = "http://127.0.0.1:8000/payroll/"
            param = {"x": self.x, "y": self.y}
            res = requests.get(url, param)
            result = res.json()["result"]
            replay_message2 = "給料は、{0}円です。"
            self.status.payroll_flg = False
            chat.set_replay_data(
                replay_message2.format(result), image_idx=7, init_flg=True
            )
        return chat

    def dutch_treat_func(self, message):
        """割り勘機能

        割り勘APIを呼び出し、チャットの応答メッセージを作成する。
        計算処理が終わった場合は、計算クラスのインスタンス、機能実行状態の更新を行う。

        Args:
            message (str): 処理対象のメッセージ.

        Returns:
            Chat: チャットの応答情報

        """
        chat = Chat()
        if self.x == None:
            replay_message1 = "何人？"
            self.x = int(message)
            chat.set_replay_data(replay_message1)
        else:
            self.y = int(message)
            url = "http://127.0.0.1:8000/dutch_treat/"
            param = {"x": self.x, "y": self.y}
            res = requests.get(url, param)
            result = res.json()["result"]
            diff = res.json()["diff"]
            replay_message2 = "じゃんけんで負けた人は{}円。\nそれ以外の人は{}円だよ。"
            self.status.dutch_treat_flg = False
            chat.set_replay_data(
                replay_message2.format(diff, result), image_idx=7, init_flg=True
            )
        return chat

    def hitgame_func(self, message):
        """数当て機能

        数当てAPIを呼び出し、チャットの応答メッセージを作成する。
        計算処理が終わった場合は、計算クラスのインスタンス、機能実行状態の更新を行う。

        Args:
            message (str): 処理対象のメッセージ.

        Returns:
            Chat: チャットの応答情報

        """
        no = message
        self.hit_count += 1
        url = "http://127.0.0.1:8000/hitgame/"
        param = {"answer": self.hit_answer, "no": no}
        res = requests.get(url, param)
        result = res.json()["result"]
        chat = Chat()

        if result == 1:
            replay_message1 = "すごく惜しいね。\nもう少し大きい値だよ。"
            chat.set_replay_data(replay_message1, image_idx=8)
        elif result == 2:
            replay_message1 = "すごく惜しいね。\nもう少し小さい値だよ。"
            chat.set_replay_data(replay_message1, image_idx=8)
        elif result == 3:
            replay_message1 = "あたりの数はもっと小さい値だよ。"
            chat.set_replay_data(replay_message1, image_idx=1)
        elif result == 4:
            replay_message1 = "あたりの数はもっと大きい値だよ。"
            chat.set_replay_data(replay_message1, image_idx=2)
        elif result == 0:
            replay_message1 = "せいか～い。\n{}回で正解だよ。\nまた遊んでね。"
            self.status.hitgame_flg = False
            chat.set_replay_data(
                replay_message1.format(self.hit_count), image_idx=3, init_flg=True
            )
        else:
            self.hit_count -= 1
            chat.set_replay_data("うまくいきませんでした。もう一度", image_idx=5)
        return chat

    def zipcode_func(self, message):
        """数当て機能

        数当てAPIを呼び出し、チャットの応答メッセージを作成する。
        計算処理が終わった場合は、計算クラスのインスタンス、機能実行状態の更新を行う。

        Args:
            message (str): 処理対象のメッセージ.

        Returns:
            Chat: チャットの応答情報

        """
        no = message
        self.hit_count += 1
        url = "http://127.0.0.1:8000/hitgame/"
        param = {"answer": self.hit_answer, "no": no}
        res = requests.get(url, param)
        result = res.json()["result"]
        chat = Chat()

        if result == 1:
            replay_message1 = "すごく惜しいね。\nもう少し大きい値だよ。"
            chat.set_replay_data(replay_message1, image_idx=8)
        elif result == 2:
            replay_message1 = "すごく惜しいね。\nもう少し小さい値だよ。"
            chat.set_replay_data(replay_message1, image_idx=8)
        elif result == 3:
            replay_message1 = "あたりの数はもっと小さい値だよ。"
            chat.set_replay_data(replay_message1, image_idx=1)
        elif result == 4:
            replay_message1 = "あたりの数はもっと大きい値だよ。"
            chat.set_replay_data(replay_message1, image_idx=2)
        elif result == 0:
            replay_message1 = "せいか～い。\n{}回で正解だよ。\nまた遊んでね。"
            self.status.hitgame_flg = False
            chat.set_replay_data(
                replay_message1.format(self.hit_count), image_idx=3, init_flg=True
            )
        else:
            self.hit_count -= 1
            chat.set_replay_data("うまくいきませんでした。もう一度", image_idx=5)
        return chat
