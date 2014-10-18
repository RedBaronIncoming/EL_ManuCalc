#Written By dragonbeing
import math

p=0.0
lvl=0
expn=0
goal=0
reclvl=0
safeval=0.05


def main():
	getInputs()
	expforlvl=0
	itmneeded=0
	attemptsneed=0
	for x in range(lvl, goal):
		expforlvl = getLvlExp(x+1) - getLvlExp(x)		
		itmneeded = math.ceil(expforlvl / expn)	
		attemptsneed = math.ceil(attemptsneed + attemptsForSuccesses(itmneeded,calcP(x)) * (1+safeval))
	print 'Estimate of Attempts Needed: ',attemptsneed

def getInputs():
	currlvl=int(input("Current Level in Skill: "))
	global lvl
	lvl=currlvl
	global goal
	goal=int(input("Level to Reach: "))
	global expn
	expn=int(input("Experience Per Item: "))
	global reclvl
	reclvl=int(input("Recommended Item Level: "))
	global p
	p= calcP(currlvl)
	global safeval
	safeval = float(input('Extra percentage\n(Recommend between 0.05-0.20) for conservative estimate: '))

def calcP(clvl):
	
	if clvl/(float(reclvl)*2) >= 1.0:
		return 0.99
	else:
		return clvl/(reclvl*float(2)) 

def get_next_lvl_exp_mult(level):
	if level >=0 and level <10:
		return 0.4
	if level >=10 and level <20:
		return 0.3
	if level >=20 and level <30:
		return 0.2
	if level >=30 and level <40:
		return 0.14
	if level >=40 and level <90:
		return 0.07
	if level >=90:
		return 0.05

def getLvlExp(level):
	#0-1 = 140 xp
	if level == 0:
		return 0
	expinlvl = 140	
	for x in range(1, level):
		expinlvl = math.floor(expinlvl * (1+get_next_lvl_exp_mult(x)))
	return expinlvl

def attemptsForSuccesses(succ,prob):
	return succ / (1 - 2/3 * (1-prob))


main()
