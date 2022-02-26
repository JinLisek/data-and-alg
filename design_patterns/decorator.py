from abc import ABC, abstractmethod


class Speakers(ABC):
    @abstractmethod
    def play(self, music: str) -> None:
        pass


class RegularSpeakers(Speakers):
    def play(self, music: str) -> None:
        print(f"Playing some {music}")


class TimedSpeakers(Speakers):
    def __init__(self, speakers: Speakers) -> None:
        self.__decorated = speakers

    def play(self, music: str) -> None:
        print("Waiting 3 seconds")
        self.__decorated.play(music=music)


def play_rock_and_roll(speakers: Speakers) -> None:
    speakers.play(music="Rock & Roll")


if __name__ == "__main__":
    play_rock_and_roll(speakers=RegularSpeakers())

    print("=" * 100)

    play_rock_and_roll(speakers=TimedSpeakers(speakers=RegularSpeakers()))
