import os
import time
import random

colors = {"red": "\033[31m", "black": '\033[30m', "blue": '\033[34m'}
afects_text = {"kyrsiv": "\033[1m", "normal": "\033[0m"}

name = ["павел", "кто то"]
color_name = ["blue", "red"]
afects_name = ["kyrsiv", "normal"]

lvlup = [3 , 3]
lvl_point = [0 , 0]
lvl = [0 ,0]

rnd_hp = random.randint(10 , 100)
hp = [ rnd_hp, rnd_hp]

rnd_many = random.randint(4 , 50)
many = [rnd_many, rnd_many]

max_armor = [10 ,10]
armor = [10, 10]
armor_regen = [1 , 1]
atac = [1 , 1]
symka = [[],[]]
max_fabric = [1  ,1]
rnd_kypec = [30 , 30]

my_vrag = ["n","n"]


kopat =  [1 , 1]
predmets = [ ["зелье здоровья +10xp[плохое]" ,"зелье улучшения лопаты +1[плохое]" , "зелье опыта +3[плохое]", "граната[плохое] -10"] ,
             ["зелье здоровья +30xp[обычное]" , "зелье опыта +6[обычное]" , "зелье улучшения лопаты +3[обычное]" , "граната[обычное] -40"] ,
             ["зелье здоровья[хорошее] +70xp" , "зелье улучшения лопаты +5[хорошее]" , "граната[хорошее] -80"],
             ["2 места для фабрики[отличное]"],
             ["HYSOS[мифическое]"]]






fabrics = [["фабрика золота 1 lvl"  ],
           ["фабрика золота 2 lvl" , "фабрика оружия 1 lvl - 6", ],
           ["фабрика золота 3 lvl" , "фабрика оружия 2 lvl - 10" ],
           ["фабрика золота 4 lvl" ,  "фабрика опыта 1 lvl" ]]







vrag = [["слизень" , 70 , 5 , ["зелье здоровья +10xp[плохое]", "зелье здоровья +10xp[плохое]" ,"граната[плохое] -10"  ,"зелье улучшения лопаты +1[плохое]"] , 50],
         ["волк" , 200 , 20 , ["зелье здоровья +30xp[обычное]" , "зелье опыта +3[плохое]" , "зелье опыта +3[плохое]" , "зелье улучшения лопаты +1[плохое]" ] , 150],
         ["медведь" , 500 , 80 , ["зелье здоровья +30xp[обычное]" , "зелье опыта +6[обычное]" ,"граната[обычное] -40" , "граната[хорошее] -80" ,"зелье улучшения лопаты +5[хорошее]"] , 400],
        ["гидра" , 1200 , 150 , ["зелье здоровья[хорошее] +70xp" ,"зелье опыта +6[обычное]" ,"зелье улучшения лопаты +5[хорошее]" , "граната[хорошее] -80" , "2 места для фабрики[отличное]" ] , 1000],
        ["пропиздон" , 25000 , 700 , ["HYSOS[мифическое]"], 15000]]


fabric_active = [[] ,[]]


xod = False

while 1:

    magaz = False


    
    


    for fab in fabric_active[xod]:
        if fab == "фабрика золота 1 lvl" :
            many[xod] += 3
        elif fab == "фабрика золота 2 lvl" :
            many[xod] += 5
        elif fab == "фабрика золота 3 lvl" :
            many[xod] += 10
        elif fab == "фабрика золота 4 lvl" :
            many[xod] += 20
        elif fab == "фабрика опыта 1 lvl":
            lvl_point[xod] += 1

        elif fab == "фабрика оружия 1 lvl - 6":
            if many[xod] >= 6:
                atac[xod] += 1
                many[xod] -= 6
        elif fab == "фабрика оружия 2 lvl - 10":
            if many[xod] >= 10:
                atac[xod] += 2
                many[xod] -= 10
        elif fab == "фабрика оружия 3 lvl - 15":
            if many[xod] >=15:
                atac[xod] += 3
                many[xod] -= 15



    if len(symka[xod]) > 10:
        for i in range(len(symka[xod]) - 10):
            del symka[xod][i+10]
        print("сумка заполнена предметы удалены")
        
        
    if armor[xod] < max_armor[xod]:
        armor[xod] += armor_regen[xod]





    os.system('cls')




    print(afects_text[afects_name[xod]])


    if my_vrag[xod] != "n":
        print()

        print(colors["red"] + my_vrag[xod][0]+ " нападает" + " хп : "+str(my_vrag[xod][1]))

        print(colors["black"])
        if armor[xod] > 0:
            armor[xod] -= my_vrag[xod][2]
        else:
            hp[xod] -= my_vrag[xod][2]

    print("\t\t\t\tmax броня : " + str(max_armor[xod]))
    print("\t\t\t\tурон : " + str(atac[xod]))
    print("\t\t\t\tлопата : " + str(kopat[xod]))
    print("\t\t\t\tшанс купца : " + str(rnd_kypec[xod]))
    print()
    print("               здоровье   " + str(hp[0]) + "(" + str(armor[0]) + ")"+ "\t\t\t\t\t\t\t\t\t\t" +
          "здоровье " + str(hp[1]) + "(" + str(armor[1]) + ")")
    print("               монеты     " + str(many[0]) + "\t\t\t\t\t\t\t\t\t\t\t" + "монеты  " + str(many[1]))
    print()
    print(colors[color_name[xod]] + "                                 ходит " + name[xod] + "  lvl : " + str(
        lvl[xod]) + "      " + str(lvl_point[xod]) + " из " + str(lvlup[xod]))
    print(colors["black"])
    print()
    print("1.Атака 1\n"
          "2.Копать\n"
          "3.lvl_up\n"
          "4.сумка\n"
          "5.фабрики\n"
          "6.напасть")

    print()






    if hp[xod] <= 0:
        print("усо")
        break





    if random.randint(0 , rnd_kypec[xod]) == 0:
        print()
        print(colors["red"] + "         купец приехал!!!!")
        print(colors["red"] + "         11.войти в магаз")
        magaz = True

    inp = input()

    if inp == "1":
        if many[xod] >= 1:
            many[xod] -= 1

            
            
            if armor[not (xod)] > 0:
                armor[not (xod)] -= atac[xod]
            else:
                if hp[not (xod)] - atac[xod] <=0 :
                    if random.randint(0 , 10) <= 5:
                        hp[not (xod)] -= atac[xod]
                    else:
                        print(colors["red"] , "ооо повезло повезло")
                        time.sleep(0.05)
                else:
                    hp[not (xod)] -= atac[xod]
        else:
            print("Нет денег")
            time.sleep(0.1)
    elif inp == "2":
        many[xod] += random.randint(kopat[xod], int(kopat[xod] * 1.5))
        
    elif inp == "3":
        lvl_point[xod] += 1


    elif inp == "4":
        for i in range(len(symka[xod])):
            print(str(i) +"."+symka[xod][i])
        inp2 = input()

        try:
            if symka[xod][int(inp2)] == "зелье здоровья +10xp[плохое]":
                hp[xod] += 10
                del symka[xod][int(inp2)]
                continue
            elif symka[xod][int(inp2)] == "зелье здоровья +30xp[обычное]":
                hp[xod] += 30
                del symka[xod][int(inp2)]
                continue
            elif symka[xod][int(inp2)] == "зелье здоровья[хорошее] +70xp":
                hp[xod] += 70
                del symka[xod][int(inp2)]
                continue
            elif symka[xod][int(inp2)] == "зелье улучшения лопаты +1[плохое]":
                kopat[xod] += 1
                del symka[xod][int(inp2)]
                continue
            elif symka[xod][int(inp2)] == "зелье опыта +3[плохое]":
                lvl_point[xod] += 3
                del symka[xod][int(inp2)]
                continue
            elif symka[xod][int(inp2)] == "зелье опыта +6[обычное]":
                lvl_point[xod] += 6
                del symka[xod][int(inp2)]
                continue
            elif symka[xod][int(inp2)] == "зелье улучшения лопаты +3[обычное]":
                kopat[xod] += 3
                del symka[xod][int(inp2)]
                continue
            elif symka[xod][int(inp2)] == "зелье улучшения лопаты +5[хорошее]":
                kopat[xod] += 5
                del symka[xod][int(inp2)]
                continue
            elif symka[xod][int(inp2)] == "граната[обычное] -40":
                if armor[not (xod)] > 0:
                    armor[not (xod)] -= 40
                else:
                    hp[not (xod)] -= 40
                del symka[xod][int(inp2)]
                continue
            elif symka[xod][int(inp2)] == "2 места для фабрики[отличное]":
                max_fabric[xod] +=2
                del symka[xod][int(inp2)]
                continue

            elif symka[xod][int(inp2)] == "граната[плохое] -10":
                if armor[not (xod)] > 0:
                    armor[not (xod)] -= 10
                else:
                    hp[not (xod)] -= 10
                del symka[xod][int(inp2)]
                continue


            elif symka[xod][int(inp2)] == "граната[хорошее] -80":
                if armor[not (xod)] > 0:
                    armor[not (xod)] -= 80
                else:
                    hp[not (xod)] -= 80
                del symka[xod][int(inp2)]
                continue
            elif symka[xod][int(inp2)] == "HYSOS[мифическое]":
                max_armor[not (xod)] = 0
                armor[not (xod)] = 0
                continue
                   





        except :
            print("eror")

    elif inp == "5":

        cena = 100

        print()
        for i in range(len( fabric_active[xod])):
            print(str(i) + "."+fabric_active[xod][i])
        print()
        print()
        print("     1.купить фабрику ")
        print("     2.купить места для фабрик ,свободныйх мест сейчас : " + str(max_fabric[xod] - len(fabric_active[xod])) )

        vibor = input()

        if vibor == "1":
            try:
                print("выберите редкость фабрики до " + str(len(fabrics)-1))
                inp2 = input()
                print()
                print("cтоимость фабрик : "+ str( (int(inp2) + 1) * cena) )
                print()
                for i in range(len(fabrics[int(inp2)])):
                    print(str(i) + "."+fabrics[int(inp2)][i])
                vibor = input()

                if many[xod] >= (int(inp2) + 1) * cena  :
                    if len(fabric_active[xod]) < max_fabric[xod]:
                        many[xod] -= (int(inp2) + 1) * cena
                        fabric_active[xod].append(fabrics[int(inp2)][int(vibor)])
                    else:
                        print("места закончились\nзаменить на")
                        for i in range(len(fabric_active[xod])):
                            print(str(i) + "." + fabric_active[xod][i])

                        try:
                            inp3 = int(input())
                            many[xod] -= (int(inp2) + 1) * cena

                            fabric_active[xod][inp3] = fabrics[int(inp2)][int(vibor)]

                        except:
                            print("eror")


                else:
                    print("нет денег")

            except Exception:
                print("eror")
                time.sleep(0.5)

        elif vibor == "2":
            print("1 место - 400$")
            try:
                inp = int(input())
                if many[xod] >= inp * 400:
                    many[xod] -= inp * 400
                    max_fabric[xod] += inp

            except Exception:
                print("eror")

    elif inp == "6":
        try:
            if my_vrag[xod] == "n":
                try:
                    for i in range(len(vrag)):
                        print(str(i)+"."+vrag[i][0] + "  хп : " + str(vrag[i][1]) + "   урон : "+str(vrag[i][2]))

                    vibor = int(input())
                    my_vrag[xod] = [vrag[vibor][0] , vrag[vibor][1] , vrag[vibor][2] , vrag[vibor][3]]
                except Exception:
                    print("eror")
            else:
                print()
                print("1.атоковать ")

                inp2 = input()
                if inp2 == "1":

                    
                    my_vrag[xod][1] -= atac[xod]
                
                    if my_vrag[xod][1] <= 0 :
                        print("ПОБЕДА")
                        rnd = random.randint(2 , 6)
                        print("вам выпало : ")
                        print()
                        for i in range(rnd):
                            predmet = my_vrag[xod][3][random.randint(0 , len( my_vrag[xod][3]) - 1 )]
                            print(predmet)
                            symka[xod].append(predmet)
                            
                        my_vrag[xod] = "n"
                        
                        
                        
                        input()
        except Exception:
            print("err")



    elif inp == "11":
        if magaz:
            rnd = random.randint(2 , 6)


            assort = []

            print("-1.выход\n")

            for i in range(rnd):
                pred = []
                redcost = 0
                rnd2= random.randint(0 , 100)
                
                
                if rnd2 < 3:
                    redcost = 3
                elif rnd2 < 10 :
                    redcost = 2
                elif rnd2 < 40 :
                    redcost = 1
                else :
                    redcost = 0



                rnd2 = random.randint(0 , len(predmets[redcost]) - 1)
                cost = random.randint(3 , 15) * (redcost + 1)

                pred.append(predmets[redcost][rnd2])
                pred.append(cost)

                assort.append(pred)
                print(str(i) +"."+ predmets[redcost][rnd2] + "    " + str(cost) +  "\n")


            vibor = input()

            if vibor == "-1":
                continue

            try:
                pocup = assort[int(vibor)]

                if many[xod] >= pocup[1]:
                    many[xod] -= pocup[1]
                    symka[xod].append(pocup[0])
                else:
                    print("нет денег")
            except Exception:
                print("eror")
                continue





    if lvl_point[xod] >= lvlup[xod]:
        lvl_point[xod] = 0
        lvl[xod] += 1
        lvlup[xod] += 1
        os.system('cls')
        print("                             " + name[xod])
        print("Новый уровень : " + str(lvl[xod]))
        print("1.броня  " + str(max_armor[xod]) + " в " + str(int(max_armor[xod] * 1.4 + 3)))
        print("2.атака  " + str(atac[xod]) + " в " + str(int(atac[xod] * 1.3 + 1)))
        print("3.лопата  " + str(kopat[xod]) + " в " + str(int(kopat[xod] + 1 * 1.2)))
        if rnd_kypec[xod] > 2:
            print("4.шанс купца  " + str(rnd_kypec[xod]) + " в " + str(rnd_kypec[xod] - 4))
        inp2 = input()
        if inp2 == "1":
            max_armor[xod] = int(max_armor[xod] * 1.5 + 3)
            armor_regen[xod] = int(armor_regen[xod] * 1.5 + 2)
        elif inp2 == "2":
            atac[xod] = int(atac[xod] * 1.6 + 1)
        elif inp2 == "3":
            kopat[xod] = int(kopat[xod] * 1.3 + 3)
        elif inp2 == "4":
            if rnd_kypec[xod] > 2:
                rnd_kypec[xod] = rnd_kypec[xod] - 4



    xod = not(xod)
    
input()
input()
input()
