import time
import random

anime = [['maria the virgin witch','12 episodes/1 season',('comedy','historical','fantasy')],
       ['cat planet cuties','13 episodes/1 season',('sci-fi','comedy')],
       ['love to lie angle','9 episodes/1 season',('romance')],
       ['kiss x sis','12 episodes/1 season',('romance','comedy')],
       ['nana to kaoru','18 episodes/1 season',('romance','comedy')],
       ['pandora in the crimson shell','12 episodes/1 season',('comedy','sci-fi','cyberpunk')],
       ['valkyrie drive','12 episodes+6 specials/1 season',('romance','supernatural')],
       ['queens blade','3 seasons',('action','fiction')],
       ['freezing','12 episodes/1 season',('action','fiction')],
       ['psycho pass','22 episodes/3 seasons',('crime','cyberpunk','thriller')],
       ['serial experiment lain','13 epsidoes/1 season',('cyberpunk','psychological')],
       ['ego proxy','23 episodes/1 season',('cyberpunk','adventure','psychological')],
       ['nana','47 episodes',('musical','romance')],
       ['neon genesis','26 episodes',('apocalyptic','mecha','psychological','drama')],
       ['terror in resonance','11 episodes/1 season',('psychological','thriller')],
       ['classroom of the elite','12 episodes/1 season',('suspense','psychological')]]

def moodDecider(feeling):
    match feeling:
        case 'sad':
            return 'comedy' 
        case 'happy':
            return 'romance' 
        case 'angry':
            return 'action' 
        case 'suprised':
            return 'thriller' 
        case 'afraid':
            return 'adventure' 
        case 'disgusted':
            return 'psychological' 
        case default:
            return "sorry, you'll have to expand your options to match moods."

def chooseAnime(matrix,mood):
    options = []
    if mood == "sorry, you'll have to expand your options to match moods.":
        return "sorry, you'll have to expand your options to match moods."
    else:
        for i in range(len(matrix)):
            genre = matrix[i][2]
            if mood in genre:
                options.append(matrix[i])
        return options
            
def showAnime(li):
    if li == "sorry, you'll have to expand your options to match moods.":
        print("SORRY, you'll have to expand your options to match moods.")
        print("Or you can CHOOSE YOURSELF from this collection:\n")
        for i in range(len(anime)):
            print(f"{anime[i][0].title()} - genres are {anime[i][2]}")
    else:
        try:
            ind = len(li)
            choice = random.randint(0,ind)
            series = li[choice]
            name = series[0]
            length = series[1]
            genre = series[2]
            print('The computer is deciding...')
            time.sleep(5)
            print('Done!')
            print(f"The computer has decided for you to watch:\t{name.title()}")
            print(f"Info:\nThis anime's genres are {genre}, with a wapping {length.title()}")
            print('watch on animixplay.to')
        except AttributeError:
            series = random.choice(li)
            name = series[0]
            length = series[1]
            genre = series[2]
            print('The computer is deciding...')
            time.sleep(5)
            print('Done!')
            print(f"The computer has decided for you to watch:\t{name.title()}")
            print(f"Info:\nThis anime's genres are {genre}, with a wapping {length.title()}")
            print('watch on animixplay.to')
    
        
    
print('How are you feeling today?(happy/sad/angry/suprised/afraid/other)')
user = input()

showAnime(chooseAnime(anime,moodDecider(user)))

