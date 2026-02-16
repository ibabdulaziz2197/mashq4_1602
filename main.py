# 8
meva = {"olma": 15000,
        "nok": 12000,
        "uzum": 20000,
        "shaftoli": 18000
}
print(meva)
meva.values()

# 9
kitob = {"nomi": "O'tkan kunlar",
         "muallif": "Abdulla Qodiriy",
         "yil": 1925, "sahifa": 320
}
print(kitob)
kitob.items()

# 10
kitob = {"nomi": "Mehrobdan chayon",
         "muallif": "Abdulla Qahhor",
         "sahifa": 280
}
print(kitob)

if "muallif" in kitob:
    print("Muallif kaliti mavjud")
else:
    print("Muallif kaliti mavjud emas")

# 11
rang = {"qizil": "red",
        "ko'k": "blue",
        "yashil": "green",
        "sariq": "yellow",
        "qora": "black"
}
print(rang)
print(len(rang))

# 12
user = {
    "ism": "Aziza",
    "yosh": 25,
    "shahar": "Farg'ona"
}

print(user.get("email", "Email topilmadi"))
