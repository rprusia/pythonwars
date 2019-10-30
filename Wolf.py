# A wolf in sheep's clothing
# Wolves have been reintroduced to Great Britain. You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.
#
# Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue which is at the end of the array:
#
# [sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
# 7      6      5      4      3            2      1
# If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep".
# Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's
# position in the queue.
#
# Note: there will always be exactly one wolf in the array.
#
# Examples
# warn_the_sheep(["sheep", "sheep", "sheep", "wolf", "sheep"]) == 'Oi! Sheep number 1!
# You are about to be eaten by a wolf!'
#
# warn_the_sheep(['sheep', 'sheep', 'wolf']) == 'Pls go away and stop eating my sheep'

def warn_the_sheep(queue):
    queue.reverse()
    wolf = queue.index('wolf')
    print(wolf)
    if wolf == 0:
        print('Pls go away and stop eating my sheep')
    else:
       print ("Oi! Sheep number " + str(wolf) + "! You are about to be eaten by a wolf!")


def main():
    lista = ['wolf', 'sheep','sheep','sheep','sheep','sheep','sheep']
    warn_the_sheep(lista)

if __name__ == "__main__":
    main()