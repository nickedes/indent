from indent import indentation


class TestClass:

    def test_count(self):
        assert indentation('str', '$', 0) == 'str'

    def test_indent(self):
        assert indentation('str\nhi', '$', 1) == '$str\n$hi'

    def test_default_count(self):
        assert indentation('hey\nsup', ' ') == ' hey\n sup'
