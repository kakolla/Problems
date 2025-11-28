# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def dfs(self, robot, x, y, d):
        robot.clean()
        self.visited.add((x,y)) 
        
        dirs = [[0,1], [1,0], [0,-1],[-1,0]]
        for i in range(4):
            # new direction could be 0,1,2,3
            # but we turn 4 times starting from orientation d
            new_dir = (d + i) % 4
            dx,dy = dirs[new_dir]
            nx,ny = x+dx, y+dy

            if (nx, ny) not in self.visited:
                if robot.move():
                    self.dfs(robot, nx,ny, new_dir)
                    # backtrack 
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()

            robot.turnRight() # turn right - explore this next

            
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        self.visited = set()
        pos = (0,0) # local position
        self.dfs(robot, pos[0], pos[1], 0)
            
        