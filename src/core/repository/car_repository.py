from typing import List, Optional

# from sqlalchemy.orm.exc import NoResultFound

from src.application.interfaces.repository import (
    AddCarRepositoryInterface,
    ListCarsRepositoryInterface,
)

from src.domain.usecases import AddCarModel

from src.domain.schemas import Car

from src.core.database import DBConnection
from src.core.models import Car as CarEntity


class CarRepository(AddCarRepositoryInterface, ListCarsRepositoryInterface):
    """Class to manage Car Repository"""

    def add(self, car: AddCarModel) -> Car:
        """
        Insert data in Car entity
        :param - car: Add Car Model
        :return - tuple with new car inserted
        """

        with DBConnection() as db_connection:
            try:
                new_car = CarEntity(
                    color=car.color, model=car.model, owner_id=car.owner_id
                )
                db_connection.session.add(new_car)
                db_connection.session.commit()

                return Car(
                    id=new_car.id,
                    color=new_car.color,
                    model=new_car.model,
                    owner_id=new_car.owner_id,
                )
            except Exception:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    def list(self, limit: Optional[int] = 100, index: Optional[int] = 0) -> List[Car]:
        """
        list data in Car entity
        :param - limit: limit of entities
                - index: starting index offset
        :return - list of cars
        """

        with DBConnection() as db_connection:
            try:
                query = db_connection.session.query(CarEntity)

                # if name:
                #     query = query.filter_by(name=name)

                list_ = query.offset(index).limit(limit).all()

                return [
                    Car(
                        id=car.id,
                        color=car.color,
                        model=car.model,
                        owner_id=car.owner_id,
                    )
                    for car in list_
                ]
            except Exception:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
