# War
# Initial Code from https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course/blob/master/war.py

from tkinter import *
import random
import PIL
from PIL import Image, ImageTk

root = Tk()
root.title('War')
root.iconbitmap('Python/war/imgages/war.ico')
root.geometry("920x600")
root.configure(background="#3c345c")

# Resize Cards
def resize_cards(card):
	# Open the image
	our_card_img = Image.open(card)

	# Resize The Image
	our_card_resize_image = our_card_img.resize((150, 218))
	
	# output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	# Return that card
	return our_card_image

# Shuffle The Cards
def shuffle():
	# Define Our Deck
	suits = ["diamonds", "clubs", "hearts", "spades"]

	global deck
	deck =[]

	for suit in suits:
		for value in range(2,15):
			deck.append(f'{value}_of_{suit}')

	# Create our players
	global dealer, player, dscore, pscore
	dealer = []
	player = []
	dscore = []
	pscore = []

	# Grab a random Card For Dealer
	dealer_card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(dealer_card)
	# Append Card To Dealer List
	dealer.append(dealer_card)
	# Output Card To Screen
	global dealer_image
	dealer_image = resize_cards(f'/Users/home/Documents/CodingDojo/Python/war/images/{dealer_card}.png')
	dealer_label.config(image=dealer_image)

	# Grab a random Card For Player
	player_card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(player_card)
	# Append Card To Dealer List
	player.append(player_card)
	# Output Card To Screen
	global player_image
	player_image = resize_cards(f'/Users/home/Documents/CodingDojo/Python/war/images/{player_card}.png')
	player_label.config(image=player_image)

	#player_label.config(text=card)

	# Put number of remaining cards in title bar
	root.title(f'War - {len(deck)} Cards Left')

	# Get The Score
	score(dealer_card, player_card)

# Deal Out Cards
def deal_cards():
	try:
		# Get the deler Card
		dealer_card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(dealer_card)
		# Append Card To Dealer List
		dealer.append(dealer_card)
		# Output Card To Screen
		global dealer_image
		dealer_image = resize_cards(f'/Users/home/Documents/CodingDojo/Python/war/images/{dealer_card}.png')
		dealer_label.config(image=dealer_image)
		#dealer_label.config(text=card)

		# Get the player Card
		player_card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(player_card)
		# Append Card To Dealer List
		player.append(player_card)
		# Output Card To Screen
		global player_image
		player_image = resize_cards(f'/Users/home/Documents/CodingDojo/Python/war/images/{player_card}.png')
		player_label.config(image=player_image)
		#player_label.config(text=card)

		# Put number of remaining cards in title bar
		root.title(f'{len(deck)} Cards Left')

		# Get The Score
		score(dealer_card, player_card)

	except:
		# Tie
		if dscore.count("x") == pscore.count("x"):
			root.title(f'Game Over! Tie! {dscore.count("x")} to {pscore.count("x")}')	
		# Dealer Wins
		elif dscore.count("x") > pscore.count("x"):
			root.title(f'Game Over! Opponent Wins! {dscore.count("x")} to {pscore.count("x")}')
		# Player Wins
		else: 
			root.title(f'Game Over! Player Wins! {pscore.count("x")} to {dscore.count("x")}')
		


def score(dealer_card, player_card):
	# Split out card numbers
	dealer_card = int(dealer_card.split("_", 1)[0])
	player_card = int(player_card.split("_", 1)[0])

	# Compare Card numbers
	if dealer_card == player_card:
		score_label.config(text="Tie! Play Again!")

	elif dealer_card > player_card:
		score_label.config(text="Opponent Wins!")
		dscore.append("x")
	else:
		score_label.config(text="Player Wins!")
		pscore.append("x")

	root.title(f'{len(deck)} Cards Left |    Opponent: {dscore.count("x")}     Player: {pscore.count("x")}')

my_frame = Frame(root, bg="#5c2c6d")
my_frame.pack(pady=30)

# Create Frames For Cards
dealer_frame = LabelFrame(my_frame, text="Opponent", bd=0, background="#5c2c6d",)
dealer_frame.grid(row=0, column=0, padx=25, ipadx=25)

player_frame = LabelFrame(my_frame, text="Player", bd=0, background="#5c2c6d")
player_frame.grid(row=0, column=1, ipadx=25)

# Put cards in frames
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=25)

player_label = Label(player_frame, text='')
player_label.pack(pady=25)

# Create Score Label
score_label = Label(root, text="", font=("Helvetica", 14), bg="#6df1d8")
score_label.pack(pady=25)

# Create a couple buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.pack(pady=25)

card_button = Button(root, text="Get Cards", font=("Helvetica", 14), command=deal_cards)
card_button.pack(pady=25)



# Shuffle Deck On Start
x=0
shuffle()
print(deck)

root.mainloop()