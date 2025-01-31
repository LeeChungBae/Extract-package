# Extract_package/src/extract_package/ice_breaking.py

ascii_1 = '''
==++++++*++++++++*#%#==========================
==+++++++++++++++*#%#==========================
+++++++++++++++++*###==========================
+++++++++++====++*###===============-=---=-----
++++++++++======+*######%%%%%##+======---------
+++++++++=======+*#%%%%%%%%%%%%%%#+===---------
++++++++========+#%%%%%#####%%%%%%%#====-------
++++++=+========#%%%%%**++*#####%%%%#+=--------
+++++++========+%%%%#*+++=====+*##%%%%+=-------
*+++++=========*%%%**++++====-==++*%%%%===-----
######*++======%%%*+++++=====-====+*%%%+==-----
%%%%%%#######*#@@#*+++=======--====+#%%+=------
****++*****##%%@#********++=+++++++=+%%+=------
+++++++++++*##*%#*****++++==++**++===#*+=------
+++++++++++***%%*++**#*#++==+**#++===+*====----
++++++++++*+++*#*+++++++*+==+=++=====+=-==-----
++++++++++++++#+*++====+*+=====================
++++++++++++++***++====**+===++=====+==========
*+++++++++++++++*+++===+***+========#+=========
*****++++++++++**+++++*+++===+++===*%+=========
*******+++++++++*#*++**#**+++***+=***==========
*********+++++++*#%**+++***+==+++*%+===========
**********+++++*%%%##**++++==+++=*#*-==========
******+++===+==%%%%##*******++==+###--=--======
***+===========%%%%%#*****++===*####--==-=---==
*========-====+%%%%%#*+++++===+#####--====--===
========--=-=-*#%#%%#+========#####%--==-=---==
=======---=--=########=======*##%###--+===--===
=====-=---=--=########+=====+###%##%--+===--===
======---=---+########*=====####%###==+====-==-
==========-==##########+===*####%##%==+==+=====
==========-=###########%==*#####%##%*=+==++====
========+==*####%##%###%**######%##%#=+==++====
========+==###########%%#####%##%##%#**+-++====
''' 

ascii_2 = '''
.............................................................
.............................................................
.............................................................
.............................................................
........................:=*#*+######+:.......................
......................-#%%###%#%#######=.....................
.....................*%%%%%##%*%%%%%%%%%%-...................
...................:%%@@@%%#%%*#%%%%@@@%%%=..................
..................:*%%%%%%#*+=--==+*%%@@%%%+.................
..................=%%%%%%+=::::..:::-+%@@%@%-................
.................:%%%%%%=-::.......:::-#@@@@#................
.................#@%%%%=---:::..::::----%@@@@=...............
................:%@%%#=:::::--:::--:::::=@@@@%:..............
................=%%+%+:-+=#+=-:.:-=#*+=::#%#@%+..............
................+%%*#+:::::::::.:::::::::*#%@%*..............
................+%%%+=:::::::::.:::::::::#%@@@#:.............
...............-*%%%@*-:::::::::-:::::::-@@@@%*..............
...............-#%%%@%=::::::----:::::--*@@%@%*..............
...............-#%%%@@#-:::--=====--:--=@@@%%#-..............
...............-#%#%%%@#-----====-----=@@@@%%#=..............
...............:*#%%%@@@%=-::::::::-=*@@@@@@%#*:.............
................+###%%@@%+++------=+=*@@@%%@%%##:............
................-*##%%@@%+===========*@@@%%%%####+...........
................+*##%%@@%+=-=-----===*@@@@%%%%%%%%+..........
..............-####%%%%%%*=-------==+%@@%@%%%%%%%%#:.........
.............=**#*#%%%%%##+=------+*%%%%%%%%%@%%%%+-.........
............**#**#%%%%%%%*+=-----=#%%%##%%##%%####=..........
...........=######%%%%%%%#*=-----=#%%%%%%##%%%%%#+...........
...........-####*#%%%%%%%##+-:::-=#%%%%%##%%%%%%#+-..........
...........:=##*+#########*+-::::-+*%%%###%%#*++--:..........
.............:=****##%####+=-:::::--=*%%###*++=-::...........
................-*%%%%%%###-:......-:-*####%#*=::............
.................-*#%@%#*++*:.......::-+##%%#-::::...........
..................-*##***+++-.........:=*#%%*:..::...........
............:......:=*##*+=-:.........=*###*::..:............
............:........:-=++=-:.......:-++++-:...::..::........
............:..................................::.........::.
...............................................::........:::.
............:..................................:::......::...
............::.................................::::.....::.:.
.............:..............................:..:::.....::::::
'''

ascii_3 = '''
⡣⡃⡣⡃⡃⡣⡃⡣⡑⡑⢕⢑⢕⢑⢕⢑⢑⢑⢑⢑⢑⢑⢑⢑⠅⠕⠅⢕⢑⠅⠕⠅⠕⠅
⡪⡨⡨⡨⡨⡨⡨⡨⠨⠪⡢⡡⣑⡥⣕⣵⣧⡷⣵⢵⣥⡡⡑⡐⠅⠕⠅⢕⢐⠅⠅⠕⠅⠅
⡢⡂⡂⡂⡂⡂⡂⡊⡪⡨⣪⡾⣯⢿⡽⣷⣻⣟⣿⢯⣷⣻⣳⣕⢕⠅⠅⢕⢐⠅⠅⠅⠅⠅
⡂⡂⡂⡂⡂⡂⡂⡂⣢⣯⢯⡿⣽⣻⣯⣿⣽⣯⡿⣯⢿⣳⣿⣺⡷⡅⢅⠑⠄⠅⠅⠅⠅⠅
⡂⡂⡂⡂⡂⡂⠢⠨⣾⡽⣯⣟⡷⣟⣷⢿⡾⣷⣟⣿⣻⢯⡷⣿⢽⣟⠄⠅⠅⠅⠅⠅⠅⠅
⡐⡐⡐⡐⡐⠌⠌⢬⣷⡿⣿⢽⣯⣻⣝⡯⣟⣗⣟⣮⢯⣯⡯⣟⣯⡿⡎⠌⠌⠌⠌⠌⠌⠌
⡂⡂⡂⠢⠨⠨⠨⢸⡷⣿⣟⣿⣳⡷⡗⣟⣷⠵⣗⢿⢽⣽⢿⡽⣷⣟⠇⠅⠅⠅⠅⠅⠅⠅
⡂⠢⠨⠨⠨⠨⢈⢂⢿⣻⢼⡼⣔⢅⣕⢕⣕⣍⢎⢎⡅⡕⣭⣝⡿⡞⠅⠅⠅⠅⠅⠅⠅⠅
⠠⠡⠡⠡⠡⢁⢂⠘⡆⡽⡌⡇⡣⡣⡣⡱⡢⡚⡔⡱⡑⠕⡜⢔⡏⡪⠨⠨⠨⠨⠨⠨⠨⠨
⠨⠨⠨⠨⠨⢐⢐⢐⢸⢸⢸⢸⠨⠨⠨⡸⡐⡐⠄⠅⢅⠑⢌⢆⠕⠌⠌⠌⠌⠌⠌⠌⠌⠌
⠅⠅⠅⠅⡁⢂⠂⡂⢂⢑⢱⢱⢑⠅⠕⢕⢇⢚⢘⢌⠢⠡⠡⡣⠡⠡⠡⠡⠡⠡⠡⠡⠡⢁
⠠⠁⠌⡀⢂⠐⡀⠂⡐⢀⠂⢇⢇⢇⢧⢣⠦⡱⢔⢔⠅⢕⠕⠄⠡⠁⠅⠡⠁⠅⠅⠅⠅⡂
⠨⢀⠡⠐⠠⠐⢀⠁⠄⢐⢐⢸⢸⢸⢸⢸⠸⡘⢔⢕⢕⢕⢅⠡⠈⠄⠡⠈⠄⠡⠁⠅⡁⡂
⠐⢀⠐⢈⠠⠈⡀⠄⠂⡐⡀⡇⡇⡇⡇⡇⡇⡎⡆⡕⢕⢕⢱⠡⠁⠌⠐⡈⠠⠁⠌⡀⢂⠐
⢈⠀⡐⢀⠐⠠⢐⠨⢐⢐⠠⢱⠱⡨⠪⠪⠪⡊⡪⡈⡂⡂⡪⠨⠨⠠⠡⢐⢀⠡⠐⢀⠂⡈
⠀⠄⢂⠐⠨⠐⡐⠨⠐⡐⠨⠀⠣⡪⠨⡈⡂⡂⡂⡂⡂⡢⠃⠨⠨⢈⠨⠐⡐⡈⠌⡀⢂⠐
⠁⠅⢐⠈⠌⠄⢂⠨⠀⡂⠅⢌⠢⡑⡑⡐⡐⡐⡐⡐⡰⡈⢄⠅⠅⡂⠄⠅⡐⢐⠐⡐⢐⠐
⠅⠨⠀⡂⠡⠈⠄⢂⠡⠀⠅⢂⢑⠐⠄⡂⢂⢂⠂⡂⢂⠨⠀⡈⠄⠐⡀⠡⠠⠐⡀⢂⠐⡀
⠨⢀⠡⠐⡈⠄⠡⠐⡀⠅⡈⠄⠐⡀⠡⢐⠀⠂⠂⠠⠀⡐⠀⠄⢂⠡⠐⢀⠁⡂⠄⠂⢐⠠
⠐⡀⢐⠠⠐⠐⡈⠄⠐⡀⢐⠈⠠⠐⠀⡂⠀⠂⢁⠈⠄⠐⢈⠀⢂⠐⢈⠠⠠⠀⠂⡁⠄⠂
⡁⠄⠄⠂⡈⠄⠐⡈⠠⠐⡀⠌⠐⡈⠠⠐⠀⢁⠠⠐⢀⠁⠄⢈⠠⠐⢀⠐⠐⢈⠠⠀⢂⠁
⠀⠂⠂⡁⠄⠨⠠⠐⢀⠡⠀⠂⡁⠄⠂⠡⠈⢀⠐⢈⠠⠐⢈⠠⠐⢈⠠⢀⠁⠄⠐⢈⠠⠐   
'''
   
def ice_breaking():
    print(ascii_1)
    print("Sehyeon")
    print(ascii_2)
    print("Jooyoung")
    print(ascii_3)
    print("Sangwoo")

ice_breaking() # testing code
