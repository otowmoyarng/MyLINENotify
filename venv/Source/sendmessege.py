from settings import Settings
import requests


def SendMessege(message: str) -> None:
    """[summary]

    Args:
        message (str): 送信メッセージ
    """
    config = Settings()

    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + config.Token}
    try:
        requests.post(config.EntryPoint,
                    data=payload,
                    headers=headers)
    except Exception as e:
        raise e

if __name__ == '__main__':
    SendMessege("test send")
