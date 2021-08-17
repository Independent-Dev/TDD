import pytest

# 여기서 setup은 pytest에서 자동으로 찾아서 세팅해줌.
def test_fixture_demo(setup):
    print("I will execute steps in fixtureDemo method")

# 클래스 내의 모든 method에 fixture를 적용하고 싶은 경우
@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixture_demo1(self):
        print("I will execute steps in fixtureDemo1 method")

    def test_fixture_demo2(self):
        print("I will execute steps in fixtureDemo2 method")

    def test_fixture_demo3(self):
        print("I will execute steps in fixtureDemo3 method")

