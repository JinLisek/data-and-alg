from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self) -> None:
        pass


class SolidFuelEngine(Engine):
    def start(self) -> None:
        print("Starting solid fuel engine, there is no stopping now!")


class LiquidFuelEngine(Engine):
    def start(self) -> None:
        print(
            "Starting liquid fuel engine, don't worry, you can regulate thrust. Oops, forgot to implement that, sorry :("
        )


class Rocket(ABC):
    @abstractmethod
    def travel(self) -> None:
        pass


class Miner(Rocket):
    def __init__(self, engine: Engine) -> None:
        self.__engine = engine

    def travel(self) -> None:
        self.__engine.start()
        print("Miner traveling to the nearest asteroid")


class InterstellarArk(Rocket):
    def __init__(self, engine: Engine) -> None:
        self.__engine = engine

    def travel(self) -> None:
        self.__engine.start()
        print("Interstellar ark travelling to another stellar system")


if __name__ == "__main__":
    liquid_fuel_miner = Miner(engine=LiquidFuelEngine())
    liquid_fuel_miner.travel()

    print("=" * 100)

    solid_fuel_interstellar_ship = InterstellarArk(engine=SolidFuelEngine())
    solid_fuel_interstellar_ship.travel()

    print("=" * 100)

    liquid_fuel_interstellar_ship = InterstellarArk(engine=LiquidFuelEngine())
    liquid_fuel_interstellar_ship.travel()
