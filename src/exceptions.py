class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""


class SessionResponseIsNone(Exception):
    """Вызывается, когда не получен ответ по URL"""

    def __init__(self, url, message='Не получен ответ по URL: '):
        self.url = url
        self.message = message + url
        super().__init__(self.message)
