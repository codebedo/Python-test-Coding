"""spells = [#(spell , Damage, Mana)
    ("Fireball", 50, 40),
    ("Ice Shard", 30, 25),
    ("Lightning", 70, 50),
    ("Wınd Slash", 20, 10),
    ("Dark Nova", 55, 50)]



def dmg_per_mana(s):
    return s[1]/s[2]

efficent_spells = sorted(
    spells,
    key=dmg_per_mana,
    reverse=True
)


for s in efficent_spells:
    print(f'{s[0]}: {s[1] / s[2]}')


x = lambda a : a + 10
print(x(5))"""

"""
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)

print(mydoubler(11))
"""



"""spells = [#(spell , Damage, Mana)
    ("Fireball", 50, 40),
    ("Ice Shard", 30, 25),
    ("Lightning", 70, 50),
    ("Wınd Slash", 20, 10),
    ("Dark Nova", 55, 50)]



def dmg_per_mana(s):
    return s[1]/s[2]

efficent_spells = sorted(
    spells,
    key=dmg_per_mana,  burada bir defaya mahsus kulanılan bir func var bunun yerine lambda kullanırız karmaşıklığı azaltır
    reverse=True
)


for s in efficent_spells:
    print(f'{s[0]}: {s[1] / s[2]}')
"""
spells = [#(spell , Damage, Mana)
    ("Fireball", 50, 40),
    ("Ice Shard", 30, 25),
    ("Lightning", 70, 50),
    ("Wınd Slash", 20, 10),
    ("Dark Nova", 55, 50)]



def dmg_per_mana(s):
    return s[1]/s[2]

efficent_spells = sorted(
    spells,
    key=lambda s: s[1] / s[2],
    reverse=True
)


for s in efficent_spells:
    print(f'{s[0]}: {s[1] / s[2]}')