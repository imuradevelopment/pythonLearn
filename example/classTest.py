import random

# coding: utf-8
# -*- coding: utf-8 -*-

class LowLevelMonster:
    def __init__(self, HP, MP, Level):
        self.HP = HP
        self.MP = MP
        self.Level = Level

    def getBaseStatus(self):
        print(
            """
            HP      ：{0}
            MP      ：{1}
            Level   ：{2}
            """.format(self.HP, self.MP, self.Level)
        )


class Slime(LowLevelMonster):
    def __init__(self,
                name,
                HP=random.randrange(1, 10),
                MP=random.randrange(1, 10),
                Level=random.randrange(1, 10)
                ):
        self.name = name
        super().__init__(HP, MP, Level)

    def attack(self):
        print("{0}の攻撃".format(self.name))

    def getStatus(self):
        print(
            """
            名前    ：{0}
            HP      ：{1}
            MP      ：{2}
            Level   ：{3}
            特技    ：{4}
            """.format(self.name, self.HP, self.MP, self.Level, self.Level)
        )


rimuru = Slime("rimuru", 100, 200, 10)
rimuru.attack()
rimuru.getStatus()
rimuru2 = Slime("rimuru2")
rimuru2.attack()
rimuru2.getStatus()
