
from interface.interpack.testcase.mocketest import invoke_mock_request

# def test_mtorder(mocker):
#     mocker.patch('interface.interpack.testcase.mocketest.reqmeituan',return_value=200)
#     assert reqmeituan() ==200

def test_get_foo(mocker):
    mocker.patch('interface.interpack.testcase.mocketest.reqmeituan', return_value=200)
    assert invoke_mock_request() == 200