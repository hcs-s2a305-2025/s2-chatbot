import requests
import random
import json

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
            self.hit_answer = random.randint(1,100)
            self.hit_count = 0
            self.status.hitgame_flg = True
            url = "http://127.0.0.1:8000/get_best_record/"
            res = requests.get(url)
            self.highscore = res.json()["result"]
            chat.set_replay_data(
                "1から100の数字を言ってね。\n何回で当たるかな～\n最高記録は{}回だよ。".format(self.highscore), image_idx=4
            )
        elif "ヒットブロー" in message:
            genList = list(range(10))
            randList = random.sample(genList, 4)
            self.hit_answer = "".join(map(str, randList))
            self.hit_count = 0
            self.status.hitblow_flg = True
            chat.set_replay_data(
                "4桁の数字(重複なし)を言ってね。\n何回で当たるかな～", image_idx=4
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
                "検索対象の郵便番号を\n入力してください。(ハイフンなし)"
            )
        elif "記録" in message:
            self.status.record_flg = True
            chat.set_replay_data(
                "記録したいメッセージを\n教えてください。",
                image_idx=6
            )
        elif "ログ出力" in message:
            url = "http://127.0.0.1:8000/log_output/"
            res = requests.get(url)
            result = res.json()["result"]
            replay_message = "".join(result)
            chat.set_replay_data(replay_message, image_idx=4, init_flg=True)
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
        image = 0
        inflg = False
        no = int(message)
        self.hit_count += 1
        url = "http://127.0.0.1:8000/hitgame/"
        param = {"answer": self.hit_answer, "no": no}
        res = requests.get(url, param)
        result = res.json()["result"]
        chat = Chat()

        if result == 1:
            replay_message1 = "すごく惜しいね。\nもう少し大きい値だよ。"
            image = 8
        elif result == 2:
            replay_message1 = "すごく惜しいね。\nもう少し小さい値だよ。"
            image = 8
        elif result == 3:
            replay_message1 = "あたりの数はもっと小さい値だよ。"
            image = 1
        elif result == 4:
            replay_message1 = "あたりの数はもっと大きい値だよ。"
            image = 2
        elif result == 0:
            replay_message1 = "せいか～い。\n {}回で正解だよ。また遊んでね。\n".format(self.hit_count)
            self.status.hitgame_flg = False
            inflg = True
            if int(self.hit_count) < int(self.highscore):
                self.hit_high_score(str(self.hit_count))
                replay_message1 += "最高記録更新！"
        else:
            self.hit_count -= 1
            replay_message1 = "うまくいきませんでした。もう一度"
            image = 5

        chat.set_replay_data(replay_message1, image_idx = image, init_flg= inflg)

        return chat

    def hit_high_score(self, score):
        url = "http://127.0.0.1:8000/put_best_record/"
        body = {"score": score}
        requests.put(url, json.dumps(body))

        return

    def hitblow_func(self, message):
        """ヒットブロー機能

        ヒットブローAPIを呼び出し、チャットの応答メッセージを作成する。
        計算処理が終わった場合は、計算クラスのインスタンス、機能実行状態の更新を行う。

        Args:
            message (str): 処理対象のメッセージ.

        Returns:
            Chat: チャットの応答情報

        """
        no = message
        self.hit_count += 1
        url = "http://127.0.0.1:8000/hit_blow/"
        param = {"answer": self.hit_answer, "number": no, "count":self.hit_count}
        res = requests.get(url, param)
        result = res.json()["result"]
        correct = res.json()["correct"]
        chat = Chat()

        if correct == 0:
            chat.set_replay_data(result, image_idx=8)
        elif correct == 1:
            self.status.hitblow_flg = False
            chat.set_replay_data(result, image_idx=7,init_flg=True)
        elif correct == 2:
            self.hit_count -= 1
            chat.set_replay_data(result, image_idx=2)

        return chat

    def zipcode_func(self, message):
        """郵便番号検索機能

        郵便番号APIを呼び出し、チャットの応答メッセージを作成する。
        計算処理が終わった場合は、計算クラスのインスタンス、機能実行状態の更新を行う。

        Args:
            message (str): 処理対象のメッセージ.

        Returns:
            Chat: チャットの応答情報

        """

        url = "http://127.0.0.1:8000/address/"
        param = {"code":message}
        res = requests.get(url, param)
        result = res.json()["result"]
        chat = Chat()

        chat.set_replay_data("住所は\n{}\nです。".format(result), image_idx=7, init_flg=True)

        return chat

    def record_func(self, message):
        url = "http://127.0.0.1:8000/log_record/"
        body = { "message": message }
        res = requests.post(url, json.dumps(body))
        result = res.json()["result"]
        chat = Chat()

        self.status.record_flg = False
        chat.set_replay_data(result, image_idx=7, init_flg=True)
        return chat
