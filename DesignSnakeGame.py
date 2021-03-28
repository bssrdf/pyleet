'''
-Medium-
*Design*
*Queue*

Design a Snake game that is played on a device with screen size = width x height. Play the 
game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food’s positions in row-column order. When a snake eats the food, 
its length and the game’s score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear 
until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a 
block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)


'''

from collections import deque

class SnakeGame(object):
    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.m = height
        self.n = width        
        self.food = food + [[-1,-1]]        
        self.foodIdx = 0
        self.bodyQueue = deque([(0,0)]) # snake head on the right, tail on the left
        self.bodySet = {(0,0)}

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        oldHead = self.bodyQueue[-1]
        newHead = ( oldHead[0] + int(direction=='D') - int(direction=='U'),
                    oldHead[1] + int(direction=='R') - int(direction=='L') )
        # hit wall?
        if not ( 0<=newHead[0]<self.m and 0<=newHead[1]<self.n ):
            return -1
        # eat food?
        eatFood = ( newHead == tuple( self.food[ self.foodIdx ] ) )

        if eatFood: 
            self.foodIdx += 1
        else:
            oldTail = self.bodyQueue.popleft()
            self.bodySet.remove( oldTail )
        
        # hit self?
        if newHead in self.bodySet:
            return -1

        # grow head
        self.bodyQueue.append( newHead )
        self.bodySet.add( newHead )

        # score is body length - 1
        return len(self.bodySet) - 1


