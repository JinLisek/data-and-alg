from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def click(self) -> None:
        pass


class BigRedButton(Button):
    def click(self) -> None:
        print("World destruction activated, goodbye")


class BigRedButtonWithAuthentication(Button):
    def __init__(self, authenticated: bool):
        self.__button = BigRedButton()
        self.__authenticated = authenticated

    def click(self) -> None:
        if not self.__authenticated:
            print("Not authorized to destroy the world, sorry :(")
            return

        self.__button.click()


def click_button(button: Button) -> None:
    button.click()


if __name__ == "__main__":
    click_button(button=BigRedButtonWithAuthentication(authenticated=False))

    print("=" * 100)

    click_button(button=BigRedButtonWithAuthentication(authenticated=True))
