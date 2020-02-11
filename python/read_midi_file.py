from pathlib import Path

print("\033[0;37;41m#####      read_midi_file.py      #####")
continu = True
compteur = 0
tmp = []
task = ""
print("\033[0;31;48m###      Write file name      ###")
filename = input("\033[0;37;48m")
filename = Path("files/"+filename)
if filename.exists():
    with open(filename, 'rb') as in_file:
        print("\033[0;31;48m###      File in process      ###")
        print("\033[0;37;48m")
        while continu == True:
            hexdata = in_file.read(1).hex()

            if len(hexdata) == 0:                # breaks loop once no more binary data is read
                continu = False
                print("\033[0;37;48m")
                print("\033[0;31;48m###      End of file      ###")
            else:
                tmp.append(hexdata)
                if(compteur == 0):
                    if("".join(tmp) == "4d546864"):
                        compteur = 14
                        color = "32"
                    elif("".join(tmp) == "4d54726b"):
                        compteur = 8
                        color = "34"
                        task = "read_track"
                else:
                    if(compteur == len(tmp)):
                        print("\033[0;"+color+";48m" + " ".join(tmp))
                        compteur = 0
                        if(task == "read_track"):
                            compteur = int(
                                "0x"+str("".join([tmp[len(tmp)-4], tmp[len(tmp)-3], tmp[len(tmp)-2], tmp[len(tmp)-1]])), 0) - 3
                            task = "write_track"
                            color = "36"
                        elif(task == "write_track"):
                            compteur = 3
                            color = "35"
                            task = "end_track"
                        tmp = []

    print("\033[0;37;48m")
    print("\033[0;37;48m###      Untreated part      ###")
    print("\033[0;37;48m"+" ".join(tmp))
    print("compteur.value : "+str(compteur))
    print("task.value : "+task)
else:
    print("\033[0;31;48m###      Can't find the file      ###")
