from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, Optional, TypeVar

T = TypeVar("T")
Output = TypeVar("Output")


class Maybe(Generic[T]):
    def __init__(self, value: Optional[T]) -> None:
        self.__value = value

    def get(self) -> Optional[T]:
        return self.__value

    def and_then(self, func: Callable[[T], Output]) -> Maybe:
        if self.__value is None:
            return Maybe(value=None)

        return Maybe(value=func(self.__value))


@dataclass
class Accessory:
    name: str


@dataclass
class Animal:
    accessory: Optional[Accessory]


@dataclass
class Human:
    pet: Optional[Animal]


def get_pet(human: Human) -> Optional[Animal]:
    return human.pet


def get_accessory(animal: Animal) -> Optional[Accessory]:
    return animal.accessory


def get_accessory_name(accessory: Accessory) -> str:
    return accessory.name


def get_pet_accessory_name(human: Optional[Human]) -> Optional[str]:
    return (
        Maybe(value=human)
        .and_then(get_pet)
        .and_then(get_accessory)
        .and_then(get_accessory_name)
        .get()
    )


def main() -> None:
    acc_name = get_pet_accessory_name(
        human=Human(pet=Animal(accessory=Accessory(name="Necklace")))
    )
    print(f"Accessory name when given everything: {acc_name}")

    acc_name = get_pet_accessory_name(human=Human(pet=None))
    print(f"Accessory name when given human without pet: {acc_name}")


if __name__ == "__main__":
    main()
