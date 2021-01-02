class LowLevelMonster:
    def __init__(self, HP=10, MP=20, Level=1):
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
    def __init__(self, name, HP, MP, Level):
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
