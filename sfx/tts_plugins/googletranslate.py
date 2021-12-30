import urllib


class GoogleTranslatePlugin:

    GOOGLE_TRANSLATE_BASE_URL = "https://translate.google.com/translate_tts"

    def __init__(self, voices, session):
        self.session = session
        self.voices = voices
        self.name = "Google Translate"
        self.limit = 200

    async def generate_url(self, voice: str, text: str):
        params = {
            "ie": "UTF-8",
            "client": "tw-ob",
            "tl": self.voices[voice]["apiName"],
            "q": text[: self.limit],
            "ttsspeed": "1",
            "total": "1",
            "idx": "0",
            "prev": "input",
            "textlen": len(text),
        }

        url = f"{self.GOOGLE_TRANSLATE_BASE_URL}?{urllib.parse.urlencode(params)}"
        return url
