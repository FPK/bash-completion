import pytest


class TestXrdb:
    @pytest.mark.complete("xrdb ")
    def test_1(self, completion):
        assert completion
