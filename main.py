mats = {
    "блин":"б**н",
    "хрень":"х***ь",
    "капец":"к***ц",
    "жопа":"ж**а",
    "нафиг":"н***г",
    "нахер":"н***р",
    "идиот":"и***т",
    "тупой":"т***й",
    "ёмоё":"ё**ё",
    "черт":"ч**т",
    "негр":"н**р",
    "негры":"н***ы",
    "твою мать":"т**ю м**ь",
    "фиг":"ф*г",
}

swearing = input("Напишите: ")
censored_score = 0
print(swearing.split())

for work in swearing.split():
    work = work.strip()
    if work in mats:
        censored_blur = mats.get(work)
        print(censored_blur,end=' ')

    else:
        print(work,end=' ')
