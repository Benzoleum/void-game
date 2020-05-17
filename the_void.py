#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:00:19 2019

@author: nikitakozino
"""
import time

print('\t\t\tThe Void')
time.sleep(3)
print('\t\t\tEpisode 1')
time.sleep(3)
print('\tWritten and created by Nikita Kozino')
time.sleep(4)
print(
    '\n\tThe year is 2516. The beginning of the 25th century. Contrary to the popular belief at the end of the 21st century,'
    ' humanity has not plunged into the everlasting atomic fire and has not met the demise of Sodom and Gomorrah.'
    ' Being on the brink of total destruction countless times, through education and worldwide technological and social innovation,'
    ' humanity has moved the Doomsday Clock hands farthest they have ever been from midnight. In the year 2100 space exploration has been'
    ' made possible by the collaborative work of the major syndicates in America and China. Russia and India dropped out of the Space'
    ' Colonization Race and signed the contract that allowed the US and China to launch interstellar ships into space on the Russian and'
    ' Indian launching pads in exchange for renting American and Chinese ships. After the long-awaited end of global oil dependence through'
    ' the subjugation of solar energy and the cure of all the main deadly diseases, mankind has completely devoted itself to the idea of'
    ' conquering and colonizing outer space. Major nations have started the process of space exploration in the mid 22nd century, by finally'
    ' developing the technology necessary for the warp jump, allowing space ships to travel faster than the speed of light, and now it is'
    ' available to anyone. To anyone with the necessary funds of course.'
)
time.sleep(50)
print('''
      \tYou were found unconscious, drifting in the outer space, wearing merely a protective suit, by a small cargo ship, that is 
delivering supplies from planet 1XD-FA1 (in the nearby galaxy) to the nearest Russian space station “Belka 7”. \tIt appears you 
have lost your memory and remember only your name and very last moments before you lost your memory.'
      ''')
time.sleep(15)


class Player():
    def __init__(self, name, age, hp, inventory, creds):
        self.name = name
        self.age = age
        self.hp = hp
        self.inventory = inventory
        self.creds = creds


class NPC():
    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def getLocation(self):
        return self.__location

    def getName(self):
        return self.__name


x = Player(input('*Please enter a name for your character: '), eval(input('*Please input age for your character: ')),
           65, ['Damaged Suit'], 0)
print('Your character: ', (x.name, x.age))
time.sleep(3)
print('You feel a slap on your face...')
time.sleep(3)


def infirmary_dialogue():
    print("""
        1) -What’s this ship?-
		2) -Who are you?-
		3) -Where are we going?-
		4) -How do I get out of here?-
		5) *exit dialogue*
""")
    choice = eval(input('Please enter 1, 2, 3, 4 or 5: '))
    while choice != 5:
        if choice == 1:
            print('\n- We are a small cargo ship named “Soyuz”.'
                  'It’s just 4 of us operating the ship here. Myself, Anton the cook, engineer Pavel, and the captain of course. -')
            infirmary_dialogue()
            break
        elif choice == 2:
            print(
                '\n- I am Dima. I am this ship’s medic. I’ve been monitoring your condition for the past couple of days -')
            infirmary_dialogue()
            break
        elif choice == 3:
            print('\n- We are going to the “Belka 7” station. It’s a small space hub at this part of the Void. - ')
            infirmary_dialogue()
            break
        elif choice == 4:
            print('\n- Just woke up and already want to get the hell out of here? As soon as we land at “Belka 7”,'
                  'you are free to go wherever you’d like. -')
            infirmary_dialogue()
            break


def Cantina():
    print('You enter a small cantina, that looks more like a small kitchen. Anton is sitting at the table, smoking.'
          'A bottle of vodka stands right beside him.')
    time.sleep(4)
    print('\nThe cook raises his head and smiles.\n- If it\'s not our special guest! How are you feeling, my friend? -')
    time.sleep(3)
    print('\n\t1)- Hey, Anton. Feeling like crap, Dima said you\'ve got something to eat?- ')
    print('\t2)- Just give me something to eat already you dirty drunk. -')

    try:
        choice = eval(input('*Please enter 1 or 2: '))
    except NameError:
        print('Your choice must be in an integer form.')

    if choice == 1:
        print(
            '- But of course, friend. Here, try this... -\n The cook stands up, it seems he lost his coordination after drinking.'
            'He approaches the stove and pours something into a metal plate.')
        time.sleep(5)
        print('\n- Here, friend, try some of my famous hand-made pelmeni. They will do you good. -')
        time.sleep(3)
        x.hp += 25
        print(
            'You sit at the table and eat the "Pelmeni". Little dumplings with beef and pork mix filling\nYou feel better, your health is now:',
            x.hp)
        print('- Thanks Anton. I feel much better now. -\n- Of course friend, if you need more just come back here. -')
    elif choice == 2:
        print('- That''s not how you talk to a friend,', x.name + '. Get the hell out of my kitchen. -')


def EngineRoom():
    print('You enter a dark corridor, at the end you see a dim light. You approach the light and see Pavel the Engineer'
          'sitting at the table and woking on some blueprint. It seems that Pavel haven''t noticed your presence.')
    print('\t1) - Hey Pavel. -')
    print('\t2) - (scare him) -')
    choice = eval(input('*Please enter 1 or 2: '))
    if choice == 1:
        print('- Oh, hi there. Didn\'t see you coming',
              x.name + '. I see you feel better. Say, I couldn\'t help but notice'
                       ' that you are wearing Mark IV Exo-Skeleton Protective Suit. It\'s in a pretty bad condition, so it\'s no good to you.'
                       ' Me, on the other hand, I can make good use of it to repair some external parts of the ship. The material will hold a small'
                       ' asteroid hit. I’ll offer 100 credits for your suit and some of my clothes. You willing to sell? Matter of fact, you are better'
                       ' off without it, as the Federal Security on station will sure start asking questions when they see it, so I am doing you a favor. -')
        time.sleep(10)
        print('\n\t1) - Alright, it\'s pretty badly damaged anyway. -')
        print('\t2) - No. The suit stays on me. -')
        choice2 = eval(input('*Please enter 1 or 2: '))
        if choice2 == 1:
            print('- Smart man! Take this ... -')
            time.sleep(3)
            print(
                'The engineer takes your suit and hands you some old but clean clothes. He turns away and start mumbling to himself, like you never talked.')
            time.sleep(6)
            x.creds += 100
            x.inventory.append('Everyday Suit')
            x.inventory.remove('Damaged Suit')
            print('\n*You sold your Damaged Military Suit. Your inventory is now:', x.inventory)
            print('*You earned some money from the transaction, you have', x.creds, 'credits now.')
        elif choice2 == 2:
            print('- Your loss, partner. Could have saved your ass. -')
    elif choice == 2:
        print('You approach Pavel silently and shout at him.')
        print('Pavel quickly stands up and punches you in the face.')
        print('You fall on the floor. Your nose starts bleeding.')
        x.hp -= 20
        print('Your health is now: ', x.hp)
        print(
            '- Jesus, partner. Who does something like this? What are you 12? Good thing I didn\'t have any weapons on me. Sorry, buddy. -')


def Cockpit():
    print('You enter the Cockpit. A room full of flashing buttons, levers, sensors, screens, touch pads, and more.'
          'All is marked with Russian words and letters, but strangely enough, you feel like you could operate this ship easily.'
          ' In the illuminator you see that the ship is approaching a relatively large space station. Captain is sitting at the very end'
          ' of the cockpit, pushing buttons, and pulling levers. You hear the Captain saying: ')
    time.sleep(5)
    print(
        '\n- Belka 7 Control, this is Soyuz - 8 cargo ship, identification Foxtrot-Charlie-Delta 707. Requesting docking permission, over. - ')
    time.sleep(4)
    print('\nYou hear someone talking indistinclty on the intercom...')
    time.sleep(3)
    print('\nCaptain continues:\n- Copy that Control, beginning docking sequence, Soyuz - 8 over and out. -')
    time.sleep(3)
    print('\nCaptain takes off his headset and turns to you.')
    time.sleep(2)
    print('\n- You are awake. Good. We will be docking with Belka 7 shortly. How are you feeling? -')
    time.sleep(3)
    print('\n\t1) -Better, thanks. Can you tell me more about the space station? -')
    print('\t2) - Just get us to the space station already… I want to be finally off this damn ship. -')
    choice = eval(input('*Please enter 1 or 2: '))
    if choice == 1:
        print(
            '\n- Good. Yeah, I can tell you a thing or two. Belka 7 was built in 2450, at first it was a hub for all of '
            'the ships coming through that part of the Void. Back in the day it was the most prestigious station in the sector,'
            ' finest restaurants, premium quality gear, finest ship service around. It all went to hell around 10 years ago, when the'
            ' Federation built a new station couple parsecs from here. There was a coup some time ago, so now it’s mostly an independent'
            ' station. You might think it\'s good being independent from the Federation, but where is freedom, there are outlaws. So now'
            ' it\'s mostly marauders, pirates and criminals on the station. See this part over there? - captain points to the left of the'
            ' station - that\'s where the cafes and vendors are mostly located - captain now points at the very bottom of the station -'
            ' that\'s where you don\'t want to go. The “Gulag” is located there. A prison for those who disrespect the selfproclaimed'
            ' administration of the station. And the very top part is where the office of the “Headmaster” is located. A blood thirsty'
            ' bastard who made himself a name racketeering and murdering. Anyhow, I advise you to sit, as we are starting the docking'
            ' with the station now. -')
        time.sleep(5)
        print(
            '\nYou sit on the seat beside the captain. The ship enters the hangar of the station and gently lands on the landing pad.')
        time.sleep(4)
    elif choice == 2:
        print('- You aren’t very grateful that we saved you, huh? Whatever, hold on to something, we are landing. -')
        time.sleep(4)
        print(
            '\nYou grab on to the handrail beside the captains seat. The ship enters the hangar of the station and lands harshly.'
            ' You hit your head. Captain is smiling. \n- Bumpy, huh? Maybe you should have waited for a different ship to save you. -')
        time.sleep(5)
        x.hp -= 10
        print('You hit your head, your health is now:', x.hp)


def Customs():
    print(
        '\nYou approach the gate separating the station from the hangar. You see a customs agent sitting behind the bulletproof glass.'
        ' You approach him.')
    time.sleep(4)
    print('\nHe says without raising his eyes:')
    time.sleep(2)
    print('\n- Name and age. -')
    time.sleep(2)
    print('\n\t1) - Hi, my name is', x.name, '. I am', x.age, '.')
    print('\t2)', x.name + ', ', x.age)
    choice = eval(input('*Please enter 1 or 2: '))
    if choice == 1:
        print('\n- Hi, my name is ... -')
        time.sleep(2)
        print('\nCustoms agent interrupts you.')
        time.sleep(2)
        print('\n- I said. Name. And age. I don''t want to hear anything else.')
        time.sleep(3)
        print('-', x.name, ',', x.age, '-')
        time.sleep(2)
        print('- Spell your name. -')
        time.sleep(2)
        print('- It\'s', [e for e in x.name], '. -')
        time.sleep(2)
    elif choice == 2:
        print('- Spell your name. -')
        time.sleep(2)
        print('- It''s', [e for e in x.name], '-')
        time.sleep(3)
    print('An agent gives you a virtual ID card that says: ')
    IDcard = {'Name': x.name, 'ID': 71460, 'Age': x.age}
    time.sleep(3)
    print(IDcard)
    print('\nHe finally raises his head an looks at you.')
    time.sleep(2)
    if x.inventory == ['Damaged Suit']:
        print('\n- Nice suit. American, huh? Wait here. -')
        time.sleep(2)
    else:
        print('\n- Haven\'t seen you here before. Wait here. -')
        time.sleep(2)
    print(
        '\nHe picks up a radio and says something in Russian.\nCouple moments later a thug with a rifle approaches you and says: ')


def Location():
    print('\n\t1) *Go to the cantina.')
    print('\t2) *Go to the engine room. ')
    print('\t3) *Go to the cockpit and land.')
    choice = eval(input('Please enter 1, 2 or 3: '))
    if choice == 1:
        Cantina()
    elif choice == 2:
        EngineRoom()
    elif choice == 3:
        Cockpit()


def InterrogationRoom():
    print('\n- Now-now … - a man in a beret steps out of the darkness, smoking a cigar. - who might that be? -')
    time.sleep(3)
    print('\n\t1) - What is the meaning of this? -')
    print('\t2) - Who are you? -')
    print('\t3) - Where am I? -')
    choice = eval(input('Please enter 1, 2 or 3: '))
    print('\nA man slaps you in the face, not letting you finish.')
    time.sleep(3)
    print('\n- I am the one asking questions. Who are you working for?- ')
    time.sleep(3)
    print('\n\t1)- I am not working for anybody. I lost my memory. I barely remember my name! -')
    print('\t2)- I am with the Soyuz - 8 ship. I am just delivering supplies to the station. -')
    print('\t3)- Go to hell. -')
    choice = eval(input('Please enter 1, 2 or 3: '))
    if choice == 1:
        time.sleep(3)
        print('\n- Oh yes. The “I lost my memory game”. My favorite… - a man pulls out a baton out of his back.'
              ' He turns to a thug who brought you in - I like when they resist… -')
        time.sleep(5)
    elif choice == 2:
        print('\n- Soyuz - 8 ship? Oh, that bucket that is delivering supplies once every two weeks?'
              ' You must be a new crew member', x.name, '? Funny, I thought the ship only holds 4 crew members… -'
                                                        ' a man pulls out a baton out of his back. He turns to a thug who brought you in - I like it'
                                                        ' when they try to come up with a story… -')
        time.sleep(6)
    elif choice == 3:
        print(
            '\n- Ooh, a fighter! I like it! - a man pulls out a baton out of his back. He turns to a thug who brought you in -'
            ' the more they fight, the more interesting it gets… -')
        time.sleep(5)
    print('\nAn interrogator raises a baton over his head, looks you in the eyes and whispers: ')
    time.sleep(3)
    print("\n- You aren\'t gonna love this... -")
    time.sleep(3)
    print('\nAs he is about to hit you with the baton, someone knocks in the door.')
    time.sleep(3)
    print('\n- Goddammit. Egor, see who is there - an interrogator says to a thug.')
    time.sleep(3)
    print(
        '\nEgor opens the door slightly. Says something in Russian. Then approaches a man with a baton and whispers something in his ear.')
    time.sleep(4)
    print('\n- What? This maggot? But see, I was right. He was worth interrogating… Alright, you', x.name[:3], '…'
                                                                                                               ' whatever your name is… The Headmaster wants to see you… Egor, untie him and escort him to the head office. -')
    time.sleep(5)
    print('\nA thug unties you and helps you on your feet.')
    time.sleep(2)
    print('\n- Come - he says')


def HeadmasterOffice():
    time.sleep(5)
    print(
        '\n- Ah, yes. Here he is. - the headmaster is a fat, bald, sweaty man with small eyes. Behind him are two thugs with rifles. - '
        'please', x.name,
        'sit here. - he points at the chair next to his table. He continues - you are lucky I intervened in this little'
        ' misunderstanding, but a man of your status should know that traveling unannounced in this parts of the Void is a little dangerous. -')
    time.sleep(15)
    print('\n\t1) - What are you talking about? -')
    print('\t2) - What is the meaning of this? -')
    print('\t3) - Why did you want to see me? -')
    choice = eval(input('Please enter 1, 2 or 3: '))
    if choice == 1:
        time.sleep(2)
        print('\n- Come on, commander. The interrogation is over. We all know who you are. No point in hiding anymore.'
              ' Someone is here to see you. -')
    elif choice == 2:
        time.sleep(2)
        print('\n- No need to be nervous. Everything is well now, commander. Someone want’s to speak to you. -')
    elif choice == 3:
        time.sleep(2)
        print('\n- Well, it\'s not me. Someone else is here to see you, commander. -')
    time.sleep(3)
    print(
        '\nYou notice a man in the far corner of the room. He is sitting in the dark, and you cannot clearly see who that is. '
        'A man stands up and steps out of the dark. You see him wearing uniform, same as yours when you were caught in space. A man says calmly: ')
    time.sleep(8)
    print('\n- Care to explain yourself, commander', x.name, '? -')


print('\n-Hey, wake up…-\n')
time.sleep(3)
print(
    'Your vision is blurry, your entire body aches, especially the head. The head hurts like you\'ve been hit with a baseball bat.\n')
time.sleep(5)
print(
    'You look around. In front of you is a bald man with a scarred face. You are in what seems to be an infirmary. It’s cramped and'
    ' looks to be very old. You see some surgical instruments hanging on the far wall.\n')
time.sleep(8)
print('-Wake up', x.name + '. It says on this name badge that you are', x.name + '… is that correct?-\n')
time.sleep(3)
print(
    '*At this point you have approached the first decision that you will have to make. Please pick one of the options for what your'
    ' character is going to say. Mind that some of the decisions in the game will have an effect on how your character progresses'
    'through the game and which ending you get*\n')
time.sleep(6)
print('\t1) - What… What happened? Who are you? -')
print('\t2) - (moan in pain) my head… -')

try:
    choice1 = eval(input('*Please enter 1 or 2: '))
except NameError:
    print('Your choice must be in an integer form.')
    choice1 = eval(input('*Please enter 1 or 2: '))

if choice1 == 1:
    print('\n- My name is Dima, do you remember how you got here?-\n')
elif choice1 == 2:
    print('\n- It’ll pass. Just take it easy. Do you remember how you got here?-')

time.sleep(3)
print('\t1) - No -')
print('\t2) - (be silent) -')

try:
    choice2 = eval(input('*Please enter 1 or 2: '))
except NameError:
    print('Your choice must be in an integer form.')

if choice2 == 1:
    print(
        '\n- We’ve caught you in open space. You were drifting through it in only your space suit. Your oxygen levels were at critical,'
        ' that’s why you were unconscious.- ')
elif choice2 == 2:
    print(
        '\n- You are in shock, but it''ll pass. We’ve caught you in space. You were drifting through it in only your space suit. '
        'Your oxygen levels were at critical levels, that’s why you were unconscious.- ')

time.sleep(3)
print('\n- What?.. You caught me in space? -')
time.sleep(3)
print('\n- Yes, we’ve pulled you into the ship a day ago. You’ve been unconscious ever since.-')

infirmary_dialogue()

print('\n- I don’t remember anything, just my name. Do you know what happened? -')
time.sleep(3)
print('\n- Well, I’ll be honest with you',
      x.name + '. By the looks of your space suit, you’ve been in quite a situation. '
               'See these burnt and ripped parts? It’s as almost it caught on fire somehow or something hit you. However your suit is an'
               ' expensive, military grade protective gear. It absorbed much of the damage, but it’s no good to you in such condition. You'
               ' remember anything yourself? -')
time.sleep(10)

print('\n\t1) - I remember a blast. Something hit me… then a light flash… next thing I know, I am here. -')
print('\t2) - (be silent) - ')

try:
    choice7 = eval(input('*Please enter 1 or 2: '))
except NameError:
    print('Your choice must be in an integer form.')

if choice7 == 1:
    print(
        '\n- It seems that your ship was either attacked by marauders, or something malfunctioned, which led to an explosion. It'
        ' doesn’t happen often, especially with military cruisers, but who knows… either way, go talk to the crew, some of them might'
        ' help you prepare for your journey. -')
    time.sleep(10)
elif choice7 == 2:
    print(
        '\n- It’s alright, your memory might come back to you later. In the meantime, go talk to the crew, some of them might help'
        ' you prepare for your journey. -')
    time.sleep(4)

print(
    '\nDima helps you get down from the surgical bed you\'ve been on. Your back hurts, your vision is still blurry. Before you step outside '
    'the infirmary, Dima says: ')
time.sleep(5)
print('\n- If I were you',
      x.name + ', I would go see Anton the cook. He is a drunkard, but has a good heart. You look pretty terrible,'
               ' maybe some food will help you get better. -')
time.sleep(5)

Location()
Location()
Location()

print(
    '\nYou step out of the ship into a huge hangar. You see all varieties of ships departing and landing. Some are marked with French flags,'
    ' some Chinese, some Russian. People are running around, automechanical bots are moving crates.')
time.sleep(8)

Customs()

print('\n -Come this way. -')
print('\n\t1) - (follow the thug) -')
print('\t2) - I am not going anywhere with you. -')
print('\t3) - Go to hell. -')
time.sleep(5)

try:
    choice8 = eval(input('*Please enter 1, 2 or 3: '))
    time.sleep(3)
except NameError:
    print('Your choice must be in an integer form.')

if choice8 == 1:
    print(
        'A thug grabs you by your arm and pulls you towards an armored door. He opens it, you see a bloody chair in the center of the room.'
        ' A thug pushes you onto the chair and ties you up.')
    time.sleep(5)
elif choice8 == 2:
    print('A thug punches you in the face. Your nose starts bleeding.')
    x.hp -= 10
    print('\nYou health is now:', x.hp)
    time.sleep(2)
    print(
        '\nA thug grabs you by your arm and pulls you towards an armored door. He opens it, you see a bloody chair in the center of'
        ' the room. A thug pushes you onto the chair and ties you up.')
    time.sleep(5)

    time.sleep(5)
elif choice8 == 3:
    print('A thug punches you in the face with a rifle. You fall unconscious on the floor…')
    time.sleep(5)
    x.hp -= 50
    print('Your health is now:', x.hp)
    time.sleep(5)
    print('You wake up sitting tied to a bloody chair in the middle of a dimmed room.')

InterrogationRoom()
time.sleep(5)
print(
    '\nYou exit the interrogation room and take an elevator to the top of the station. You enter a large office with a window at the back of the room overseeing an entire station.')
time.sleep(5)
HeadmasterOffice()

time.sleep(5)
print('\n\t...Episode 2 coming January 2020')
time.sleep(5)

print(
    '\nThis is a work of fiction. Names, characters, businesses, places, events, locales, and incidents are either the'
    ' products of the author\'s imagination or used in a fictitious manner. Any resemblance to actual persons, living or dead,'
    ' or actual events is purely coincidental.')
time.sleep(10)
print('\n Boston. 2019')
