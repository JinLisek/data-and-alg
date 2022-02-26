from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class VehicleElement(ABC):
    @abstractmethod
    def accept(self, visitor: VehicleElementVisitor) -> None:
        pass


class Engine(VehicleElement):
    def __init__(self, engine_type: str) -> None:
        self.__engine_type = engine_type

    def accept(self, visitor: VehicleElementVisitor) -> None:
        visitor.visit_engine(engine=self)

    def engine_type(self) -> str:
        return self.__engine_type


class Wheel(VehicleElement):
    def __init__(self, position: str) -> None:
        self.__position = position

    def accept(self, visitor: VehicleElementVisitor) -> None:
        visitor.visit_wheel(wheel=self)

    def position(self) -> str:
        return self.__position


class VehicleElementVisitor(ABC):
    @abstractmethod
    def visit_engine(self, engine: Engine) -> None:
        pass

    @abstractmethod
    def visit_wheel(self, wheel: Wheel) -> None:
        pass


class VehicleElementRepairVisitor(VehicleElementVisitor):
    def visit_engine(self, engine: Engine) -> None:
        print(f"Repairing {engine.engine_type()} engine")

    def visit_wheel(self, wheel: Wheel) -> None:
        print(f"Repairing {wheel.position()} wheel")


class VehicleElementLegalVisitor(VehicleElementVisitor):
    def visit_engine(self, engine: Engine) -> None:
        print(f"Checking if {engine.engine_type()} engine is legal in sports")

    def visit_wheel(self, wheel: Wheel) -> None:
        print(f"Checking if {wheel.position()} engine is legal in sports")


class Motorcycle:
    def __init__(self) -> None:
        self.__elements: List[VehicleElement] = [
            Wheel(position="front"),
            Wheel(position="back"),
            Engine(engine_type="electrical"),
        ]

    def visit(self, visitor: VehicleElementVisitor) -> None:
        for element in self.__elements:
            element.accept(visitor=visitor)


if __name__ == "__main__":
    vehicle = Motorcycle()

    vehicle.visit(visitor=VehicleElementRepairVisitor())

    print("=" * 100)

    vehicle.visit(visitor=VehicleElementLegalVisitor())
