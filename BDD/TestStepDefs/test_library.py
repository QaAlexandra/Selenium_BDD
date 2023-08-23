from pytest_bdd import given, when,then, scenario, parsers, scenarios

from Pages import login_page, main_page, lib_page


scenarios('/home/alex/Profiscech/autotests/FrontPS/Features/library.feature')


# @scenario('User access libraly as normal user', 'Features/library.feature')
# def test_libraly(broweser):
#
#     global lib
#     lib = lib_page.LibraryClass(broweser)
#
#
#
# @given('User on the main page')
# def step_function(session: Session):
#     # Add Your Code Here
#     global lib
#     lib = lib_page.LibraryClass(broweser)
