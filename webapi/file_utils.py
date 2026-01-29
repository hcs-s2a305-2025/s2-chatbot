def file_append(file_path, value):
  """ファイル追記
  引数で指定されたファイルに引数で受け取った値を追記する。
  Attributes:
  file_path (str): 追記対象のファイルパス.
  value (str): 追記する値
  Raises:
  IOError: ファイルをほかのプロセスで使用している場合に発生
  """
  try :
    with open(file_path, mode='a', encoding='UTF-8') as f:
      f.write(value + "\n")
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
      try:
        lines = f.readlines()
        lines3 = lines[-3:]
      except IndexError as inerr:
        lines3 = ['失敗']
  except IOError as err:
    print(err)

  return lines3
