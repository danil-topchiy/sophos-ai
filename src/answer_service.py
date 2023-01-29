import openai

# openai.api_key = 


class QuestionAnswerService:

    BASE_PROMPT = (
        'You are company\'s internal AI assistant '
        'made to answer any questions from employees '
        'taking into account only the information you have in context '
        'if you don\'''t find the answer - apologise and say that you don\'''t have the answer '
        'context: {context}'
        'question: {question}'
    )

    @classmethod
    def answer(cls, question: str) -> str:
        # TODO: add context from search
        context = "Context about current company"
        prompt = cls.BASE_PROMPT.format(context=context, question=question)
        completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1000)
        return completion.choices[0].text.strip()
