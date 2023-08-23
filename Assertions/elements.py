from Library.config_reader import read_assertion_data


def assert_h3(h3_list_resp):
    h3_list_assert = read_assertion_data("lib_page", "h3").split()
    h3 = [_.text for _ in h3_list_resp]

    assert h3_list_assert.sort() == h3.sort()
