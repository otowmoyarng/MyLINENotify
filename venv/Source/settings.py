import json


class Settings:
    """[summary]
    setting.jsonを保持するデータクラス
    """
    token: str
    entryPoint: str

    def __init__(self, filename='setting.json'):
        """[summary]
        コンストラクタ
        setting.jsonを読み込む
        Args:
            filename (str, optional): ロードする設定ファイル. Defaults to 'setting.json'.
        """
        with open(filename) as f:
            settings = json.load(f)
            self.token = settings['LINENotify']['token']
            self.entryPoint = settings['LINENotify']['entryPoint']

    @property
    def Token(self) -> str:
        return self.token

    @property
    def EntryPoint(self) -> str:
        return self.entryPoint


if __name__ == "__main__":
    ins = Settings()
    print("Token:" + ins.Token)
    print("EntryPoint:" + ins.EntryPoint)
