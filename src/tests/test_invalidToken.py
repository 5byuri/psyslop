from invalidToken import invalidTokenCheck
import pytest

def test_invalidToken():
    assert invalidTokenCheck("src/tests/test_saved_cookies/emptyToken.txt") == False
    assert invalidTokenCheck("src/tests/test_saved_cookies/filledToken.txt") == True
