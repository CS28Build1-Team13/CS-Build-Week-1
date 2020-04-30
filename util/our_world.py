from adventure.models import Room

Room.objects.all().delete()

class World:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def createBoard(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        # CREATE EMPTY BOARD
        board = [None] * new_height
        for row in range(len(board)):
            board[row] = [None] * new_width
        self.data = board
    def connectRooms(self, rooms):
        for room in rooms:
            # CONNECT TO WEST
            if room.x - 1 >= 0:
                room.w_to = room.id - 1
            # CONNECT TO EAST
            if room.x + 1 <= self.width:
                room.e_to = room.id + 1
            # CONNECT TO SOUTH
            if room.y - 1 >= 0:
                room.s_to = room.id - self.height
            # CONNECT TO NORTH
            if room.y + 1 <= self.height:
                room.n_to = room.id + self.height
            room.save()
    def generateRoom(self, title, description, x, y):
        # ROOM CREATION FUNCTION
        room = Room(title=title, description=description , x=x, y=y)
        room.save()
    def populateWorld(self):
        # INITIALIZE VALUES
        roomCounter = 0
        description = f'An empty room... it has the number {roomCounter} on the floor'
        x_counter = 0
        y_counter = 0
        for row_index in range(self.width):
            # LOOP THROUGH WIDTH AND HEIGHT
            for column_index in range(self.height):
                # MAKE ROOMS
                self.generateRoom(roomCounter, description, x_counter, y_counter)
                # INCREMENT ROOM NUMBER
                roomCounter += 1
                description = f'An empty room... it has the number {roomCounter} on the floor'
                # IF X-AXIS FULL INCREMENT Y-AXIS
                if x_counter >= self.width - 1:
                    x_counter = 0
                    y_counter += 1
                else:
                    x_counter += 1
        # CONNECT ROOMS
        allRooms = Room.objects.all()
        self.connectRooms(allRooms)


world = World(10, 10)
world.populateWorld()