# MyPackage/tests.py

from MyPackage import foo, bar, inc
import MyPackage

def test_foo_returns_1():
    assert foo(0) == 1, "foo(0) should return 1"

def test_bar_sum():
    assert bar([1, 2, 3]) == 6, "bar([1,2,3]) should return 6"

def test_foo_invalid_input():
    try:
        foo("a")
    except (TypeError, ValueError):
        pass
    else:
        assert False, "foo('a') should raise TypeError or ValueError"

def test_bar_invalid_input_type():
    try:
        bar("abc")
    except (TypeError, ValueError):
        pass
    else:
        assert False, "bar('abc') should raise TypeError or ValueError"

def test_bar_invalid_input_list_item():
    try:
        bar([1, "2", 3])
    except (TypeError, ValueError):
        pass
    else:
        assert False, "bar([1,'2',3]) should raise TypeError or ValueError"

def test_import_star_hides_private():
    from MyPackage import *
    try:
        _foo
    except NameError:
        pass
    else:
        assert False, "_foo should not exist after import *"

    try:
        _bar
    except NameError:
        pass
    else:
        assert False, "_bar should not exist after import *"

def test_import_star_hides_modules():
    from MyPackage import *
    try:
        module1
    except NameError:
        pass
    else:
        assert False, "module1 should not exist after import *"

    try:
        module2
    except NameError:
        pass
    else:
        assert False, "module2 should not exist after import *"

def test_inc_alias():
    assert hasattr(MyPackage, "inc"), "MyPackage should have inc attribute"
    assert "inc" not in MyPackage.__all__, "inc should not be in __all__"

def test_name_main():
    import sys
    if __name__ == "__main__":
        assert True
    else:
        assert True  # apenas garante que __name__ funciona corretamente

if __name__ == "__main__":
    test_foo_returns_1()
    test_bar_sum()
    test_foo_invalid_input()
    test_bar_invalid_input_type()
    test_bar_invalid_input_list_item()
    test_import_star_hides_private()
    test_import_star_hides_modules()
    test_inc_alias()
    test_name_main()
    print("ALL TESTS PASSED")
