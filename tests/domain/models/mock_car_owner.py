from faker import Faker
from src.domain.schemas import CarOwner

faker = Faker()


def mock_car_owner() -> CarOwner:
    """Mocking Car Owner"""

    return CarOwner(id=faker.uuid4(), name=faker.name())
