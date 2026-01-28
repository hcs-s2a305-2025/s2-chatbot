def file_append(file_path, value):
  """ファイル追記
  引数で指定されたファイルに引数で受け取った値を追記する。
  Attributes:
  file_path (str): 追記対象のファイルパス.
  value (str): 追記する値
  Raises:
  IOError: ファイルをほかのプロセスで使用している場合に発生
  """

  with open(file_path, 'a', encoding='UTF-8') as f:
    f.write(value)

  f.close
