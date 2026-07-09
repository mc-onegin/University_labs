from enum import Enum
from typing import Self
import os
FONTS_DIR = os.path.join(os.path.dirname(__file__), 'fonts')


class Color(Enum):
    BLACK = "30"
    RED = "31" 
    GREEN = "32"
    YELLOW = "33"
    BLUE = "34"
    MAGENTA = "35"
    CYAN = "36"
    WHITE = "37"
    BRIGHT_RED = "91"
    BRIGHT_GREEN = "92" 
    BRIGHT_YELLOW = "93"
    BRIGHT_BLUE = "94"
    BRIGHT_MAGENTA = "95"
    BRIGHT_CYAN = "96"
    DEFAULT = "39"


class ANSI:
    RESET = "\033[0m"
    CLEAR_SCREEN = "\033[2J"
    CURSOR_HOME = "\033[H"
    
    @staticmethod
    def color(color):
        return f"\033[{color.value}m"
    
    @staticmethod  
    def position(row, col):
        return f"\033[{row};{col}H"


class Printer:
    def __init__(self, color=Color.DEFAULT, position: tuple = (1, 1), symbol: str = "*", font_size: int = 5) -> None:
        self.color = color
        self.position = position
        self.symbol = symbol
        self.current_row = position[0]
        self.font_size = font_size

        font_file = f"font{font_size}.txt"

        self.font = self._load_font(font_file)

    def _load_font(self, filename) -> dict:
        font_dict = {}
        filepath = os.path.join(FONTS_DIR, filename)
        
        try:
            with open(filepath, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"Шрифт {filename} не найден")
            return font_dict
        
        current_char = None
        current_glyph = []
        
        for line in lines:
            line = line.rstrip('\n')
            
            if not line:
                font_dict[current_char] = current_glyph
                current_char = None
                current_glyph = []
            elif current_char is None and len(line) == 1:
                current_char = line
            else:
                current_glyph.append(line)
        
        if current_char and current_glyph:
            font_dict[current_char] = current_glyph
            
        return font_dict
    
    def print(self, text: str) -> None:
        RANGE_BETWEEN_LETTERS = 3
        SPACE = 5

        output_lines = [''] * self.font_size
        for char in text.upper():
            if char in self.font:
                glyph = self.font[char]
                max_width = max(len(line) for line in glyph)
                for i in range(self.font_size):
                    if i < len(glyph):
                        line = glyph[i].replace('*', self.symbol)
                        padded_line = line.ljust(max_width)
                        output_lines[i] += padded_line + RANGE_BETWEEN_LETTERS * ' '
            elif char == ' ':
                for i in range(self.font_size):
                    output_lines[i] += SPACE * ' '
        
        print(ANSI.RESET)
        for i, line in enumerate(output_lines):
            print(ANSI.position(self.current_row + i, self.position[1]) + 
                  ANSI.color(self.color) + 
                  line + 
                  ANSI.RESET, end = "")
        
        self.current_row += self.font_size + 1
        print(ANSI.RESET, flush=True)
    
    def __enter__(self) -> Self:
        return self
    
    def __exit__(self, *args) -> None:
        print(ANSI.RESET, end = "", flush = True)


def print_static(text, color=Color.DEFAULT, position: tuple = (1, 1), symbol: str = "*", font_size: int = 5) -> None:
    printer = Printer(color, position, symbol, font_size)
    printer.print(text)


print(ANSI.CLEAR_SCREEN + ANSI.CURSOR_HOME)

print_static("Ne hochu na diffuri", Color.WHITE, (3, 10), "☢", 9)

with Printer(Color.YELLOW, (10, 30), "☡", 7) as p:
    p.print("Vizdoravlivayte")

with Printer(Color.RED, (18, 50), "☡", 7) as p:
    p.print("Mikhail")
    p.print("Dmitrievich")