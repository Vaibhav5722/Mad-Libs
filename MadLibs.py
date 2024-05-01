from tkinter import *


def Story1(window):
    def final(tl: Toplevel, friend_name, sports, City, playername, drinkname, snacks):

        text = f'''
           One day me and my friend { friend_name} decided to play  {sports}   in {City}.
           But we were not able to play.So, we went to watch the game and our favourite player {playername}.
           We drank {drinkname} and also ate some {snacks} 
           We really enjoyed it! We are looking forward to go again and enjoy '''

        tl.geometry(newGeometry='1920x1080')

        Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)

    NewScreen = Toplevel(window, bg='violet')
    NewScreen.title("A Memorable Day")
    NewScreen.geometry('1920x1080')
    Label(NewScreen, text=' A Memorable Day').place(x=100, y=0)
    Label(NewScreen, text='friend Name:').place(x=0, y=35)
    Label(NewScreen, text='Enter a sports:').place(x=0, y=70)
    Label(NewScreen, text='Enter a city:').place(x=0, y=110)
    Label(NewScreen, text='Enter the name of a player:').place(x=0, y=150)
    Label(NewScreen, text='Enter the name of a drink:').place(x=0, y=190)
    Label(NewScreen, text='Enter the name of a snack:').place(x=0, y=230)
    Name = Entry(NewScreen, width=17)
    Name.place(x=250, y=35)
    game = Entry(NewScreen, width=17)
    game.place(x=250, y=70)
    city = Entry(NewScreen, width=17)
    city.place(x=250, y=105)
    player = Entry(NewScreen, width=17)
    player.place(x=250, y=150)
    drink = Entry(NewScreen, width=17)
    drink.place(x=250, y=190)
    snack = Entry(NewScreen, width=17)
    snack.place(x=250, y=220)
    SubmitButton = Button(NewScreen, text="Submit", background="white", font=('Times', 12), command=lambda:final(NewScreen, Name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))
    SubmitButton.place(x=150, y=270)

    NewScreen.mainloop()


def Story2(window):
    def final(tl: Toplevel, profession, noun, feeling, emotion,verb):
            text = f'''
            When I was a child, I wanted to become a {profession}
          but as I grew up I got into the {noun} and decided to become an
          engineer. Then I went into a job that I was not {feeling} at.
          After getting {emotion} I decided to do what I love.
          Despite getting lower{verb} than I used to get in my previous job.I am feeling
         happy'''

            tl.geometry(newGeometry='1920x1080')

            Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
            Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)
    NewScreen = Toplevel(window, bg='light green')
    NewScreen.title("Ambitions")
    NewScreen.geometry('1920x1080')
    Label(NewScreen, text='Ambitions').place(x=150, y=0)
    Label(NewScreen, text='Enter a profession:').place(x=0, y=35)
    Label(NewScreen, text='Enter a noun:').place(x=0, y=70)
    Label(NewScreen, text='Enter a feeling:').place(x=0, y=110)
    Label(NewScreen, text='Enter a emotion:').place(x=0, y=150)
    Label(NewScreen, text='Enter a verb:').place(x=0, y=190)
    Profession = Entry(NewScreen, width=17)
    Profession.place(x=250, y=35)
    Noun = Entry(NewScreen, width=17)
    Noun.place(x=250, y=70)
    Feeling = Entry(NewScreen, width=17)
    Feeling.place(x=250, y=105)
    Emotion= Entry(NewScreen, width=17)
    Emotion.place(x=250, y=150)
    Verb = Entry(NewScreen, width=17)
    Verb.place(x=250, y=190)
    SubmitButton = Button(NewScreen, text="Submit", background="white", font=('Times', 12), command=lambda:final(NewScreen, Profession.get(), Noun.get(), Feeling.get(), Emotion.get(), Verb.get()))
    SubmitButton.place(x=150, y=270)
  

def Story3(window):
    def final(tl: Toplevel, animal, place, action, emotion, food):
        text = f'''
        Once upon a time, there was a {animal} living in {place}.
        One day, it decided to {action} which made everyone feel {emotion}.
        To celebrate, they all gathered and enjoyed a feast of {food}.
        It was a day filled with joy and laughter, creating memories that would last forever.'''

        tl.geometry(newGeometry='1920x1080')

        Label(tl, text='Story:', wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)

    NewScreen = Toplevel(window, bg='light blue')
    NewScreen.title("The Adventure of a Creature")
    NewScreen.geometry('1920x1080')
    Label(NewScreen, text='The Adventure of a Creature').place(x=100, y=0)
    Label(NewScreen, text='Enter an animal:').place(x=0, y=35)
    Label(NewScreen, text='Enter a place:').place(x=0, y=70)
    Label(NewScreen, text='Enter an action:').place(x=0, y=110)
    Label(NewScreen, text='Enter an emotion:').place(x=0, y=150)
    Label(NewScreen, text='Enter a food:').place(x=0, y=190)
    Animal = Entry(NewScreen, width=17)
    Animal.place(x=250, y=35)
    Place = Entry(NewScreen, width=17)
    Place.place(x=250, y=70)
    Action = Entry(NewScreen, width=17)
    Action.place(x=250, y=105)
    Emotion = Entry(NewScreen, width=17)
    Emotion.place(x=250, y=150)
    Food = Entry(NewScreen, width=17)
    Food.place(x=250, y=190)
    SubmitButton = Button(NewScreen, text="Submit", background="white", font=('Times', 12),
                          command=lambda: final(NewScreen, Animal.get(), Place.get(), Action.get(), Emotion.get(),
                                                Food.get()))
    SubmitButton.place(x=150, y=270)

    NewScreen.mainloop()


Screen = Tk()
Screen.title("Mad_libs Game")
Screen.geometry('700x700')
Screen.config(bg="orange")
Label(Screen, text='Choose a topic', font=("Times New Roman", 24)).place(x=150, y=20)
Story1Button = Button(Screen, text='A memorable day', font=("Times New Roman", 18),command=lambda: Story1(Screen),bg='red')
Story1Button.place(x=140, y=90)
Story2Button = Button(Screen, text='Ambitions', font=("Times New Roman", 18),command=lambda: Story2(Screen), bg='red')
Story2Button.place(x=140, y=250)
Story3Button = Button(Screen, text='The Adventure of a Creature', font=("Times New Roman", 18), command=lambda: Story3(Screen), bg='red')
Story3Button.place(x=140, y=410)


Screen.update()
Screen.mainloop()
