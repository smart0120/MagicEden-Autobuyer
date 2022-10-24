from datetime import datetime

from colorama import Fore, Back


def c_print(message: str, color: Fore = Fore.WHITE, b_color: Back = None) -> None:
    if color == Fore.RED:
        message_type = "ERROR"
    elif color == Fore.YELLOW:
        message_type = "INFO"
    elif color == Fore.GREEN:
        message_type = "SUCCESS"
    else:
        message_type = "MESSAGE"

    d_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(
        f"{b_color if b_color is not None else Back.RESET}{color}[{message_type}] [{d_time}] | {message}{Fore.RESET}{Back.RESET}",
        color)


def c_input(message: str, color: Fore = Fore.CYAN) -> str:
    d_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"{color}[{d_time}] | {message}{Fore.RESET}", end=" ")
    return input(f"> ")
