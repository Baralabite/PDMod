GOAL_SPEED = 50
X_SCALE = 80

PWM_TOP = 90
PWM_BOTTOM = 10

X_SIZE = 160
Y_SIZE = 120

CONVERTER_CONSTANT = 10000

def calculateSpeed(x, y): #Only calculating mode 1 currently
    #X Axis Calculations
    leftSpeed = 0
    rightSpeed = 0
    if x > X_SCALE:
        leftSpeed = 0
        rightSpeed = GOAL_SPEED
    elif abs(x) > X_SCALE:
        leftSpeed = GOAL_SPEED
        rightSpeed = 0
    else:
        if x == 0:
            leftSpeed = GOAL_SPEED
            rightSpeed = GOAL_SPEED
        elif x > 0:
            leftSpeed =  GOAL_SPEED
            rightSpeed = findSpeed(abs(x))
        elif x < 0:
            leftSpeed = findSpeed(abs(x))
            rightSpeed = GOAL_SPEED

    #Y Axis Calculations
    
    return (leftSpeed, rightSpeed)

def findSpeed(x):
    return GOAL_SPEED-(x*(GOAL_SPEED*CONVERTER_CONSTANT/X_SCALE))/CONVERTER_CONSTANT        

def normalizePos(x, y):
    return (x-(X_SIZE/2), y-(Y_SIZE/2))

def speedUnitConverter(inp_speed): #Converting percentage speed to 10-90 PWM duty
    return ((((PWM_TOP-PWM_BOTTOM)*CONVERTER_CONSTANT/100)*inp_speed)/CONVERTER_CONSTANT)+10

leftSpeed, rightSpeed = calculateSpeed(0, 0)

print "Speed in Percentage: "
print leftSpeed, rightSpeed
print
print "PWM Duty Cycle Speed: "
print speedUnitConverter(leftSpeed), speedUnitConverter(rightSpeed)
