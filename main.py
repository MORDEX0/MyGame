import random
import sys

warrior = {'location': "start_room", "HP": 200, "STR": 100,
        "DEX": 50, "INTL": 50, "weapon": "sword",
        "item": None, "potion": None}
mage = {'location': "start_room", "HP": 150, "STR": 50,
        "DEX": 100, "INTL": 150, "weapon": "stick",
        "item": None, "potion": None}
rogue = {'location': "start_room", "HP": 125, "STR": 75,
         "DEX": 150, "INTL": 100, "weapon": "dagger",
         "item": None, "potion": None}
enemies = {"skeleton":  {"location": None, "Shp": 150, "Sstr": 20},
           "pigman": {"location": None, "Php": 300, "Pstr": 35},
           "boss": {"location": "Boss_Room", "Bhp": 600, "Bstr": 50},
           "crimer": {"Chp": 150, "Cstr": 10, "Cdex": 50}}
trader = [15, 30, 10, 20, 15]
class_ = None
inventory = {"gold": 0}
main_player = {}
print("Возможные классы: \n1)Воин \n2)Маг \n3)Плут")
while (True):
    while(True):
        try:
            choice = int(input("Выберите персонажа: "))
            break
        except ValueError:
            print("Используйте ЦИФРЫ для выбора класса!!!")
    if (choice == 1):
        print("Класс Воин. Характеристики: \nЗдоровье - 200 \nСила - 100 "
              "\nЛовкость - 50 \nИнтеллект - 50 \nОружие - меч")
        bol = str(input("Вы уверены что хотите взять Воина? (д)да или (н)нет \n"))
        if (bol.lower() == "д" or bol.lower() == "да"):
            main_player = warrior
            class_ = str("Воин")
            break
        elif (bol.lower() == "н"or bol.lower() == "нет"):
            print("Выберите другого персонажа.")
    if (choice == 2):
        print("Класс Маг. Характеристики: \nЗдоровье - 150 "
              "\nСила - 50 \nЛовкость - 100 \nИнтеллект - 150 \nОружие - посох ")
        bol = str(input("Вы уверены что хотите взять Мага? (д)да или (н)нет \n"))
        if (bol.lower() == "д" or bol.lower() == "да"):
            main_player = mage
            class_ = str("Маг")
            break
        elif (bol.lower() == "н" or bol.lower() == "нет"):
            print("Выберите другого персонажа.")
    if (choice == 3):
        print("Класс Плута. Характеристики: \nЗдоровье - 125 \nСила - 75 "
              "\nЛовкость - 150 \nИнтеллект - 100 \nОружие - кинжал ")
        bol = str(input("Вы уверены что хотите взять Плута? (д)да или (н)нет \n"))
        if (bol.lower() == "д" or bol.lower() == "да"):
            main_player = rogue
            class_ = str("Плут")
            break
        elif (bol.lower() == "н" or bol.lower() == "нет"):
            print("Выберите другого персонажа.")
    else:
        print("Такого класса нет!!")
print(f"Ваш класс {class_} \nЗдоровье: {main_player['HP']} "
        f"\nСила: {main_player['STR']} \nЛовкость: {main_player['DEX']} "
        f"\nИнтеллект: {main_player['INTL']}")



def Movement(room):
    main_player['location'] = room
def Open_Chest():
    open_choice = str(input("Вы хотите открыть сундук? (д)да или (н)нет \n"))
    if open_choice.lower() == "д" or open_choice.lower() == "да":
        drop = int(random.randint(1, 5))
        if drop == 1:
            main_player["HP"] = main_player["HP"] + 25
            print(f"Вам выпал бафф на здоровье \nТекущее здоровье: {main_player['HP']}")
        elif drop == 2:
            main_player["STR"] = main_player["STR"] + 15
            print(f"Вам выпал бафф на силу \nТекущая сила: {main_player['STR']}")
        elif drop == 3:
            main_player["DEX"] = main_player["DEX"] + 20
            print(f"Вам выпал бафф на ловкость \nТекущая ловкость: {main_player['DEX']}")
        elif drop == 4:
            main_player["HP"] = main_player["HP"] - 50
            print(f"Вам выпал дебафф на здоровье \nТекущая здоровье: {main_player['HP']}")
        elif drop == 5:
            main_player["INTL"] = main_player["INTL"] + 20
            print(f"Вам выпал дебафф на ловкость \nТекущая ловкость: {main_player['DEX']}")
    elif (open_choice.lower() == "н" or open_choice.lower() == "нет"):
        print("Вы не получили бафф ;(")

def Trader():
    while (True):
        choose_item = int(input())
        if choose_item == 1:
            if (inventory["gold"] >= 5):
                inventory["gold"] = inventory["gold"] - 5
                main_player["HP"] = main_player["HP"] + 15
                print("Спасибо за покупку!")
            else:
                print("Вам не хватает монеток.")
        elif choose_item == 2:
            if (inventory["gold"] >= 12):
                inventory["gold"] = inventory["gold"] - 12
                main_player["HP"] = main_player["HP"] + 30
                print("Спасибо за покупку!")
            else:
                print("Вам не хватает монеток.")
        elif choose_item == 3:
            if (inventory["gold"] >= 8):
                inventory["gold"] = inventory["gold"] - 8
                main_player["STR"] = main_player["STR"] + 10
                print("Спасибо за покупку!")
            else:
                print("Вам не хватает монеток.")
        elif choose_item == 4:
            if (inventory["gold"] >= 15):
                inventory["gold"] = inventory["gold"] - 15
                main_player["STR"] = main_player["STR"] + 20
                print("Спасибо за покупку!")
            else:
                print("Вам не хватает монеток.")
        elif choose_item == 5:
            if inventory["gold"] >= 10:
                inventory["gold"] = inventory["gold"] - 10
                main_player["STR"] = main_player["STR"] + 15
                print("Спасибо за покупку!")
            else:
                print("Вам не хватает монеток.")
        elif choose_item == 6:
            break
def Enemy_drop():
    enemy_drop = int(random.randint(1, 3))
    if enemy_drop == 1:
        main_player["potion"] = "зелье здоровья"
        print("О какое везение вам выпало зелье здоровья")
    elif enemy_drop == 2:
        main_player["potion"] = "зелье силы"
        print("О какое везение вам выпало зелье силы")
    elif enemy_drop == 3:
        print("Ничего не выпало.")

def battle_skeleton():
    while(True):
        print("1)Атакавать")
        print("2)Уйти в защиту(немного увеличивает здоровье)")
        while (True):
            try:
                action = int(input("Выберите одно из двух действий: "))
                break
            except ValueError:
                print("Используйте цифры для выбора!")
        if action == 1:
            if (main_player["DEX"] > 75 or main_player["INTL"] > 125):
                main_player["STR"] = main_player["STR"] + 25
                enemies["skeleton"]["Shp"] = enemies["skeleton"]["Shp"] - main_player["STR"]
                main_player["STR"] = main_player["STR"] - 25
                if enemies["skeleton"]["Shp"] > 0:
                    print("Он все еще жив и может атакавать")
                    print(f"Его здоровье: {enemies['skeleton']['Shp']}")
                elif enemies["skeleton"]["Shp"] <= 0:
                    print("Вы убили его")
                    inventory["gold"] = inventory["gold"] + int(random.randint(1, 10))
                    print(f"У вас сейчас {inventory['gold']} монет")
                    break
            else:
                enemies["skeleton"]["Shp"] = enemies["skeleton"]["Shp"] - main_player["STR"]
                if enemies["skeleton"]["Shp"] > 0:
                    print("Он все еще жив и может атакавать")
                    print(f"Его здоровье: {enemies['skeleton']['Shp']}")
                elif enemies["skeleton"]["Shp"] <= 0:
                    print("Вы одолели его")
                    gold_drop = int(random.randint(0, 5))
                    inventory["gold"] = inventory["gold"] + gold_drop
                    print("Вам выпало " + str(gold_drop))
                    print(f"У вас сейчас {inventory['gold']} монет")
                    break
        elif action == 2:
            main_player["HP"] = main_player["HP"] + 10
        attack_skeleton = int(random.randint(1, 3))
        if attack_skeleton == 1:
            main_player["HP"] = main_player["HP"] - enemies["skeleton"]["Sstr"]
            print(f"Скелет акаковал вас и нанес 20 урона. Ваше здоровье {main_player['HP']}")
        elif attack_skeleton == 2:
            main_player["HP"] = main_player["HP"] - enemies["skeleton"]["Sstr"]
            print(f"Скелет акаковал вас и нанес 20 урона. Ваше здоровье {main_player['HP']}")
        elif attack_skeleton == 3:
            print("Вам повезло скелет промахнулся.")
        if (main_player["HP"] <= 0):
            print("Вы умерли")
            break

def battle_pigman():
    while(True):
        print("1)Атакавать")
        print("2)Уйти в защиту(немного увеличивает здоровье)")
        while(True):
            try:
                action = int(input("Выберите одно из двух действий: "))
                break
            except ValueError:
                print("Используйте цифры для выбора!")
        if action == 1:
            if (main_player["DEX"] > 75 or main_player["INTL"] > 125):
                main_player["STR"] = main_player["STR"] + 25
                enemies["pigman"]["Php"] = enemies["pigman"]["Php"] - main_player["STR"]
                main_player["STR"] = main_player["STR"] - 25
                if enemies["pigman"]["Php"] > 0:
                    print("Он все еще жив и может атакавать")
                    print(f"Его здоровье: {enemies['pigman']['Php']}")
                elif enemies["pigman"]["Php"] <= 0:
                    gold_drop = int(random.randint(0, 5))
                    inventory["gold"] = inventory["gold"] + gold_drop
                    print("Вам выпало " + str(gold_drop))
                    print(f"У вас сейчас {inventory['gold']} монет")
                    break
            else:
                enemies["pigman"]["Php"] = enemies["pigman"]["Php"] - main_player["STR"]
                if enemies["pigman"]["Php"] > 0:
                    print("Он все еще жив и может атакавать")
                    print(f"Его здоровье: {enemies['pigman']['Php']}")
                elif enemies["pigman"]["Php"] <= 0:
                    gold_drop = int(random.randint(5, 15))
                    inventory["gold"] = inventory["gold"] + gold_drop
                    print("Вам выпало " + str(gold_drop))
                    print(f"У вас сейчас {inventory['gold']} монет")
                    break
        elif action == 2:
            main_player["HP"] = main_player["HP"] + 10
        attack_pigman = int(random.randint(1, 3))
        if attack_pigman == 1:
            main_player["HP"] = main_player["HP"] - enemies["pigman"]["Pstr"]
            print(f"Свинья-человек акаковал вас и нанес 35 урона. Ваше здоровье {main_player['HP']}")
            if main_player["HP"] <= 0:
                break
        elif attack_pigman == 2:
            print("Вам повезло свинья-человек вас не атакавал.")
        elif attack_pigman == 3:
            print("Вам повезло свинья-человек вас не атакавал.")

def battle_crimer():
    gold_crimed = 0
    while (True):
        print("1)Атакавать")
        print("2)Уйти в защиту(немного увеличивает здоровье)")
        while (True):
            try:
                action = int(input("Выберите одно из двух действий: "))
                break
            except ValueError:
                print("Используйте цифры для выбора!")
        if action == 1:
            if (main_player["DEX"] > 75 or main_player["INTL"] > 125):
                main_player["STR"] = main_player["STR"] + 25
                enemies["crimer"]["Chp"] = enemies["crimer"]["Chp"] - main_player["STR"]
                main_player["STR"] = main_player["STR"] - 25
                if enemies["crimer"]["Chp"] > 0:
                    print("Он все еще жив и может атакавать")
                    print(f"Его здоровье: {enemies['crimer']['Сhp']}")

                elif enemies["crimer"]["Chp"] <= 0:
                    print("Вы одолели его и сохранили золото")
                    break
            else:
                enemies["crimer"]["Chp"] = enemies["crimer"]["Chp"] - main_player["STR"]
                if enemies["skeleton"]["Shp"] > 0:
                    print("Он все еще жив и может атакавать")
                    print(f"Его здоровье: {enemies['crimer']['Chp']}")

                elif enemies["crimer"]["Chp"] <= 0:
                    print("Вы одолели его и сохранили золото")
                    break
        elif action == 2:
            main_player["HP"] = main_player["HP"] + 10
        attack_crimer = int(random.randint(1, 2))
        if attack_crimer == 1:
            main_player["HP"] = main_player["HP"] - enemies["crimer"]["Cstr"]
            print(f"Воровщик акаковал вас и нанес 10 урона. Ваше здоровье {main_player['HP']}")
            crime_chance = int(random.randint(1, 2))
            if crime_chance == 1:
                gold_crimed = gold_crimed + 1
                print("При атаке воровщик украл 1 монету")
            elif crime_chance == 2:
                print("Вам повезло, воровщик ничего не украл")
        elif attack_crimer == 2:
            print("Вам повезло воровщик промахнулся.")
        if (main_player["HP"] <= 0):
            print("Вы умерли")
            break
    if enemies["crimer"]["Chp"] > 0:
        inventory["gold"] = inventory["gold"] - gold_crimed
    print("Он украл " + str(gold_crimed) + " монет(у) и свалил")
    print(f"У вас сейчас {inventory['gold']} монет")

def battle_boss():
    while(True):
        print("1)Атакавать")
        print("2)Уйти в защиту(немного увеличивает здоровье)")
        print("3) Использовать зелье, либо силы, либы здоровья, только то что выпало.")
        while (True):
            try:
                action = int(input("Выберите одно из двух действий: "))
                break
            except ValueError:
                print("Используйте цифры для выбора!")
        if action == 1:
            if (main_player["DEX"] > 75 or main_player["INTL"] > 125):
                main_player["STR"] = main_player["STR"] + 25
                enemies["boss"]["Bhp"] = enemies["boss"]["Bhp"] - main_player["STR"]
                main_player["STR"] = main_player["STR"] - 25
                if enemies["boss"]["Bhp"] > 0:
                    print("Он все еще жив и может атакавать")
                    print(f"Его здоровье: {enemies['boss']['Bhp']}")
                elif enemies["boss"]["Bhp"] <= 0:
                    gold_drop = int(random.randint(10, 30))
                    inventory["gold"] = inventory["gold"] + gold_drop
                    print("Вам выпало " + str(gold_drop))
                    print(f"У вас сейчас {inventory['gold']} монет")
                    break
            else:
                enemies["boss"]["Bhp"] = enemies["boss"]["Bhp"] - main_player["STR"]
                if enemies["boss"]["Bhp"] > 0:
                    print("Он все еще жив и может атакавать")
                    print(f"Его здоровье: {enemies['boss']['Bhp']}")
                elif enemies["boss"]["Bhp"] <= 0:
                    gold_drop = int(random.randint(10, 30))
                    inventory["gold"] = inventory["gold"] + gold_drop
                    print("Вам выпало " + str(gold_drop))
                    print(f"У вас сейчас {inventory['gold']} монет")
                    break
        elif action == 2:
            main_player["HP"] = main_player["HP"] + 10
        elif action == 3:
            print(f"Вы использовали {main_player['potion']}")
            if (main_player["potion"] == "зелье силы"):
                main_player["STR"] = main_player["STR"] + 40
                print("Вы получили прибавку к силе в размере 40 единиц")
                main_player["potion"] = None
            elif (main_player["potion"] == "зелье здоровья"):
                main_player["HP"] = main_player["HP"] + 85
                print("Вы получили прибавку к здоровью в размере 85 единиц")
                main_player["potion"] = None
        attack_boss = int(random.randint(1, 3))
        if attack_boss == 1:
            main_player["HP"] = main_player["HP"] - enemies["boss"]["Bstr"]
            print(f"Мунлорд акаковал вас и нанес 50 урона. Ваше здоровье {main_player['HP']}")
            if main_player["HP"] <= 0:
                break
        elif attack_boss == 2:
            print("Вам повезло Мунлорд вас не атакавал.")
        elif attack_boss == 3:
            print("Вам повезло Мунлорд вас не атакавал.")

 # MAIN CODE

start_room = main_player["location"]
while (True):
    print("1)Пройти в правую дверь")
    print("2)Пройти в левую дверь")
    print("3)Пойти прямо")
    while(True):
        try:
            move = int(input("Выберите действие: "))
            break
        except ValueError:
            print("Выбор с помощью цифр!")
    if move == 1:
        print("Перед вами скелет, а дверь не открывается. Придется сражатся.")
        battle_skeleton()
        if (main_player["HP"] <= 0):
            sys.exit("Game over")
        print("Больше ничего тут нет, вы проходите в комнату напротив. "
              "\nВ комнате уже новый противник свинья-человек, но в этой комнате еще есть и сундук. "
              "Бежать не получится. Деритесь или умрите!!")
        battle_pigman()
        if (main_player["HP"] <= 0):
            sys.exit("Game over")
        else:
            Enemy_drop()
            print("Не забывай про сундук. \n")
            break
    elif move == 2:
        print("Вы вошли в комнату и видите сундук, но не стоит радоваться, "
                "\nтак как помимо сундука в комнате находится мутировавшая свинья-человек")
        battle_pigman()
        Enemy_drop()
        if (main_player["HP"] <= 0):
            sys.exit("Game over")
        else:
            print("Молодец, ты победил его. Не забывай про сундук. \n")
            break
    elif move == 3:
        print("Войдя в комнату вы видите какого-то человека. "
              "\nВы уже готовитесь к атаке, но понимаете что он не враждебный. "
              "Вы к нему подходите и это оказывается торговец.")
        print("1) Прибавляет 15 к здоровью за 5 монет")
        print("2) Прибавляет 30 к здоровью за 12 монет")
        print("3) Прибавляет 10 к силе за 8 монет")
        print("4) Прибавляет 20 к силе за 15 монет")
        print("5) Улучшение оружия за 10 монет")
        print("6) Вернутся к прошлым комнатам")
        Trader()
    else:
        print("Вы долго колеблились и в итоге пол под вами проволился и вы умерли в муках. Соболезную.")
        sys.exit("Game over")
Open_Chest()
while (True):
    print("1)Пройти в левую дверь")
    print("2)Пройти в правую дверь")
    print("3)Вернутся к торговцу")
    while(True):
        try:
            move3 = int(input("Выберите действие: "))
            break
        except ValueError:
            print("Выбор цифрами!!")
    if move3 == 1:
        battle_pigman()
        print("Но он сбежал и вы не смогли забрать его золото. Тут тупик и вы проходите в другую дверь. "
              "\nТам вы встречаетесь с тремя скелетами. Надо победить их всех!!!")
        battle_skeleton()
        if (main_player["HP"] <= 0):
            sys.exit("Game over")
        print("Первый расспался")
        battle_skeleton()
        if (main_player["HP"] <= 0):
            sys.exit("Game over")
        print("А вот и второй посыпался как пыль.")
        battle_skeleton()
        if (main_player["HP"] <= 0):
            sys.exit("Game over")
        print("Ну и третий не составил проблем.")
        break
    elif move3 == 2:
        print("Перед вами новый противник: воровщик. "
              "Будьте бдительны он крадет монетки и может сбежать. \nА также с ним скелет")
        battle_crimer()
        if (main_player["HP"] <= 0):
            sys.exit("Game over")
        print("Еще скелет на вашем пути")
        battle_skeleton()
        print("Скелет уже не помеха. После победы появляется сундук.")
        Open_Chest()
        break
    elif move3 == 3:
        print("1) Прибавляет 15 к здоровью за 5 монет")
        print("2) Прибавляет 30 к здоровью за 12 монет")
        print("3) Прибавляет 10 к силе за 8 монет")
        print("4) Прибавляет 20 к силе за 15 монет")
        print("5) Улучшение оружия за 10 монет")
        print("6) Вернуться к прошлым комнатам")
        Trader()
while (True):
    print("Перед вами снова две двери. Одна перед вами другая по правой стороне.")
    move2 = int(input("Куда пойдете? \n 1) В дверь перед вами \n 2) В дверь справа \n 3) Вернутся к торговцу"))
    if move2 == 1:
        print("Вы входите в дверь и видите свинью-человека и скелета рядом с ним, "
              "и в кармане свиньи-человека, что-то светится это похоже на ключ. "
              "\nОни атакуют, будьте осторожней")
        battle_pigman()
        if (main_player["HP"] <= 0):
            sys.exit("Game over")
        print("Но не расслабляйтесь еще скелет. Защищайтесь он нападает.")
        battle_skeleton()
        if (main_player["HP"] <= 0):
            sys.exit("Game over")
        else:
            print("После победы вы видите, как появляется сундук.")
            Open_Chest()
            print("Осмотрев труп, вы достаете ключ с черепком из кармана."
              " \nПохоже этот ключ нужен чтобы пройти в комнату напротив. Кто же там?")
            break
    elif move2 == 2:
        print("Вы вошли в дверь и видите уже двух скелетов."
              " \nВы кричите: 'Подходите по одному!!' - и они правда начали подходить по одному")
        print("Первый подходит будьте на готове!")
        battle_skeleton()
        if (main_player["HP"] <= 0):
            sys.exit("Game over")
        print("Первый повержен. А вот и второй")
        battle_skeleton()
        if (main_player["HP"] <= 0):
            sys.exit("Game over")
        print("Вы выходите после ожесточенной битвы и идете в другую дверь. "
              "Там снова стоит свинья-человек, и в его кармане что-то блестит, это походу ключ.")
        battle_pigman()
        print("После победы вы видите, как появляется сундук.")
        Open_Chest()
        print("Осмотрев труп, вы достаете ключ с черепком из кармана."
              " \n Похоже этот ключ нужен чтобы пройти в комнату напротив. Кто же там?")
        break
    elif move2 == 3:
        print("1) Прибавляет 15 к здоровью за 5 монет")
        print("2) Прибавляет 30 к здоровью за 12 монет")
        print("3) Прибавляет 10 к силе за 8 монет")
        print("4) Прибавляет 20 к силе за 15 монет")
        print("5) Улучшение оружия за 10 монет")
        print("6) Вернуться к прошлым комнатам")
        Trader()
if (main_player["HP"] <= 0):
    sys.exit("Game over")
print("Вы использовали ключ, дверь отперлась и вы видите огромное существо, возникшее перед вами."
      " \nИ вы понимаете что это то самое существо за головой которого вы пришли. Его имя Мунлорд.")
if (main_player["HP"] > 0):
    battle_boss()

print("Это победа. Мунлорд повержен, вы забрали артефакт подтверждающий его смерть. "
        "\nВы выходите из подземелья, но на этом ваше путешествие не заканчивается. "
        "\nВпереди еще много разных испытаний. История этого испытания заканчивается сейчас. \nHappy End")
