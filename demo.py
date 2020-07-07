import time
import pytest
date=time.strftime("%Y-%m-%d",time.localtime())

print(date)




@pytest.fixture(scope="session")
def open():
    print("打开浏览器")
    a=11
    yield a

def test_one(open):
    print(f"{open}test_one")

def test_two(open):
    print(f"{open}test_two")

if __name__ == '__main__':
    pytest.main('v')