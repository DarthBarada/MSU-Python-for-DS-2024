import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   input.txt                           |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

Писатель Яша купил себе новую пишущую машинку и сразу бросился писать свой новый роман. Закончив пятнадцатую главу и решив оценить свое творение, Яша заметил, что в пишущей машинке был очень необычный заводской брак: все слова она писала задом-наперёд, хотя и в нужном порядке. У Яши больше нет сил, чтобы переписывать роман с самого начала.

Помогите опечаленному Яше справиться с его бедой: напишите программу, которая развернет все слова в строке, не меняя их порядка.
"""

def test_example():
    assert reverseWords("Что такое осень - это небо") == "отЧ еокат ьнесо - отэ обен"
    assert reverseWords("А роза упала на лапу Азора") == "А азор алапу ан упал арозА"
    assert reverseWords("Корабли лавировали-лавировали, да не вылавировали") == "илбароК ,илаворивал-илаворивал ад ен илаворивалыв"


def reverseWords(text: str)-> str:
    return " ".join(
        word[-1::-1]
        for word in text.split()
    )


def main() -> None:
    with open("input.txt") as file:
        text = file.readline()
        print(reverseWords(text))


if __name__ == "__main__":
    main()