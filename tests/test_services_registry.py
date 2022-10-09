import pytest
from unittest.mock import Mock
from src.services_registry.services_registry import Service, ServicesRegistry


@pytest.fixture
def services_registry():
    return ServicesRegistry()


def test_can_register_service(services_registry):
    # given
    mocked_service = Mock()
    # when
    services_registry.register_service(mocked_service)
    # then
    assert services_registry.get_service(mocked_service.__class__) == mocked_service


def test_can_register_service_of_some_type_only_once(services_registry):
    # given
    mocked_service = Mock()
    # when
    services_registry.register_service(mocked_service)
    # then
    with pytest.raises(ValueError):
        services_registry.register_service(mocked_service)


def test_registers_service_on_getting(services_registry):
    # given
    service = Service()
    # when
    services_registry.get_service(service.__class__)
    # then
    assert services_registry.get_service(service.__class__)
