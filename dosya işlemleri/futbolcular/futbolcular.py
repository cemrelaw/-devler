with open("futbolcular.txt", "r", encoding= "utf-8") as file:

    gs = list()
    fb= list()
    bjk = list()

    for satır in file:
        satır = satır[:-1]
        liste = satır.split(",")
        if liste[1] == "Galatasaray":
            gs.append(liste[0] + ", "  + liste[1])
        elif liste[1] == "Fenerbahçe":
            fb.append(liste[0] + ", " + liste[1])
        else:
            bjk.append(liste[0] + ", " + liste[1])

    with open("gs.txt", "w", encoding= "utf-8") as file1:
        for i in gs:
            file1.write(i + "\n")
    
    with open("fb.txt", "w", encoding= "utf-8") as file2:
        for i in fb:
            file2.write(i + "\n")

    with open("bjk.txt", "w", encoding= "utf-8") as file3:
        for i in bjk:
            file3.write(i + "\n")
