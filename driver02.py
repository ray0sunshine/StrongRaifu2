import random
import threading
import time

from utilDriver import *
from utilPrimitive import *
from utilContext import *
from utilManagement import *
from utilMovement import *

grid_radius = 15

posGrid = []
posGrid.append((None))
posGrid.append(((342, 714), (grid_radius, grid_radius), grid_radius))
posGrid.append(((559, 727), (grid_radius, grid_radius), grid_radius))
posGrid.append(((794, 728), (grid_radius, grid_radius), grid_radius))
posGrid.append(((443, 577), (grid_radius, grid_radius), grid_radius))
posGrid.append(((633, 577), (grid_radius, grid_radius), grid_radius))
posGrid.append(((824, 576), (grid_radius, grid_radius), grid_radius))
posGrid.append(((524, 475), (grid_radius, grid_radius), grid_radius))
posGrid.append(((682, 476), (grid_radius, grid_radius), grid_radius))
posGrid.append(((842, 476), (grid_radius, grid_radius), grid_radius))

PL_mainMenu = [((277, 150), (57, 195, 255)), ((277, 538), (255, 182, 0)), ((1582, 1013), (255, 255, 255)), ((1583, 60), (255, 182, 0))]
PL_ch0nm = [((497, 189), (255, 182, 0)), ((492, 296), (255, 255, 255)), ((286, 48), (255, 186, 0)), ((1447, 154), (255, 182, 0)), ((1467, 468), (49, 48, 49))]
mission = (((1162, 446), (221.5, 37.5), 0), 0.5, 0.3, False)
PL_mission = [((524, 259), (255, 255, 255)), ((1028, 780), (255, 182, 0)), ((1249, 382), (49, 48, 49))]
battle = (((1050, 766), (74.0, 32.5), 0), 3, 3, False)
PL_map1 = [((439, 576), (255, 0, 0)), ((813, 441), (255, 0, 0)), ((1123, 380), (255, 255, 255)), ((1126, 117), (255, 255, 255)), ((555, 191), (132, 150, 57)), ((1178, 525), (24, 48, 49))]

click_command = (((959, 539), (54, 54), 54), 1, 1, False)
click_heli = (((543, 529), (40, 40), 40), 1, 1, False)
click_heli_dshort = (((543, 529), (40, 40), 40), 0.2, 0.3, False)
PL_echChoose = [((1542, 312), (0, 48, 66)), ((1542, 322), (16, 101, 140)), ((439, 245), (255, 255, 255)), ((457, 800), (255, 117, 0)), ((1467, 852), (49, 48, 49)), ((1427, 868), (255, 186, 0))]
ech_formation = (((522, 812), (78.0, 17.0), 0), 1, 1, False)
PL_ech1 = [((291, 51), (255, 255, 255)), ((382, 216), (255, 182, 0)), ((384, 308), (255, 255, 255)), ((1412, 802), (255, 255, 255)), ((1437, 789), (49, 48, 49))]
dps1 = (((705, 515), (73.5, 157.5), 0), 1, 0.3, False)
PL_dollSelect = [((293, 52), (255, 255, 255)), ((1569, 170), (49, 48, 49)), ((1554, 183), (255, 255, 255)), ((1569, 298), (49, 48, 49)), ((1551, 313), (255, 255, 255)), ((1213, 457), (239, 239, 239))]
filterBy = (((1510, 329), (78.0, 44.0), 0), 0.5, 0.3, False)
PL_filter = [((1138, 746), (255, 162, 0)), ((1071, 743), (255, 255, 255)), ((943, 521), (255, 255, 255)), ((1289, 464), (255, 255, 255))]

arSelect = (((917, 540), (78.0, 29.5), 0), 0.5, 0.3, False)
rfSelect = (((1296, 446), (79.0, 29.5), 0), 0.5, 0.3, False)
PL_arOnly = [((948, 520), (255, 182, 0)), ((1136, 744), (255, 162, 0)), ((1570, 298), (49, 48, 49)), ((1550, 310), (255, 255, 255))]
confirmFilter = (((1250, 745), (124.0, 20.0), 0), 1.3, 0.3, False)
PL_filtered = [((633, 159), (255, 186, 0)), ((1441, 355), (255, 182, 0)), ((1213, 458), (239, 239, 239)), ((1570, 298), (49, 48, 49)), ((1552, 315), (255, 255, 255)), ((1569, 169), (49, 48, 49)), ((1549, 179), (255, 255, 255))]

ech2Select = (((329, 308), (50.5, 27.0), 0), 1.15, 0.3, False)
PL_ech2 = [((291, 51), (255, 255, 255)), ((385, 311), (255, 182, 0)), ((383, 215), (255, 255, 255)), ((1542, 331), (0, 48, 66)), ((1532, 341), (49, 48, 49))]
dps2Select = (((514, 513), (76.5, 155.0), 0), 1, 0.3, False)
backMap = (((341, 79), (58.0, 36.0), 0), 3, 0.3, False)

deployOk = (((1507, 841), (76.5, 22.0), 0), 0.5, 0.3, False)
startMap = (((1458, 979), (130.5, 42.5), 0), 4, 4, False)
PL_mapStarted = [((416, 919), (255, 255, 255)), ((594, 73), (255, 85, 0)), ((1123, 382), (255, 255, 255)), ((1126, 117), (255, 255, 255))]
PL_resupply = [((441, 244), (255, 255, 255)), ((456, 800), (255, 117, 0)), ((1541, 312), (0, 48, 66)), ((1542, 321), (16, 101, 140)), ((1543, 771), (239, 207, 0)), ((1456, 855), (49, 48, 49))]
resupply = (((1507, 748), (92.0, 21.5), 0), 0.8, 0.3, False)

planning = (((345, 913), (69.0, 18.0), 0), 1, 0.3, False)
PL_planning = [((412, 905), (251, 207, 76))]
PL_commandSelected = [((1024, 519), (255, 186, 0)), ((959, 451), (255, 186, 0))]
PL_dragged = [((582, 62), (255, 85, 0)), ((440, 980), (255, 0, 0)), ((1394, 526), (255, 255, 255)), ((1124, 519), (255, 255, 255)), ((1122, 798), (255, 255, 255)), ((1139, 302), (255, 0, 0))]

node1 = (((794, 841), (30, 30), 30), 0.3, 0.3, False)
node2 = (((829, 616), (38, 38), 38), 0.3, 0.3, False)
node3 = (((972, 403), (30, 30), 30), 0.3, 0.3, False)
node4 = (((820, 304), (29, 29), 29), 0.8, 0.3, False)
PL_n1 = [((835, 823), (255, 186, 0))]
PL_n2 = [((799, 584), (255, 186, 0))]
PL_n3 = [((1009, 374), (255, 186, 0))]
PL_n4 = [((785, 271), (255, 186, 0))]
execute = (((1513, 981), (76.5, 34.5), 0), 0.5, 0.3, False)
PL_executed = [((275, 908), (49, 48, 49))]

PL_battle = [((930, 48), (255, 186, 0)), ((937, 48), (255, 255, 255)), ((941, 48), (255, 186, 0)), ((946, 48), (255, 255, 255)), ((954, 48), (255, 186, 0))]
PL_ended = [((1291, 560), (255, 0, 0)), ((1394, 513), (255, 255, 255)), ((1125, 508), (255, 255, 255)), ((792, 844), (255, 0, 0)), ((276, 897), (255, 255, 255)), ((1352, 997), (255, 170, 0)), ((1368, 998), (255, 170, 0))]
endRound = (((1502, 984), (75.5, 34.0), 0), 15, 15, False)
endRound2 = (((1502, 984), (75.5, 34.0), 0), 10, 10, False)

PL_turn2 = [((719, 351), (148, 203, 255)), ((1393, 514), (255, 0, 0)), ((1125, 507), (255, 255, 255))]
PL_node4 = [((757, 285), (255, 186, 0)), ((818, 216), (255, 186, 0))]
node5 = (((1118, 300), (29, 29), 29), 0.3, 0.3, False)
node6 = (((1311, 339), (53, 53), 53), 0.8, 0.3, False)
PL_n5 = [((1077, 317), (255, 186, 0))]
PL_n6 = [((1326, 384), (255, 186, 0))]

# comes later
PL_ended2 = [((582, 60), (255, 85, 0)), ((818, 302), (148, 203, 255)), ((1120, 302), (255, 0, 0)), ((1393, 513), (255, 0, 0)), ((1388, 999), (255, 170, 0)), ((1359, 999), (255, 170, 0))]
PL_result = [((1581, 69), (255, 219, 107)), ((1594, 52), (255, 186, 99)), ((465, 793), (239, 169, 0)), ((406, 735), (252, 197, 3)), ((363, 494), (255, 255, 255))]

#Manually ran
clickAway = ((995, 586), (313.5, 217.5), 0)
clickToMainMenu = ((359, 246), (68.5, 21.5), 0)
clickToChapters = (((1239, 717), (96.0, 36.0), 0), 3, 3, False)
PL_loading = [((1072, 275), (66, 69, 66)), ((724, 282), (66, 69, 66)), ((903, 281), (66, 69, 66)), ((803, 395), (198, 195, 198)), ((886, 439), (198, 195, 198)), ((956, 487), (198, 195, 198))]

#specifically set filters up
#future additions can include more diverse combinations
def filterAR():
    runSequence([PL_filter, arSelect, PL_arOnly, confirmFilter, PL_filtered])

def randomMapDrag():
    return ((randPoint((1142, 202), (200, 120)), randPoint((1202, 797), (250, 100)), 150, normalRange(0.45, 0.15)), 0.5, 0.5, True)

def initRun():
    cycle = threading.Thread(None, run, 'run')
    cycle.start()

def threadRun():
    # only reset if ended a run
    if cd.runsDone == cd.runsLimit:
        cd.runsDone = 0

    # can manually set logistics to wait for (delayed start)
    if cd.runsDone == 0:
        doLogistics()

    cd.MAP_RUNNING = not cd.MAP_RUNNING

def run():
    while not cd.COMMIT_SUDOKU:
        if cd.runsDone == 0 and cd.MAP_RUNNING:
            cd.RUNTIME = time.time()
        while cd.runsDone < cd.runsLimit and cd.MAP_RUNNING:
            runMap(cd.firstOrder)
            runMap(not cd.firstOrder)

        if cd.runsDone > 0:
            #probably need a thing to reset burnFodder
            if cd.burnFodder < cd.burnFodderLimit:
                burn_fodder()
                cd.burnFodder += 1
                cd.MAP_RUNNING = False
                threadRun()
            elif cd.MAP_RUNNING:
                alert()
                cd.MAP_RUNNING = False
        wait(0.1, 0)

def runMap(firstOrder):
    #wait until one of the start conditions is met before running through sequences
    starterWait = 0
    while not checkPixels(PL_mainMenu) and not checkPixels(PL_ch0nm):
        starterWait += 1
        if starterWait > 15:
            starterWait = 0
            alert()
        wait(1)

    #if starting from main menu
    if checkPixels(PL_mainMenu):
        logiSync()
        runSequence([PL_mainMenu, clickToChapters, PL_ch0nm])

    #enter map
    runSequence([PL_ch0nm, mission, PL_mission, battle, PL_map1])

    #setup echelons and filter
    echelon_setting = random.choice([click_command, click_heli])
    runSequence([PL_map1, echelon_setting, PL_echChoose, ech_formation, PL_ech1, dps1, PL_dollSelect, filterBy, PL_filter])
    filterAR()

    if firstOrder:
        #select first dps, ech2, select second dps, back
        runSequence([PL_filtered, cd.clickDps2_02, PL_ech1, ech2Select, PL_ech2, dps2Select, PL_filtered, cd.clickDps1_02, PL_ech2, backMap, PL_map1])
    else:
        #select first dps, ech2, select second dps, back
        runSequence([PL_filtered, cd.clickDps1_02, PL_ech1, ech2Select, PL_ech2, dps2Select, PL_filtered, cd.clickDps2_02, PL_ech2, backMap, PL_map1])

    #deploy on heli and cmd
    runSequence([PL_map1, click_command, PL_echChoose, deployOk, PL_map1, click_heli, PL_echChoose, deployOk, PL_map1])

    #start, resupply, planning, select heli, scroll
    runSequence([PL_map1, startMap, PL_mapStarted, click_heli_dshort, PL_mapStarted, click_heli, PL_resupply, resupply, PL_mapStarted, planning, PL_planning, click_command, PL_commandSelected, randomMapDrag(), PL_dragged])

    #select 4 nodes
    runSequence([PL_dragged, node1, PL_n1, node2, PL_n2, node3, PL_n3, node4, PL_n4])

    #execute
    runSequence([PL_n4, execute, PL_executed])

    #wait loop
    for i in range(3):
        singularFight(i)

    #end turn
    runSequence([PL_ended, endRound, PL_turn2, planning, PL_planning, node4, PL_node4, node5, PL_n5, node6, PL_n6])

    #execute
    runSequence([PL_n6, execute, PL_executed])

    #wait loop
    for i in range(3,5):
        singularFight(i)

    #end turn
    runSequence([PL_ended2, endRound2, PL_result])

    #click through, exit to main menu if at end of script
    if cd.runsDone < cd.runsLimit:
        rpt = randPoint(*clickAway)
        while not checkPixels(PL_loading):
            rClick(rpt, (40, 40), 40)
            wait(0.18, 0.03)
    else:
        while not checkPixels(PL_loading):
            rClick(*clickToMainMenu)
            wait(0.18, 0.03)

def singularFight(index):
    while not checkPixels(PL_battle):
        wait(0.05, 0)
    micro(index)
    while checkPixels(PL_battle):
        wait(0.05, 0)
    cd.runsDone = round(cd.runsDone + 0.1, 2)
    wait(2.3, 0.2)
    rpt = randPoint(*clickAway)
    while not checkPixels(PL_loading):
        rClick(rpt, (40, 40), 40)
        wait(0.18, 0.03)

def micro(index):
    #do some kiting here (maybe per fight based on index?)
    wait(0.5, 0.2)
    for retreat in cd.retreats_02:
        positionSelected(*posGrid[retreat])
        wait(0.3, 0.2)
        withdraw()
        wait(0.3, 0.2)
    wait(2, 0.2)
    reposition(posGrid[6], posGrid[5])
    if index != 1:
        wait(1, 0.2)
        reposition(posGrid[5], posGrid[6])
        wait(0.4, 0.2)
        reposition(posGrid[6], posGrid[5])
    if index == 2:
        wait(1.7, 0.2)
        if checkPixels(PL_battle):
            reposition(posGrid[5], posGrid[7])
            wait(1, 0.2)
            reposition(posGrid[7], posGrid[5])

def testRun():
    #param = ((1248, 735), (104.5, 36.0), 0)
    for _ in range(10):
        #rClick(*param)
        rDrag(*(randPoint((1142, 202), (200, 120)), randPoint((1202, 797), (250, 100)), 150, 0.2))
