# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result', [
    (2, -1, -2),
    pytest.param(3, 2, 1.5, marks=pytest.mark.smoke),
    pytest.param(1.5, 1.2, 1.25,  marks=pytest.mark.skip('bad test')),
], ids=["usual_test: 2 / -2 = -2", "smoke-test: 3 / 2 = 1.5", "skip-test 1.5 / 1.2 = 1.25"])
def test1(a, b, result):
    assert all_division(a, b) == result
