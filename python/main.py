import bryly

#Program Główny
print("Witaj w programie do obliczeń geometrycznych!")
print("Wybierz, co chcesz obliczyć (wpisz odpowiednią cyfrę):")
print("""
1: Obwód kwadratu
2: Pole kwadratu
3: Obwód prostokąta
4: Pole prostokąta
5: Obwód równoległoboku
6: Pole równoległoboku
7: Obwód trapezu
8: Pole trapezu
9: Obwód trójkąta
10: Pole trójkąta
11: Pole trójkąta równobocznego
12: Obwód koła
13: Pole koła
14: Obwód rombu
15: Pole rombu
16: Pole powierzchni sześcianu
17: Objętość sześcianu
18: Pole powierzchni prostopadłościanu
19: Objętość prostopadłościanu
20: Pole powierzchni graniastosłupa
21: Objętość graniastosłupa
22: Pole powierzchni ostrosłupa
23: Objętość ostrosłupa
24: Pole powierzchni walca
25: Objętość walca
26: Pole powierzchni stożka
27: Objętość stożka
28: Pole powierzchni kuli
29: Objętość kuli
0: Zakończ program
""")

while True:
    inp = input("\nWybierz opcję (cyfrę): ")
    if inp == "0":
        print("Program zakończył działanie.")
        break
    elif inp == "1":
        a = float(input("Podaj bok a: "))
        print(f"Obwód kwadratu = {bryly.o_kwadratu(a)}")
    elif inp == "2":
        a = float(input("Podaj bok a: "))
        print(f"Pole kwadratu = {bryly.p_kwadratu(a)}")
    elif inp == "3":
        a = float(input("Podaj bok a: "))
        b = float(input("Podaj bok b: "))
        print(f"Obwód prostokąta = {bryly.o_prostokata(a, b)}")
    elif inp == "4":
        a = float(input("Podaj bok a: "))
        b = float(input("Podaj bok b: "))
        print(f"Pole prostokąta = {bryly.p_prostokata(a, b)}")
    elif inp == "5":
        a = float(input("Podaj bok a: "))
        b = float(input("Podaj bok b: "))
        print(f"Obwód równoległoboku = {bryly.o_rownolegloboku(a, b)}")
    elif inp == "6":
        a = float(input("Podaj bok a: "))
        h = float(input("Podaj wysokość h: "))
        print(f"Pole równoległoboku = {bryly.p_rownolegloboku(a, h)}")
    elif inp == "7":
        a = float(input("Podaj bok a: "))
        b = float(input("Podaj bok b: "))
        c = float(input("Podaj bok c: "))
        d = float(input("Podaj bok d: "))
        print(f"Obwód trapezu = {bryly.o_trapezu(a, b, c, d)}")
    elif inp == "8":
        a = float(input("Podaj bok a: "))
        b = float(input("Podaj bok b: "))
        h = float(input("Podaj wysokość h: "))
        print(f"Pole trapezu = {bryly.p_trapezu(a, b, h)}")
    elif inp == "9":
        a = float(input("Podaj bok a: "))
        b = float(input("Podaj bok b: "))
        c = float(input("Podaj bok c: "))
        print(f"Obwód trójkąta = {bryly.o_trojkata(a, b, c)}")
    elif inp == "10":
        a = float(input("Podaj bok a: "))
        h = float(input("Podaj wysokość h: "))
        print(f"Pole trójkąta = {bryly.p_trojkata(a, h)}")
    elif inp == "11":
        a = float(input("Podaj bok a: "))
        print(f"Pole trójkąta równobocznego = {bryly.p_trojkata_rownobocznego(a)}")
    elif inp == "12":
        r = float(input("Podaj promień r: "))
        print(f"Obwód koła = {bryly.o_kola(r)}")
    elif inp == "13":
        r = float(input("Podaj promień r: "))
        print(f"Pole koła = {bryly.p_kola(r)}")
    elif inp == "14":
        a = float(input("Podaj bok a: "))
        print(f"Obwód rombu = {bryly.o_rombu(a)}")
    elif inp == "15":
        e = float(input("Podaj przekątną e: "))
        f = float(input("Podaj przekątną f: "))
        print(f"Pole rombu = {bryly.p_rombu(e, f)}")
    elif inp == "16":
        a = float(input("Podaj bok a: "))
        print(f"Pole powierzchni sześcianu = {bryly.p_szescianu(a)}")
    elif inp == "17":
        a = float(input("Podaj bok a: "))
        print(f"Objętość sześcianu = {bryly.v_szescianu(a)}")
    elif inp == "18":
        a = float(input("Podaj bok a: "))
        b = float(input("Podaj bok b: "))
        c = float(input("Podaj bok c: "))
        print(f"Pole powierzchni prostopadłościanu = {bryly.p_prostopadloscianu(a, b, c)}")
    elif inp == "19":
        a = float(input("Podaj bok a: "))
        b = float(input("Podaj bok b: "))
        c = float(input("Podaj bok c: "))
        print(f"Objętość prostopadłościanu = {bryly.v_prostopadloscianu(a, b, c)}")
    elif inp == "20":
        pp = float(input("Podaj pole podstawy pp: "))
        pb = float(input("Podaj pole powierzchni bocznej pb: "))
        print(f"Pole powierzchni graniastosłupa = {bryly.p_graniastoslupa(pp, pb)}")
    elif inp == "21":
        pp = float(input("Podaj pole podstawy pp: "))
        h = float(input("Podaj wysokość h: "))
        print(f"Objętość graniastosłupa = {bryly.v_graniastoslupa(pp, h)}")
    elif inp == "22":
        pp = float(input("Podaj pole podstawy pp: "))
        pb = float(input("Podaj pole powierzchni bocznej pb: "))
        print(f"Pole powierzchni ostrosłupa = {bryly.p_ostroslupa(pp, pb)}")
    elif inp == "23":
        pp = float(input("Podaj pole podstawy pp: "))
        h = float(input("Podaj wysokość h: "))
        print(f"Objętość ostrosłupa = {bryly.v_ostroslupa(pp, h)}")
    elif inp == "24":
        r = float(input("Podaj promień podstawy r: "))
        h = float(input("Podaj wysokość h: "))
        print(f"Pole powierzchni walca = {bryly.p_walca(r, h)}")
    elif inp == "25":
        r = float(input("Podaj promień podstawy r: "))
        h = float(input("Podaj wysokość h: "))
        print(f"Objętość walca = {bryly.v_walca(r, h)}")
    elif inp == "26":
        r = float(input("Podaj promień podstawy r: "))
        l = float(input("Podaj długość tworzącej stożka l: "))
        print(f"Pole powierzchni stożka = {bryly.p_stozka(r, l)}")
    elif inp == "27":
        r = float(input("Podaj promień podstawy r: "))
        h = float(input("Podaj wysokość h: "))
        print(f"Objętość stożka = {bryly.v_stozka(r, h)}")
    elif inp == "28":
        r = float(input("Podaj promień kuli r: "))
        print(f"Pole powierzchni kuli = {bryly.p_kuli(r)}")
    elif inp == "29":
        r = float(input("Podaj promień kuli r: "))
        print(f"Objętość kuli = {bryly.v_kuli(r)}")   