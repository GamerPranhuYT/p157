from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()

root.title("Endless Dice Game")
root.geometry("600x400")
root.configure(background="yellow2")

abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
iyvasour = ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
img = ImageTk.PhotoImage(Image.open("click.jpeg"))

player1 = Label(root, text="Player 1",bg="royal blue",fg="white")
player1.place(relx=0.1, rely=0.3, anchor=CENTER)

player2 = Label(root, text="Player 2", bg="royal blue", fg="white")
player2.place(relx=0.9, rely=0.3, anchor=CENTER)

player1_score_label = Label(root,bg="royal blue", fg="white")
player1_score_label.place(relx=0.1, rely=0.4, anchor=CENTER)

player2_score_label = Label(root, bg="royal blue", fg="white")
player2_score_label.place(relx=0.9, rely=0.4, anchor=CENTER)

random_dice_label = Label(root, bg="chocolate1", fg="white")
random_dice_label.place(relx=0.5, rely=0.5, anchor=CENTER)

pokemon_list = [pikachu, bulbasour, iyvasour, charmender, squirtle, ratata, jigglypuff, meowth, persion, abra, kadabra, paras]
power_list = [200, 60, 160, 50, 50, 40, 70, 60, 70, 30, 70, 40]

label = Label(root)
label.place(relx=0.5,rely=0.5, anchor=CENTER)

player1_score = 0

def player1():
    global player1_score
    random_number = random.randint(0,11)
    random_pokemon = pokemon_list[random_number]
    label["image"]= random_pokemon
    random_power = power_list[random_number]
    player1_score = player1_score + random_power
    player1_score_label["text"]= str(player1_score)

player1_button = Button(root, image= img, command= player1)
player1_button.place(relx=0.1, rely=0.6, anchor=CENTER)

player2_score = 0

def player2():
    global player2_score
    random_number = random.randint(0,11)
    random_pokemon = pokemon_list[random_number]
    label["image"]= random_pokemon
    random_power = power_list[random_number]
    player2_score = player2_score + random_power
    player2_score_label["text"]= str(player2_score)

player2_button = Button(root, image= img, command= player2)
player2_button.place(relx=0.9, rely=0.6, anchor=CENTER)
    
root.mainloop()