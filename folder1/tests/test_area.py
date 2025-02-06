from source import area
import pytest
import sys

# print(sys.version_info[0])
class TestArea:
    def test_square(self):
        assert area.square(4) == 18, "Value should be 18 but it is not"

    def test_rectangle(self):
        assert area.rectangle(8, 9) == 72

# Skip the test
    @pytest.mark.skip(reason = "I don't want to do this test")
    def test_skip(self):
        assert True

    @pytest.mark.skipif(sys.version_info[0] >= (3), reason = "Skip if version > 3.5")
    def test_skip_v3(self):
        assert True

# Run test based on name
# to run all tests that have windows in name, give `pytest -k windows`
    def test_windows_1(self):
        assert True

    def test_windows_2(self):
        assert True
# 
    def test_linux_1(self):
        assert True

    def test_linux_2(self):
        assert True


# In case of many functions that fall under a category, instead of putting the name in each of the test, 
# Use tags

    @pytest.mark.wind
    def test_windows(self):
        assert True
    
    @pytest.mark.lin
    def test_linux(self):
        assert True
        

# Exception matching.
    def test_division_error(self):
        with pytest.raises(ZeroDivisionError):
            1/0

# The below test will pass since notimplemented error is a subclass fo runtime error.
    def test_runtime_error(self):
        def foo():
            raise NotImplementedError
        with pytest.raises(RuntimeError) as excinfo:
            foo()

# The below test will fail since eventhough notimplemented error is a subclass fo runtime error, the assertion fails
    def test_runtime1_error(self):
        def foo():
            raise NotImplementedError
        with pytest.raises(RuntimeError) as excinfo:
            foo()

        assert excinfo.type is RuntimeError

        