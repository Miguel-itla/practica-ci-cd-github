
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert b'There is a error here' in response.data
