import random

GameOver = ValueError

def generata_com_num():
    return random.randint(1,10)

def check_guess(com_num, guessed_num):
    msg = f"Men o'ylagan son {guessed_num} sonidan "
    if com_num>int(guessed_num):
        return msg+"katta"
    if com_num<int(guessed_num):
        return msg+"kichik"
    raise GameOver

def input_user_num(counter):
    while True:
        try:
            user_num = int(input(f"{counter}-tahminingizni kiriting:  "))
            return user_num
        except ValueError:
            print("Iltimos, sonlardan foydalaning!!!")

def main():
    counter = 1
    com_num = generata_com_num()
    print("Men 1 va 10 oralig'ida son o'yladim. Sizda uchta imkoniyat bor.")
    user_num = 1


    while counter<=3:
        user_num = input_user_num(counter)
        try:
            msg = check_guess(com_num, user_num)
            print(msg)
        except GameOver:
            print(f"Siz men o'ylagan sonni {counter} urinish bilan topib g'alaba qozondingiz.")
            break
        counter += 1
    else:
        print(f"Siz barcha imkoniyatlaringizdan foydalanib yutqizdingiz. Men o'ylagan son {com_num} soni edi.")

if __name__ == "__main__":
    main()