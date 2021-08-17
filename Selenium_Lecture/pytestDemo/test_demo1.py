# -v: more info metadata
# -s: logs in output
# -k: method names execution
# -m: test mark
import pytest

@pytest.mark.smoke
@pytest.mark.xfail
def test_prac1():
    print(1111)


@pytest.mark.smoke
@pytest.mark.xfail
def test_prac2():
    print(2222)
