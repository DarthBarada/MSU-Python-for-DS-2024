import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   studygroup.txt                      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

Классу 8 "Б" было поручено организовать школьные дежурства в новом учебном году. Ученики должны дежурить по трое, и перед классным руководителем была поставлена задача организовать тройки дежурных, составив план дежурств.

8 "Б" — очень дружный класс. Когда пришло время назначать план школьных дежурств, каждый из учеников 8 "Б" напрочь отказался принимать в этом участие, пока ему не пообещают, что в течение года он подежурит с каждым из своих друзей.

Классный руководитель 8 "Б" и учитель истории Мария Ивановна — замечательный человек и прекрасный педагог. Она решила пойти навстречу своим ученикам. Мария Ивановна сразу поняла, что ей предстоит решить сложную комбинаторную задачу и, не мешкая, приступила к опросу своих учеников.

К окончанию опроса выяснилось, что все ребята дружат со всеми. Мария Ивановна сразу сообразила, что ей предстоит организовать C^3_N троек, где N — количество ребят в классе. Помогите Марии Ивановне написать программу, составляющую всевозможные тройки дежурных.

Дан текстовый файл studygroup.txt, содержащий имена школьников 8 "Б". При помощи itertools.combinations вывести все способы назначения трёх дежурных.

Гарантируется, что в 8 "Б" классе не менее 3 человек
"""

def test_example():
    combs = getCombinations(
        "Dima Petya Sasha Misha Egor".split()
    )
    assert "\n".join(
        [
            " ".join([
                f"1: {comb[0]}",
                f"2: {comb[1]}",
                f"3: {comb[2]}"
            ])
            for comb in combs
        ]
    ) == (
        "1: Dima 2: Petya 3: Sasha\n"
        "1: Dima 2: Petya 3: Misha\n"
        "1: Dima 2: Petya 3: Egor\n"
        "1: Dima 2: Sasha 3: Misha\n"
        "1: Dima 2: Sasha 3: Egor\n"
        "1: Dima 2: Misha 3: Egor\n"
        "1: Petya 2: Sasha 3: Misha\n"
        "1: Petya 2: Sasha 3: Egor\n"
        "1: Petya 2: Misha 3: Egor\n"
        "1: Sasha 2: Misha 3: Egor"
    )


def getCombinations(students: list[str], comb = 3):
    import itertools as it
    return list(it.combinations(students, comb))


def main() -> None:
    with open("studygroup.txt", mode="r") as file:
        text = file.read()
    
    combinations =  getCombinations(text.split())
    for _, comb in enumerate(combinations, 1):
        print(
            f"1: {comb[0]}",
            f"2: {comb[1]}",
            f"3: {comb[2]}"
        )


if __name__ == "__main__":
    main()
