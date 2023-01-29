class Message:

    def __init__(self, channel):
        self.channel = channel
        self.username = "sophus.ai"


    def get_message_payload(self, text: str):
        return {
            "ts": "",
            "channel": self.channel,
            "username": self.username,
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": text,
                    },
                }
            ],
        }
