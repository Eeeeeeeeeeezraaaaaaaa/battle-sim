class weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int,) -> None:
        self.name = name
        self.weapon = weapon_type
        self.damage = damage
        self.value = value


iron_sword = weapon(name="iron sword",
                    weapon_type="sharp",
                    damage=6,
                    value=10)


shor_bow = weapon(name="short bow",
                  weapon_type="ranged",
                  damage=5,
                  value=6)

fist = weapon(name="fist",
              weapon_type="blunt",
              damage=2,
              value=0)


goblin = weapon(name="goblin",
                weapon_type="goblin",
                damage=8,
                value=18)


gun = weapon(name="gun",
             weapon_type="fire arm",
             damage=10,
             value=100)

hammer = weapon(name="hammer",
                weapon_type="blunt",
                damage=9,
                value=20)

gafelid = weapon(name="garf gun",
                 weapon_type="garf",
                 damage=20,
                 value="monday")
