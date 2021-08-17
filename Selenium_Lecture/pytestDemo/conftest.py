# 특정 fixture가 여러 파일에 걸쳐서 실행된다고 하면 이 conftest.py 파일에 저장해놓고 쓰는 것이 좋음.
import pytest

# 여기서 scope를 설정하면 해당 fixture를 실행하는 단위를 제어할 수 있음.
@pytest.fixture(scope='module')
def setup():
    print("I will execute this first")
    yield  # 이 구문 앞의 항목은 함수 실행 전에. 그 다음 항목은 함수 실행 후에 실행됨. 
    print("I will execute this last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return {
        'first_name': "jinoh",
        "last_name": "kim"
    }

@pytest.fixture(params=["chrome", "firefox", "IE"])
def crossBrowser(request):
    return request.param
