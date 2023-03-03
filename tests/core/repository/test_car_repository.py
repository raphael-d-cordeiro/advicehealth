import random

from faker import Faker

from tests.core.repository import CarOwnerRepositorySpy
from tests.core.repository import CarRepositorySpy

from src.domain.usecases import AddCarModel, AddCarOwnerModel
from src.domain.schemas import CarColor, CarModel

faker = Faker()
car_repository = CarRepositorySpy()
car_owner_repository = CarOwnerRepositorySpy()


def test_add_car_must_success():
    """Must successfully add a new valid car owner"""

    color = random.choice(list(CarColor))
    model = random.choice(list(CarModel))

    owner_name = faker.name()
    owner = car_owner_repository.add(AddCarOwnerModel(name=owner_name))

    new_car = AddCarModel(color=color, model=model, owner_id=owner.id)

    response = car_repository.add(new_car)

    assert new_car.color.value == response.color.value
    assert new_car.model.value == response.model.value
    assert new_car.owner_id == response.owner_id


# def test_list_car_owner_must_success():
#     """Must successfully list car owners"""

#     limit = faker.random_int(1, 100)
#     index = 0

#     response = car_owner_repository.list(limit=limit, index=index)

#     assert isinstance(response, list)
