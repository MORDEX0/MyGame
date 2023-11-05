import random
import sys
import json
import csv


warrior = {'location': None, "HP": 200, "STR": 100,
               "DEX": 50, "INTL": 50, "weapon": "sword",
               "item": None, "potion": None}
mage = {'location': None, "HP": 150, "STR": 50,
            "DEX": 100, "INTL": 150, "weapon": "stick",
            "item": None, "potion": None}
rogue = {'location': None, "HP": 125, "STR": 75,
             "DEX": 150, "INTL": 100, "weapon": "dagger",
             "item": None, "potion": None}
enemies = {"skeleton": {"location": None, "Shp": 150, "Sstr": 20},
               "pigman": {"location": None, "Php": 300, "Pstr": 35},
               "boss": {"location": "Boss_Room", "Bhp": 600, "Bstr": 50},
               "crimer": {"Chp": 150, "Cstr": 10, "Cdex": 50}}
trader = [15, 30, 10, 20, 15]
class_ = None
inventory = {"gold": 0}
main_player = {}
first_player = {}
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
            print(f"Вам выпал дебафф на здоровье \nТекущее здоровье: {main_player['HP']}")
        elif drop == 5:
            main_player["INTL"] = main_player["INTL"] + 20
            print(f"Вам выпал дебафф на ловкость \nТекущая ловкость: {main_player['DEX']}")
    elif (open_choice.lower() == "н" or open_choice.lower() == "нет"):
        print("Вы не получили бафф ;(")

def Trader():
    while (True):
        print(f"Ваши монеты: {inventory ['gold']}")
        print("1) Прибавляет 15 к здоровью за 5 монет")
        print("2) Прибавляет 30 к здоровью за 12 монет")
        print("3) Прибавляет 10 к силе за 8 монет")
        print("4) Прибавляет 20 к силе за 15 монет")
        print("5) Улучшение оружия за 10 монет")
        print("6) Вернутся к прошлым комнатам")
        print("Что хотите купить? Выберите(1-6): ")
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
                    inventory["gold"] = inventory["gold"] - gold_crimed
                    print("Он украл " + str(gold_crimed) + " монет(у) и свалил")
                    print(f"У вас сейчас {inventory['gold']} монет")
                    break
            else:
                enemies["crimer"]["Chp"] = enemies["crimer"]["Chp"] - main_player["STR"]
                if enemies["skeleton"]["Shp"] > 0:
                    print("Он все еще жив и может атакавать")
                    print(f"Его здоровье: {enemies['crimer']['Chp']}")

                elif enemies["crimer"]["Chp"] <= 0:
                    inventory["gold"] = inventory["gold"] - gold_crimed
                    print("Он украл " + str(gold_crimed) + " монет(у) и свалил")
                    print(f"У вас сейчас {inventory['gold']} монет")
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

def Save_player():
    with open('save.json', 'w') as file:
        json.dump(main_player, file, indent=4)

def Save_inventory():
    with open('savei.json', 'w') as file1:
        json.dump(inventory, file1, indent=4)

def Save_csv():
    with open('save.csv', 'w', newline='') as file:
        keis = ['location', 'HP', 'STR', 'DEX', 'INTL', 'weapon', 'item', 'potion']
        player = csv.DictWriter(file, fieldnames=keis, delimiter="\n")
        player.writeheader()
        player.writerow(main_player)

        for row in main_player:
            player.writerow(row)

def Del_player():
    with open('save.json', 'r') as file:
        main_player = json.load(file)

    main_player['location'] = "start_room"
    main_player['HP'] = 0
    main_player['DEX'] = 0
    main_player['STR'] = 0
    main_player['INTL'] = 0

    with open('save.json', 'w') as file:
        json.dump(main_player, file, indent=4)



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

def Fisrt_room():
    while (True):

        print("1)Пройти в правую дверь")
        print("2)Пройти в левую дверь")
        print("3)Дверь с торговцем")
        print("4) Сохраниться")
        main_player["location"] = "first_room"
        while(True):
            try:
                move = int(input("Выберите действие: "))
                break
            except ValueError:
                print("Выбор с помощью цифр!")
        if move == 1:
            print("Перед вами скелет. Как вам рассказывали скелет не самое сильное существо, "
                  "что вы можете найти в этих подземельях. Так называемый обычный рядовой монстр. "
                  f"\nЕго характеристики: \nЗдоровье {enemies['skeleton']['Shp']} "
                  f"\nСила атаки {enemies['skeleton']['Sstr']}. \nБудет странно если вы сбежите, просто убейте его.")
            battle_skeleton()
            if (main_player["HP"] <= 0):
                sys.exit("Game over")
            print("Больше ничего тут нет, вы проходите в комнату напротив. "
                  "\nВ комнате уже новый противник свинья-человек. Если верить мифам"
                  ", которые вам пассказывали в детстве,\n один чернокнижник решил скрестить два вида: "
                  "человека и свинью, и в итоге получилось это ужасно уродливое существо."
                  " Оно уже не так просто как скелет. "
                  f"\nЕго характеристики: \nЗдоровье {enemies['pigman']['Php']} "
                  f"\nСила атаки {enemies['pigman']['Pstr']}."
                  "\nБежать не получится. Деритесь или умрите!!")
            battle_pigman()
            if (main_player["HP"] <= 0):
                sys.exit("Game over")
            else:
                Enemy_drop()
                print("Не забывай про сундук. \n")
                break
        elif move == 2:

            print("В комнате новый противник свинья-человек. \nЕсли верить мифам"
                  ", которые вам пассказывали в детстве, один чернокнижник решил скрестить два вида: "
                  "человека и свинью, \nи в итоге получилось это ужасно уродливое существо."
                  " \nОно не так просто как можно подумать на первый взгляд."
                  f"\nЕго характеристики: \nЗдоровье {enemies['pigman']['Php']} "
                  f"\nСила атаки {enemies['pigman']['Pstr']}."
                  "\nБежать не получится. Деритесь или умрите!!")
            battle_pigman()
            Enemy_drop()
            if (main_player["HP"] <= 0):
                sys.exit("Game over")
            else:
                print("Молодец, ты победил его. В комнате появился сундук. \n")
                break
        elif move == 3:
            print("С опаской войдя в комнату вы видите какого-то человека. "
                  "\nВы уже готовитесь к атаке, но понимаете что это и вправду торговец.")
            Trader()
        elif move == 4:
            Save_player()
            Save_inventory()
            print("Данные успешно сохранены")

        else:
            print("Вы долго колеблились и в итоге пол под вами проволился и вы умерли в муках. Соболезную.")
            sys.exit("Game over")
    Open_Chest()
def Second_room():
    while (True):
        main_player["location"] = "second_room"
        print("1)Пройти в левую дверь")
        print("2)Пройти в правую дверь")
        print("3)Вернутся к торговцу")
        print("4)Сохраниться")
        while(True):
            try:
                move3 = int(input("Выберите действие: "))
                break
            except ValueError:
                print("Выбор цифрами!!")
        if move3 == 1:
            print("Перед вами новый противник и это воровщик. Этот сутулый поросший мхом гном любит красть золото,"
                  " ничего не спасет вас от его загребущих рук. \nТак что скорее победите его, чтобы его прогнать")
            print("Тут тупик и вы проходите в другую дверь. "
                  "\nСнова скелеты. Но их трое. Надо победить их всех!!!")
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
            print("Перед вами новый противник: воровщик. Этот сутулый поросший мхом гном любит красть золото,"
                  " ничего не спасет вас от его загребущих рук. \nТак что скорее победите его, чтобы его прогнать"
                  "\nА также с ним скелет")
            battle_crimer()
            if (main_player["HP"] <= 0):
                sys.exit("Game over")
            print("Еще скелет на вашем пути")
            battle_skeleton()
            print("Скелет уже не помеха. После победы появляется сундук.")
            Open_Chest()
            break
        elif move3 == 3:
            Trader()
        elif move3 == 4:
            Save_player()
            Save_inventory()
            print("Данные успешно сохранены")
def Third_room():
    while (True):
        main_player["location"] = "third_room"

        print("Перед вами две двери. Одна перед вами другая по правой стороне.")
        move2 = int(input("Куда пойдете? \n 1) В дверь перед вами \n 2) В дверь справа"
                          " \n 3) Вернутся к торговцу \n 4) Сохраниться\n"))
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
            print("Вы вошли в дверь и видите двух скелетов."
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

            Trader()
        elif move2 == 4:
            Save_player()
            Save_inventory()
            print("Данные успешно сохранены")
    if (main_player["HP"] <= 0):
        sys.exit("Game over")
    print("Вы использовали ключ, дверь отперлась и вы видите огромное существо, возникшее перед вами."
          " \nИ вы понимаете что это то самое существо за головой которого вы пришли. Его имя Мунлорд. "
          "Именно это неописуемое существо тревожило царство вашего короля. Пришло время покончить с этим. "
          f"\nЕго характеристики: \nЗдоровье: {enemies['boss']['Bhp']} "
          f"\nСила атаки: {enemies['boss']['Bstr']}")
    if (main_player["HP"] > 0):
        battle_boss()
    if (main_player["HP"] <= 0):
        sys.exit("Game over")
    print("Это победа. Мунлорд повержен, вы забрали артефакт подтверждающий его смерть. "
            "\nВы выходите из подземелья, но на этом ваше путешествие не заканчивается. "
            "\nВпереди еще много разных испытаний. История этого испытания заканчивается сейчас. \nHappy End")

choise = str(input("Вы впервые играете? да или нет\n"))
if (choise == "да"):
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
    Fisrt_room()
    Second_room()
    Third_room()
    Save_csv()
    Del_player()
elif (choise == "нет"):

    with open('save.json', 'r') as file:
        main_player = json.load(file)

    locacion = main_player['location']

    print(locacion)
    if (locacion == "first_room"):
        Fisrt_room()
        Second_room()
        Third_room()
        Save_csv()
        Del_player()
    elif (locacion == "second_room"):
        Second_room()
        Third_room()
        Save_csv()
        Del_player()
    elif (locacion == "third_room"):
        Third_room()
        Save_csv()
        Del_player()
