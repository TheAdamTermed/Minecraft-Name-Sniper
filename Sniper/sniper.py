import requests
from colorama import Fore, Style, init

init()

print(Fore.GREEN + f"██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░██████╗" + Style.RESET_ALL)
print(Fore.GREEN + f"██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██╔════╝" + Style.RESET_ALL)
print(Fore.GREEN + f"██████╔╝██║░░██║███████║██║░░██║██████╦╝██║░░░░░██║░░██║██║░░╚═╝█████═╝░╚█████╗░" + Style.RESET_ALL)
print(Fore.GREEN + f"██╔══██╗██║░░██║██╔══██║██║░░██║██╔══██╗██║░░░░░██║░░██║██║░░██╗██╔═██╗░░╚═══██╗" + Style.RESET_ALL)
print(Fore.GREEN + f"██║░░██║╚█████╔╝██║░░██║██████╔╝██████╦╝███████╗╚█████╔╝╚█████╔╝██║░╚██╗██████╔╝" + Style.RESET_ALL)
print(Fore.GREEN + f"╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░" + Style.RESET_ALL)


def check_username(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(Fore.LIGHTBLACK_EX + f"TAKEN: {username}" + Style.RESET_ALL)
        elif response.status_code == 204:
            print(Fore.GREEN + f"AVAILABLE: {username}" + Style.RESET_ALL)
            with open("valid.txt", "a") as valid_file:
                valid_file.write(username + "\n")
        elif response.status_code == 404:
            print(Fore.GREEN + f"AVAILABLE: {username}" + Style.RESET_ALL)
            with open("valid.txt", "a") as maybe_file:
                maybe_file.write(username + "\n")

    except requests.exceptions.RequestException:
        pass


def main():
    try:
        with open("usernames.txt", "r") as file:
            usernames = file.read().splitlines()

        for username in usernames:
            check_username(username)
    
    except FileNotFoundError:
        print(Fore.RED + "ERROR: usernames.txt not found!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
