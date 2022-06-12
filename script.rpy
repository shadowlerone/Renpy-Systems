# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eye Guy")

# init python:
    # from systems.database import Database
    # from systems.inventory import Inventory
    # from systems.recipe import Recipe, RecipeBook
    # from systems.player import Player
    # # print(systems.__all__())
    # # DATABASE = Database()
    # # DATABASE.load_items_from_file(renpy.file('data/items.json'))
    # # DATABASE.load_recipes_from_file(renpy.file('data/recipes.json'))

    # game.people['eye_guy'] = Person("")
    
    # player = Player()

    # inventory.add_recipe(DATABASE.get_recipe('a pretty shoe'))
    # inventory.add_recipe()

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Psst hey, hey big corporate landlord in waiting, psst."
    e "I heard you're looking for your coat, don't ask from where, I have my sources."
    e "What if, I told you, I can help you find it."
    e "Of course, this ain't gonna come gonna come for free ya know. I'm gonna need a bit of... convincing..."

    e "Find me a couple of things, and I'll get you what I think you need."

    menu:
        "Accept":
            "Sure, why not, I can trust your info."
            # Start quest
        "Deny":
            "Um nah, eye guy, you're full of baloney."

    # update quest log

    label return_objects_all:
        e "Here's the thing... you're looking for something, I can tell you what u need to know"
        jump end

    label return_objects_some:
        e "Good good... The bribery-I mean memory jogging equipment, it grows.."
        jump end

    label end:
        e "Clearly you're a good dectective if you can find me all these things."

        # Eye guy disappears
        # Quest complete
        # gain item: mysterious


screen choices:
