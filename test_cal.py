import cal

class TestCal:
    def test_add(self):
        assert 4 == cal.add(2,2)

    def test_sub(self):
        assert 5 == cal.sub(10,5)