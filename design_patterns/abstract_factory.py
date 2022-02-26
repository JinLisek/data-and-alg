from abc import ABC, abstractmethod


class Refrigerator(ABC):
    @abstractmethod
    def cool(self, food: str) -> None:
        pass


class ModernRefrigerator(Refrigerator):
    def cool(self, food: str) -> None:
        print(f"Cooling {food} while listening to music on IoT refrigerator")


class CavemanRefrigerator(Refrigerator):
    def cool(self, food: str) -> None:
        print(f"Take {food} to shadow, hope fine, hope cool")


class Oven(ABC):
    @abstractmethod
    def heat(self, food: str) -> None:
        pass


class ModernOven(Oven):
    def heat(self, food: str) -> None:
        print(f"Heating {food} using solar power")


class CavemanOven(Oven):
    def heat(self, food: str) -> None:
        print(f"Fire on {food} good")


class KitchenFactory(ABC):
    @abstractmethod
    def create_oven(self) -> Oven:
        pass

    @abstractmethod
    def create_refrigerator(self) -> Refrigerator:
        pass


class ModernKitchenFactory(KitchenFactory):
    def create_oven(self) -> Oven:
        return ModernOven()

    def create_refrigerator(self) -> Refrigerator:
        return ModernRefrigerator()


class CavemanaKitchenFactory(KitchenFactory):
    def create_oven(self) -> Oven:
        return CavemanOven()

    def create_refrigerator(self) -> Refrigerator:
        return CavemanRefrigerator()


def prepare_and_cook_meal(meal: str, kitchen_factory: KitchenFactory):
    refrigerator = kitchen_factory.create_refrigerator()
    refrigerator.cool(food=meal)

    oven = kitchen_factory.create_oven()
    oven.heat(food=meal)


if __name__ == "__main__":
    prepare_and_cook_meal(meal="meatballs", kitchen_factory=CavemanaKitchenFactory())

    print("=" * 100)

    prepare_and_cook_meal(meal="pizza", kitchen_factory=ModernKitchenFactory())
