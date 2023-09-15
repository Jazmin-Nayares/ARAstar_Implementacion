"""
Env 2D
@author: huiming zhou
"""


class Env:
    def __init__(self):


        #ORIGINAL----------------------------------------------------#
        #self.x_range = 51  # size of background
        #self.y_range = 31

        #//////////////------------------------------Laberinto_1
        #self.x_range = 13  # size of background
        #self.y_range = 7

        #//////////////------------------------------Laberinto_2
        #self.x_range = 7  # size of background
        #self.y_range = 13

        #//////////////------------------------------Laberinto_3
        self.x_range = 13  # size of background
        self.y_range = 7

        self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    def obs_map(self):
        """
        Initialize obstacles' positions
        :return: map of obstacles
        """

        x = self.x_range
        y = self.y_range
        obs = set()

        for i in range(x):
            obs.add((i, 0))
        for i in range(x):
            obs.add((i, y - 1))

        for i in range(y):
            obs.add((0, i))
        for i in range(y):
            obs.add((x - 1, i))


#Nota para colocar lineas en vertical se debe de colocar el numero de la cordenada y despues i
#Para colocar lineas en horizontal se debe de colocar i y despues la cordenada 

        #Linea horizontal 
        #for i in range(1,7):
           # obs.add((i,15))
        #Linea horizontal
        #for i in range(8, 16):
            #obs.add((i, 15))
        #Linea Vertical
        #for i in range(2,26):
            #obs.add((17, i))
        #Linea vertical
        #for i in range(15):
            #obs.add((15, i))
        #Linea vertical
        #for i in range(25,30):
            #obs.add((40, i))
        #Linea Vertical
        #for i in range(15,30):
            #obs.add((30, i))
        #Linea vertical
        #for i in range(16):
            #obs.add((40, i))

        #//////////////------------------------------Laberinto_1
        """
         #Linea vertical
        for i in range(1,5):
            obs.add((1, i))
         #Linea Horizontal
        for i in range(2,11):
            obs.add((i, 1))
        #Linea vertical
        for i in range (1, 3):
            obs.add((3, i))
        """
        #//////////////------------------------------Laberinto_2
        
        """ #Linea vertical
        for i in range (2,11):
            obs.add((1, i))
        #Linea horizontal
        for i in range (1,4):
            obs.add((i, 1))
        #Linea Vertical 
        for i in range (2,11):
            obs.add((5, i))
        #Linea horizontal
        for i in range (1,3):
            obs.add((i, 11))
        #Linea horizontal
        for i in range (5,6):
            obs.add((i, 1))
        #Linea horizontal
        for i in range (4,6):
            obs.add((i, 11))
        #Linea horizontal
        for i in range (4,5):
            obs.add((i, 9))
         #Linea horizontal
        for i in range (4,5):
            obs.add((i, 6))
         #Punto solo
        for i in range(3, i):
            obs.add((i, 5)) """
       

        #//////////////------------------------------Laberinto_3
        
        
        #Linea Horizontal
        for i in range (1,9):
            obs.add((i, 1))
        #Linea Horizontal
        for i in range (10,11):
            obs.add((i, 1))
        #Linea en vertical 
        for i in range (1,5):
            obs.add((11, i))
        #Linea en vertical 
        for i in range (1,5):
            obs.add((1, i))
        #Linea Horizontal
        for i in range(1,3):
            obs.add((i,5))
        #Linea Horizontal
        for i in range(4,12):
            obs.add((i, 5))
        #Linea Horizontal
        for i in range(10,11):
            obs.add((i, 3))
        #Un solo cuadro
        for i in range(8, 9):
            obs.add((i, 2))

        

        
        return obs
