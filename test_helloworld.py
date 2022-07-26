from myhelloworld import say_hello

def test_helloworld_no_params():
    print(say_hello())
    assert say_hello() == "Hello, World!"


def test_helloworld_with_param():
    print(say_hello("shahzad"))
    assert say_hello("Everyone") == "Hello, Everyone!"
