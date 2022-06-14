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

init python:
    from systems.player import Player
    from systems.game import Game
    from systems.quests import Quest, QuestStage
    game = Game()

    test_quest = Quest(
        "test_quest",
        "A Test Quest",
        "This quest is but a test. Eye is testing you. Do not fail.",
        stages=[
            QuestStage(
                id=0,
                parent_quest_id ="test_quest",
                name = "Eye Guy's Mission",
                description = "I need to find this... stuff... for Eye Guy.",
                next_stage = 30,
                substages = [
                    QuestStage(
                        5,
                        "test_quest",
                        "Find {b}Bucket of Paint{/b}",
                        "I need to somehow find this item...",
                        next_stage = None,
                        requirements = {"item": {
                            "ids":[
                                ("paint_bucket", 1)
                            ],
                            "all":True,
                        }}
                    ),
                    QuestStage(
                        15,
                        "test_quest",
                        "Find {b}Burger Crust{/b}",
                        "I need to somehow find this item...",
                        next_stage = None,
                        requirements = {"item": {
                            "ids":[
                                ("burger_crust", 1)
                            ],
                            "all": True,
                        }}
                    ),
                    QuestStage(
                        25,
                        "test_quest",
                        "Find {b}Lost Fedora{/b}",
                        "I need to somehow find this item...",
                        next_stage = None,
                        requirements = {"item": {
                            "ids":[
                                ("burger_crust", 1)
                            ],
                            "all": True,
                        }}
                    ),
                ],
                requirements={
                    "substage": "all"
                }
            )

        ],
        first_stage = 0,
        final_stage = 30
    )


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
            $ game.start_quest("test_quest", quest_object = test_quest)
            call screen main_loop
            # Start quest
        "Deny":
            "Um nah, eye guy, you're full of baloney."
            jump denied

    
    # update quest log
label denied:
    e "k byyeyeyeyeyeyeyeyeyeyeyeyeyeyeyyyyyyyeeeeeeee."
    return

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




screen main_loop:
    tag menu
    zorder 1
    modal True

    text "Hello, World."

screen quests:
    tag menu_overlay
    zorder 2

    modal True

    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5

        vbox:
            text "Quests!"
            null height 10
            for i, q in enumerate(game.player.questlog.get_active()):
                text q.name

screen get_items:
    tag menu_overlay
    zorder 2
    modal True

    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5

        vbox:
            text "items!"
    
