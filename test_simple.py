import random

import pytest

@pytest.fixture(scope="session")
def browser():
    print("Открытие")
    yield random.randint(0, 100)
    print("Закрытие")
@pytest.fixture
def get_admin(browser):
    return random.randint(0, 100)
@pytest.fixture()
def teardown():
    yield

def test_simple(get_admin, browser):
    print(browser)
    assert get_admin == 5, "Ожидаемый айди 5"
    assert 1 == 1, "Единица не должна быть равна двойкеpytest"

def test_another(browser, get_admin):
    print(browser)
    assert get_admin == 5
    assert 1 == 1, "Единица не должна быть равна двойкеpytest"


