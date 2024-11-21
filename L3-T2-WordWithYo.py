import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   input.txt                           |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

Буква ё в рукописных и печатных текстах по различным причинам часто заменяется на е. Эту особенность традиции письменности в русском языке можно отслеживать и использовать для установления оригинальности текстов, для поиска грамматических ошибок, для других целей, связанных с анализом текстов.

Напишите программу, которая будет искать слова в текстовом файле, в которых есть буква ё и выводить их на экран.

Знаки пунктуации не должны считаться частью слов, их следует игнорировать!
"""

def test_example():
    assert getYo(
        '''\
        Абсолютное совершенство ведёт нас к нашей цели,
        Мы не остановимся ни перед чем.
        Самой вселенной не под силу поколебать нашу твёрдость!
        И благодарные потомки оценят наш подвиг
        И будут чтить нас в веках.
        '''
    ) == ["ведёт", "твёрдость"]


def getYo(*texts: str)-> list[str]:
    return [
        word\
            .replace("!", "")\
            .replace("?", "")\
            .replace(",", "")\
            .replace(".", "")
        for text in texts
        for word in text.split()
        if "ё" in word
    ]


def main() -> None:
    with open("input.txt") as file:
        text = file.read()
        for word in getYo(text):
            print(word)


if __name__ == "__main__":
    main()