from abc import ABC, abstractmethod


class MazeWalker(ABC):
    @abstractmethod
    def walk(self, maze: str) -> None:
        pass


class RightTurningMazeWalker(MazeWalker):
    def walk(self, maze: str) -> None:
        print(f"Walking through {maze}, turning RIGHT when possible")


class LeftTurningMazeWalker(MazeWalker):
    def walk(self, maze: str) -> None:
        print(f"Walking through {maze}, turning LEFT when possible")


def walk_through_maze(strategy: MazeWalker, maze: str) -> None:
    strategy.walk(maze=maze)


if __name__ == "__main__":
    walk_through_maze(strategy=RightTurningMazeWalker(), maze="minotaur maze")

    print("=" * 100)

    walk_through_maze(strategy=LeftTurningMazeWalker(), maze="triwizard maze")
