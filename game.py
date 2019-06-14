#!/usr/bin/python
import os, time, random

os.system('clear')
random.seed()

class npc:	#Used for getting npc names
	def __init__(self, fname, lname):
		self.fname = fname; self.lname = lname
		self.name = fname + " " + lname

class char:	#Main player
	def __init__(self):
		self.name = " "; self.clas = 0; self.att = 0; self.defe = 0
		self.magdef = 0; self.crit = 0; self.spd = 0; self.xp = 0
		self.gold = 10

	def setstats(self):
		if self.clas == 1:
			self.att = 4; self.defe = 4; self.magdef = 2
			self.crit = 0; self.spd = 3
		elif self.clas == 2:
			self.att = 1; self.defe = 6; self.magdef = 5
			self.crit = 0; self.spd = 1
		elif self.clas == 3:
			self.att = 2; self.defe = 1; self.magdef = 4
			self.crit = 0; self.spd = 6
		else:
			self.att = 1; self.defe = 0; self.magdef = 4
			self.crit = 0; self.spd = 5

	def choosechar(self):
		print("What's your name?")
		self.name = raw_input("> ")
		os.system('clear')
		while True:
			print("Choose your character.")
			print("1. Buff guy with fairly large sword")
			print("2. Fairly normal guy with mace and massive shield and a heart of gold")
			print("3. Skinny guy with a crossbow and a few knives? Yeah, I don't know about him")
			print("4. Some old guy in some robes with a fancy looking stick")
			try:
				self.clas = input("> ")
				if self.clas == 1:
					print("You chose the idiot!")
					break
				elif self.clas == 2:
					print("What a wonderful man.")
					break
				elif self.clas == 3:
					print("I don't understand you're decision making.")
					break
				elif self.clas == 4:
					print("You like hard mode, don't you?")
					break
				else:
					print("That is not an option, idiot.")
					time.sleep(2)
					os.system('clear')
			except:
				print("Enter a legitamate number ya dip.")
				time.sleep(2)
				os.system('clear')
			self.setstats()

	def inventory(constype = None):
		rows = 4
		columns = 4
		w = 0
		x = 0
		array = [[0 for i in range(columns)] for j in range(rows)]
		if constype != None:
			array[0][0] = constype.name

class weapon:	#Weapon objects
	def __init__(self, name, damage, crit):
		self.name = name
		self.damage = damage
		self.crit = crit
class armor:	#Armor objects
	def __init__(self, name, defense, magicdefense, spd):
		self.name = name
		self.defense = defense
		self.magicdefense = magicdefense
		self.spd = spd
class consumable:	#Used for potions
	def __init__(self, name):
		self.name = name
		self.hprest = 0
		self.spdboost = 0

def shop():	#Function used to bring up the shop
	npcnum = random.randrange(0,len(npcs))
	print "A man named " + npcs[npcnum].name + " greats you."
	print "1. Buy 2. Sell 3. Leave"
	while True:
		try:
			choice = input("> ")
			if choice == 1:
				print "Buy"
				while True:
					break
				break
			elif choice == 2:
				print "Sell"
				break
			elif choice == 3:
				print "You decide to leave."
				break
			else:
				print "He wasn't asking about that. I can't take you anywhere."
		except:
			print "Your incompetence has made " + npcs[npcnum].name + " annoyed with you and he tells you to leave."
			break

try:	#Opens input Files
	with open("weapon_file","r")as file:
		v = 0
		weap = []
		for line in file:
			ln = line.split()
			weap.append(weapon(ln[0],ln[1],ln[2]))
			v += 1
	file.close()
	with open("armor_file","r")as file:
		w = 0
		arm = []
		for line in file:
			ln = line.split()
			arm.append(armor(ln[0],ln[1],ln[2],ln[3]))
			w += 1
	file.close()
	with open("npc_names","r")as file:
		x = 0
		npcs = []
		for line in file:
			ln = line.split()
			npcs.append(npc(ln[0],ln[1]))
			x += 1
	file.close()
except:
	print "Bro, you're either missing the weapons file, armor file, or NPC names file."
	print "You might even be missing all of them. How'd you misplace those?"
	print "Better find those if you want this to work."
	time.sleep(2)
	exit()

def main():
	player_1 = char()
	player_1.choosechar()

	os.system('clear')
	print "Okay " + player_1.name + ", let's get this over with."
	print "You come to the opening of the dungeon, or something..."
	print "There's a guy selling stuff, you might want some of his stuff or whatever, just don't take long."
	shop()
	time.sleep(4)
	print "Anyways you enter the dungeon..."
	time.sleep(2)
	os.system('clear')

	while True:
		os.system('clear')
		print "The dungeon forks. Do you go left(1), right(2), or straight(3)?"
		try:
			choice = input("> ")
			if choice == 1:
				roomnum = random.randrange(4,10)
				break
			elif choice == 2:
				roomnum = random.randrange(4,10)
				break
			elif choice == 3:
				roomnum = random.randrange(4,10)
				break
			else:
				print "I know you're confused but that's obviously not a direction."
				time.sleep(2)
		except:
			print "Not even remotely close. Have you tried reading the screen?"
			time.sleep(2)
	if roomnum <=5:
		print "I'm genuinely surprised you didn't mess that up."
	elif roomnum <= 8:
		print "You could've made a worse choice. Not worth worthy of praise but good job I guees."
	else:
		print "Poor choice, really."

	print "You enter the first room..."

if __name__ == '__main__':
	main()
