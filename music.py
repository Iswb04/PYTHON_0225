from rich.console import Console
from time import sleep

console = Console()

def type_text(text: str, delay: float = 0.08, color: str = "cyan"):
    for char in text:
        console.out(char, end="", style=color)  
        sleep(delay)
    console.out("\n")  
def printLyrics():
    lines = [
        "I wanna da-",
        "I wanna dance in the lights",
        "I wanna ro-",
        "I wanna rock your body",
        "I wanna go",
        "I wanna go for a ride",
        "Hop in the music and",
        "Rock your body",
    ]

    for line in lines:
        type_text(line, delay=0.08)  # 0.03s por letra
        sleep(0.45) 

if __name__ == "__main__":
    printLyrics()
