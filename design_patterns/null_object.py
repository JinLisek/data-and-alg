from abc import ABC, abstractmethod


class Algorithm(ABC):
    @abstractmethod
    def run(self) -> None:
        pass


class HeavyAlgorithm(Algorithm):
    def __init__(self, data: int) -> None:
        self.__data = data

    def run(self) -> None:
        print(f"Doing some heavy work lasting {self.__data} minutes")


class NullAlgorithm(Algorithm):
    def run(self) -> None:
        pass


def run_algorithm_ten_times(algorithm: Algorithm):
    for _ in range(10):
        algorithm.run()


if __name__ == "__main__":
    run_algorithm_ten_times(algorithm=HeavyAlgorithm(data=3))

    print("=" * 100)

    run_algorithm_ten_times(algorithm=NullAlgorithm())
