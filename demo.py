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


def demo(*a,**b):
    print(a,b)

if __name__ == '__main__':
    # pytest.main('v')
    a=1
    b=2
    c=3
    d={'e':1,'f':2}
    demo(a,b,c,e=1,f=2)