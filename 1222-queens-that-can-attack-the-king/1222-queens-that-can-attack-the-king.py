class Solution:
    def queensAttacktheKing(self, queens,king):
        
        horizontalAttackerLeft = []
        horizontalAttackerRight = []
        
        verticalAttackerUp = []
        verticalAttackerDown = []

        diagonalAttacker1 = []       #clockWise
        diagonalAttacker2 = []
        diagonalAttacker3 = []
        diagonalAttacker4 = []
        
        for queen in queens:
            if queen[0] == king[0]:   #vertical attacker
                
                if queen[1] > king[1]:
                    distance = queen[1]-king[1]
                    if len(verticalAttackerUp) == 0:
                        verticalAttackerUp.append(distance)
                        verticalAttackerUp.append(queen)

                    else:
                        if distance < verticalAttackerUp[0]:
                            verticalAttackerUp = []
                            verticalAttackerUp.append(distance)
                            verticalAttackerUp.append(queen)
                            
                else:
                    distance = king[1]-queen[1]
                    if len(verticalAttackerDown) == 0:
                        verticalAttackerDown.append(distance)
                        verticalAttackerDown.append(queen)

                    else:
                        if distance < verticalAttackerDown[0]:
                            verticalAttackerDown = []
                            verticalAttackerDown.append(distance)
                            verticalAttackerDown.append(queen)
                    
                        
            elif queen[1] == king[1]:   #horizontal attacker

                if queen[0] > king[0]:
                    distance = queen[0]-king[0]

                    if len(horizontalAttackerLeft) == 0:
                        horizontalAttackerLeft.append(distance)
                        horizontalAttackerLeft.append(queen)

                    else:
                        if distance < horizontalAttackerLeft[0]:
                            horizontalAttackerLeft = []
                            horizontalAttackerLeft.append(distance)
                            horizontalAttackerLeft.append(queen)
                            
                else:
                    distance = king[0]-queen[0]
                    if len(horizontalAttackerRight) == 0:
                        horizontalAttackerRight.append(distance)
                        horizontalAttackerRight.append(queen)

                    else:
                        if distance < horizontalAttackerRight[0]:
                            horizontalAttackerRight = []
                            horizontalAttackerRight.append(distance)
                            horizontalAttackerRight.append(queen)
                        
            if (queen[0]-king[0])==0:
                slope = None
                
            else:
                slope = (queen[1]-king[1])/(queen[0]-king[0])
            
            if slope == 1 or slope == -1:
                x1 = king[0]
                x2 = queen[0]
                
                y1 = king[1]
                y2 = queen[1]
                
                if (x1>x2) and (y1>y2):
                    distance = math.sqrt(((queen[1]-king[1])**2)+((queen[0]-king[0])**2))

                    if len(diagonalAttacker1) == 0:
                        diagonalAttacker1.append(distance)
                        diagonalAttacker1.append(queen)

                    else:
                        if distance < diagonalAttacker1[0]:
                            diagonalAttacker1 = []
                            diagonalAttacker1.append(distance)
                            diagonalAttacker1.append(queen)
                            
                elif (x1<x2) and (y1>y2):
                    
                    distance = math.sqrt(((queen[1]-king[1])**2)+((queen[0]-king[0])**2))

                    if len(diagonalAttacker2) == 0:
                        diagonalAttacker2.append(distance)
                        diagonalAttacker2.append(queen)

                    else:
                        if distance < diagonalAttacker2[0]:
                            diagonalAttacker2 = []
                            diagonalAttacker2.append(distance)
                            diagonalAttacker2.append(queen)
                            
                elif (x1>x2) and (y1<y2):
                    
                    distance = math.sqrt(((queen[1]-king[1])**2)+((queen[0]-king[0])**2))

                    if len(diagonalAttacker3) == 0:
                        diagonalAttacker3.append(distance)
                        diagonalAttacker3.append(queen)

                    else:
                        if distance < diagonalAttacker3[0]:
                            diagonalAttacker3 = []
                            diagonalAttacker3.append(distance)
                            diagonalAttacker3.append(queen)
                            
                elif (x1<x2) and (y1<y2):
                    
                    distance = math.sqrt(((queen[1]-king[1])**2)+((queen[0]-king[0])**2))

                    if len(diagonalAttacker4) == 0:
                        diagonalAttacker4.append(distance)
                        diagonalAttacker4.append(queen)

                    else:
                        if distance < diagonalAttacker4[0]:
                            diagonalAttacker4 = []
                            diagonalAttacker4.append(distance)
                            diagonalAttacker4.append(queen)
                
        attackers = [horizontalAttackerLeft,horizontalAttackerRight,verticalAttackerUp,verticalAttackerDown,diagonalAttacker1,diagonalAttacker2,diagonalAttacker3,diagonalAttacker4 ]
              
        validAttackers = []
        for i in range(8):
            if len(attackers[i]) > 0:
                validAttackers.append(attackers[i][1])


        return validAttackers
        