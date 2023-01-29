#provide an array of strings where . means empty space and x means object eg. R = ["..X.X", "...X.", "X...X"]

class RobotCleaner:
    def __init__(self):
        #position based on coordinates
        self.position = [0, 0]
        #rotation as follows: 0 - East, 1 - South, 2 - West, 3 - North
        self.rotation = 0
        self.cleanned_tiles = 1
        self.moving = True
        self.visited_tiles = set()
        self.visited_tiles.add(tuple([0,0,0]))

    def clean_tile(self):
      self.cleanned_tiles +=1
    
    def supposed_rotation(self):
        return (self.rotation + 1) % 4

    def supposed_forward(self):
        #suppose move right
        if(self.rotation == 0):
            return [self.position[0] + 1, self.position[1]]
        #suppose move down
        elif(self.rotation == 1):
            return [self.position[0], self.position[1] + 1]
        #suppose move left
        elif(self.rotation == 2):
            return [self.position[0] - 1, self.position[1]]
        #suppose move up
        elif(self.rotation == 3):
            return [self.position[0], self.position[1] - 1]

    def supposed_move(self, map):
        map_height = len(map)
        map_width = len(map[0])

        supposed_step = self.supposed_forward()
        supposed_rotate = self.supposed_rotation()
        
        hit_left_wall = supposed_step[0] < 0
        hit_right_wall = supposed_step[0] > map_width - 1
        hit_top_wall = supposed_step[1] < 0
        hit_bottom_wall = supposed_step[1] > map_height - 1

        if(hit_left_wall or hit_top_wall or hit_right_wall or hit_bottom_wall or map[supposed_step[1]][supposed_step[0]] == "X"):
            return tuple([self.position[0], self.position[1], supposed_rotate])
        else:
            return tuple([supposed_step[0], supposed_step[1] , self.rotation])

    def already_clean_tile(self, tile):
        return any(t[0] == tile[0] and t[1] == tile[1] for t in self.visited_tiles)

    def move(self, tile):
        self.position = [tile[0], tile[1]]
        self.rotation = tile[2]
        self.visited_tiles.add(tile)

    def clean(self, map):
        while(self.moving == True):
            tile = self.supposed_move(map)

            if(tile in self.visited_tiles):
                self.moving = False
            else:
                if(not self.already_clean_tile(tile)):
                    self.clean_tile()
                self.move(tile)

        return self.cleanned_tiles  


def solution(R):
  robot = RobotCleaner()
  return robot.clean(R)
