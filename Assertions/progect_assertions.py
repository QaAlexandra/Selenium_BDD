import pytest

def element_is_displayed(element):

    if element.is_enabled() is True:
        print(f"Test Passed {element} is displayed")
    else:
        pytest.raises(FileNotFoundError)
        print(f"Don't found {element}")