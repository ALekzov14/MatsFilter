mats = {
    "блин",
    "хрень",
    "капец",
    "жопа",
    "нафиг",
    "нахера",
    "идиот",
    "тупой",
    "чувырло",
    "ёмоё",
    "емое",
    "черт",
    "негр",
    "твою мать",
    "фиг",
}

swearing = input("Напишите: ")

for work in swearing.split():
    if work in mats:
        print('****',end=' ')
    else:
        print(work, end=' ')