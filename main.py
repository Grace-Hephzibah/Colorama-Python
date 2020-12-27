import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset = True)

# Fore : BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
# Back : BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
# Style : DIM, NORMAL, BRIGHT, RESET_ALL

print(Fore.RED + 'Some Red Text')
print(Fore.GREEN + 'Some Green text')
print(Fore.YELLOW + 'Some Yellow text')
print(Fore.BLUE + 'Some Blue text')
print(Fore.MAGENTA + 'Some Magenta text')
print(Fore.CYAN + 'Some Cyan text')
print(Fore.WHITE + 'Some White text')
print()

print(Back.RED + 'RED')
print(Back.GREEN + 'GREEN')
print(Back.YELLOW + 'YELLOW')
print(Back.BLUE + 'BLUE')
print(Back.MAGENTA + 'MAGENTA')
print(Back.CYAN + 'CYAN')
print(Back.WHITE + 'WHITE')
print()

print(Style.DIM + "I am DIM")
print(Style.NORMAL + "I am NORMAL")
print(Style.BRIGHT + "I am BRIGHT")
