import time
import pytest
date=time.strftime("%Y-%m-%d",time.localtime())

print(date)




@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")

def test_one():
    print("test_one")

def test_two():
    print("test_two")

if __name__ == '__main__':
    pytest.main()