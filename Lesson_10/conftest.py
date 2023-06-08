import pytest
from datetime import datetime as dt


@pytest.fixture(scope='class')
def start_stop_time(request):
    """Фикстура для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания"""
    print(f'Время начала тестов {request.node.name}: {dt.now()}')
    yield None
    print(f'\nВремя окончания тестов {request.node.name}: {dt.now()}')


@pytest.fixture()
def time_count(request):
    """Фикстура для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста"""
    start = dt.now()
    print()
    yield None
    print(f' - Время выполнения теста {request.node.name}: {dt.now() - start}')
