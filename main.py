from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 100, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")

# Create White Magic
cure = Spell("Cure", 12, 120, "White")
heaven = Spell("Heaven", 18, 200, "White")


# Create Items
small_potion = Item("Small health potion", "Potion", "Heals 50 HP", 50)
med_potion = Item("Medium health potion", "Potion", "Heals 100 HP", 100)
large_potion = Item("Large health potion", "Potion", "Heals 300 HP", 300)
small_elixer = Item("Small elixer", "Elixer", "Restores 25 MP", 25)
large_elixer = Item("Large elixier", "Elixer", "Restores 50 MP", 50)

bomb = Item("Bomb", "Attack", "Deals 100 points of damage", 100)


player_spells = [fire, thunder, blizzard, meteor, quake, cure, heaven]
player_items = [{"item": med_potion, "quantity": 3}, {"item": small_elixer, "quantity": 5},
				{"item": bomb, "quantity": 4}]

player = Person(500, 65, 60, 35, player_spells, player_items)
enemy = Person(1200, 65, 35, 25, [], [])

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
	print("======================================================================")
	player.choose_action()
	choice = input("Choose action: ")
	index = int(choice) - 1

	if index == 0:
		dmg = player.generate_dmg()
		enemy.take_dmg(dmg)
		print("\nYou attacked for", dmg, "points of damage.")
	elif index == 1:
		player.choose_magic()
		magic_index = int(input("Choose spell: ")) - 1

		if magic_index == -1:
			continue

		spell = player.magic[magic_index]
		curr_mp = player.get_mp()
		if curr_mp < spell.cost:
			print(bcolors.FAIL + "NOT ENOUGH MP!" + bcolors.ENDC)
			continue

		player_spell_power = spell.generate_dmg()
		player.reduce_mp(spell.cost)
		if spell.type == "Black":
			enemy.take_dmg(player_spell_power)
			print("\n" + spell.name, "spell did", player_spell_power, "points of damage.")
		elif spell.type == "White":
			player.heal(player_spell_power)
			print("\n" + spell.name, "spell healed you for", player_spell_power, "HP.")
	elif index == 2:
		player.choose_item()
		item_index = int(input("Choose item: ")) - 1

		if item_index == -1:
			continue

		item = player.items[item_index]["item"]

		player.items[item_index]["quantity"] -= 1
		if player.items[item_index]["quantity"] == 0:
			print(bcolors.FAIL + "\nNone left..." + bcolors.ENDC + "\n")
			continue

		if item.type == "Potion":
			player.heal(item.power)
			print("\n" + item.name, "healed you for", item.power, "HP.")
		elif item.type == "Elixer":
			player.restore_mp(item.power)
			print("\n" + item.name, "restored", item.power, "of your MP.")
		elif item.type == "Attack":
			enemy.take_dmg(item.power)
			print("\n" + item.name, "did", item.power, "points of damage to the enemy.")

	enemy_choice = 1
	enemy_dmg = enemy.generate_dmg()
	player.take_dmg(enemy_dmg)
	print("Enemy attacks for", enemy_dmg, "points of damage!", "\n")

	print("Player HP:", bcolors.FAIL + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
	print("Player MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC +"\n")

	print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
	print("Enemy MP:", bcolors.OKBLUE + str(enemy.get_mp()) + "/" + str(enemy.get_max_mp()) + bcolors.ENDC + "\n")

	if enemy.get_hp() == 0:
		print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
		running = False
	elif player.get_hp() == 0:
		print(bcolors.FAIL + "The enemy has defeated you!" + bcolors.ENDC)
		running = False
