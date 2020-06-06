from main import create_token
from main import verify_signature


class TestChallenge4:

    payload = {"language": "Python"}

    secret = "acelera"

    token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
    token+= b'.eyJsYW5ndWFnZSI6IlB5dGhvbiJ9'
    token+= b'.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M'
    
    def test_create_token(self):
        assert (create_token(self.payload,
                             self.secret) == self.token), "Invalid Token!"

    def test_verify_signature(self):
        assert (verify_signature(self.token) == self.payload), {"error": 2}
