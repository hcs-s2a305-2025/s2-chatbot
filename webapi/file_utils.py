def file_append(file_path, value, mode):
  """ファイル追記
  引数で指定されたファイルに引数で受け取った値を追記する。
  Attributes:
  file_path (str): 追記対象のファイルパス.
  value (str): 追記する値
  Raises:
  IOError: ファイルをほかのプロセスで使用している場合に発生
  """
  try :
    with open(file_path, mode, encoding='UTF-8') as f:
      f.write(value)
  except IOError as err:
    print(err)


def file_readlines(file_path):
  """ファイル読み込み
  指定されたファイルパスのテキストファイルを読み込み、行ごとのリストを返します。

  Attributes:
  file_path (str): 読み込むファイルのパス

  Returns:
  list: ファイルの各行を要素とするリスト

  Raises:
  IOError: ファイルの読み込みエラーが発生した場合に発生します。
  """

  try:
    with open(file_path, mode='r', encoding='UTF-8') as f:
      lines = f.readlines()
  except IOError as err:
    print(err)

  return lines


def file_read(file_path):
    """ファイル読み込み
  引数で指定されたファイルをオープンし内容を読み込み、結果を返す。
  Attributes:
  file_path (str): 読み込み対象のファイルパス.
  Returns:
  str: ファイルから読み込んだ内容
  Raises:
  IOError: ファイルが存在しない場合に発生
  """ 
    try:
        with open(file_path, mode="r", encoding="UTF-8") as f:
            highscore = f.readline().strip()
    except IOError as err:
        print(err)

    return highscore

def json_file_read(self, file_path):
  """JSON 形式のファイル読み込み
  引数で指定された JSON 形式のファイルをオープンし内容を読み込む。
  Args:
  file_path (str): 読み込み対象のファイルパス.
  Returns:
  str: ファイルから読み込んだ内容
  Raises:
  IOError: ファイルが存在しない場合に発生
  JSONDEcodeError: データが 0 件の時に read すると発生
  """
