import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   input.txt                           |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

Нотариус Зоя помогает юридически неграмотным гражданам оформлять их жалобы и запросы в государственные службы и коммерческие компании. У Зои трудная работа: многие граждане совсем не умеют не только составлять юридически верные тексты, но ещё и оформлять свои мысли в сколько-нибудь связной форме.

Однажды клиентом Зои стал подросток Вадим. Вадим очень любил копаться в компьютерах и прочей технике и очень не любил уроки литературы, которые активно прогуливал. Вадим принес Зое папку жалоб на разные компании, в которых он заказывал компоненты компьютеров — они часто доставлялись в неудовлетворительном состоянии.

Прочитав первую жалобу, Зоя обомлела: слова-паразиты встречались в тексте Вадима буквально через слово.

Зоя поняла, что исправить все записки Вадима вручную — задача непосильная. Помогите Зое, исключив каждое второе слово из текстов Вадима.
"""

def test_example():
    assert skipEverySecondWord(
        "Мне типа привезли этот товар ну в вообще плохом совсем состоянии."
    ) == "Мне привезли товар в плохом состоянии."
    
    assert skipEverySecondWord(
        "Плата там разбита прямо."
    ) == "Плата разбита"
    
    assert skipEverySecondWord(
        "Я вот хочу типа вернуть это, деньги."
    ) == "Я хочу вернуть деньги."


def skipEverySecondWord(text: str)-> str:
    return " ".join(text.split()[::2])


def main() -> None:
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            print(
                skipEverySecondWord(line)
            )


if __name__ == "__main__":
    main()