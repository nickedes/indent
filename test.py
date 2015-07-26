from indent import indentation


class TestClass:
    def test_count(self):
        assert indentation('str', '$', 0) == 'str'
