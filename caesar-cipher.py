#!/usr/bin/python3

from typing import Dict, Tuple

ALPHABETS = [
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
        'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
        'abcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
]

# Индексируем алфавиты
CHAR_MAP: Dict[str, Tuple[int, int]] = {}
for alph_idx, alphabet in enumerate(ALPHABETS):
        for char_idx, char in enumerate(alphabet):
                CHAR_MAP[char] = (alph_idx, char_idx) # Номер алфивита и порядковый знака
LENGTH_LIST: Tuple[int, ...] = tuple(len(alphabet) for alphabet in ALPHABETS)

def shift_char(char: str, shift: int) -> str:
        data = CHAR_MAP.get(char) 
        if data is not None: # если символ есть в алфавитах
                alph_num, current_index = data
                alphabet = ALPHABETS[alph_num] # Узнаем какому алфавиту принадлежит
                length = LENGTH_LIST[alph_num] # Берем длину этого алфавита
                new_index = (current_index + shift) % length
                return alphabet[new_index]
        return char

# Зашифровка - поочердно сдвигаем все символы и объеденям в строку
def encrypt(text: str, shift: int) -> str:
        return ''.join(shift_char(symbol, shift) for symbol in text)

# Расшифровка
def decrypt(text: str, key: int) -> str:
        return encrypt( text=text, shift=(-key) )

# Работа с пользователем
def run_caesar_cipher():
        try:
                text = input()
                shift = int(input())
                mode = int(input())
                if mode == 1: print(encrypt(text, shift))
                elif mode == 2: print(decrypt(text, shift))
                else: print(f"Error. Encryption mode \'{mode}\' not found.")
        except Exception: print('Error. Wrong input. Please try again.')

# Основной цикл - выход по Ctrl+C
def main():
        try:
                while True: run_caesar_cipher()
        except KeyboardInterrupt: pass

if __name__ == '__main__': main()
