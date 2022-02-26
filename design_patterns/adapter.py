from abc import ABC, abstractmethod


class ExternalColorer(ABC):
    @abstractmethod
    def color(self, to_color: str) -> None:
        pass


class RegularColorer(ExternalColorer):
    def color(self, to_color: str) -> None:
        print(f"Red {to_color}")


class Colourer(ABC):
    @abstractmethod
    def colour(self, stuff: str) -> None:
        pass


class ExternalColorerToColourerAdapter(Colourer):
    def __init__(self, external_colorer: ExternalColorer) -> None:
        self.__colorer = external_colorer

    def colour(self, stuff: str) -> None:
        self.__colorer.color(to_color=stuff)


if __name__ == "__main__":
    colourer = ExternalColorerToColourerAdapter(external_colorer=RegularColorer())
    colourer.colour(stuff="car")
