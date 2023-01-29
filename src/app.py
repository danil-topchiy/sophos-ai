import logging
from slack_bolt import App
from slack_sdk.web import WebClient

import ssl as ssl_lib
import certifi

from message import Message
from answer_service import QuestionAnswerService

ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
app = App(ssl_check_enabled=False, url_verification_enabled=False)


def answer_question(user_id: str, channel: str, client: WebClient, question: str):
    answer = QuestionAnswerService.answer(question=question)
    message = Message(channel)
    message = message.get_message_payload(text=answer)

    # post message in slack
    response = client.chat_postMessage(**message)


@app.event("message")
def message(event, client):
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")
    return answer_question(user_id, channel_id, client, text)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.start(8000)
