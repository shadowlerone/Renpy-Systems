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
    from systems.item import Item
    from systems.game import Game
    from systems.quests import Quest, QuestStage
    from systems.recipe import Recipe
    game = Game()
    one = "one_%s.png"
    paint_bucket = Item("paint_bucket", "Bucket of Paint", "It's a... bucket. Full of paint.", "bucket", "bucket")
    burger_crust = Item("burger_crust", "A Burger Crust", "What is this???", one, one)
    lost_fedora = Item("lost_fedora", "A Lost Fedora", "It's a lost fedora. Do they miss it as much as I miss my coat? Who knows.", one, one)

    empty_bucket = Item("bucket", "Empty Bucket", "A nice and dirty bucket", one , one)
    paint_tube = Item("paint_tube", "A paint tube", "It's a tube of paint.", one, one)
    empty_tube = Item("empty_tube", "An empty tube", "Empty Tube of Paint", one, one)
    paint_bucket_recipe = Recipe(
        id = "paint_bucket_recipe",
        name = "Making: A Bucket of Paint",
        requirements = [("bucket", 1), ("paint_tube", 3)],
        items = [("empty_tube", 3), ("paint_bucket", 1)],
        description = ''
    )

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
                                ("lost_fedora", 1)
                            ],
                            "all": True,
                        }}
                    ),
                ],
                requirements={
                    "substage": "all"
                }
            ),
            QuestStage(
                id=30,
                parent_quest_id ="test_quest",
                name = "Return to Eye Guy",
                description = "I should return to eye guy with stuff...",
                next_stage = None,
            )


        ],
        first_stage = 0,
        final_stage = 30
    )
    
    
    game.setup(items = [paint_bucket, burger_crust, lost_fedora, empty_bucket, paint_tube, empty_tube], recipes = [paint_bucket_recipe], quests = [test_quest])
    game.player.recipebook.add_recipe(paint_bucket_recipe)


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

    return
    # Eye guy disappears
    # Quest complete
    # gain item: mysterious




screen main_loop:
    tag menu
    zorder 3

    # text "Hello, World."

    frame:
        xpadding 10
        ypadding 10
        xalign 0.0
        yalign 0.0
        hbox:

            # textbutton "Quests" action Show("quests")
            textbutton "Crafting" action Show("crafting")
            textbutton "Get your items!" action Show("get_items")
            textbutton "Inventory!" action Show("inventory")
            textbutton "Eye Guy":
                action [
                    SensitiveIf(any([
                        q.complete for q in game.player.questlog['test_quest'].get_stage(0).substages
                    ])),
                    Jump("return_objects_all" if game.player.questlog['test_quest'].current_stage >= 30 else "return_objects_some")
                ]
    
    frame:
        xpadding 25
        ypadding 25
        xalign 1.0
        yalign 0.15
        
        hbox:
            vbox: 
                label "Quests!"
                null height 10
                for i, q in enumerate(game.player.questlog.get_active()):
                    textbutton "{1} {0}".format(q.name, "✓" if q.complete else "◇") action Function(game.player.questlog.set_selected_quest, q.id)
            vbox:
                label game.player.questlog.selected_quest.name
                text game.player.questlog.selected_quest.description
                null height 40
                label "Completed objectives"
                null height 20
                # vbox:
                #     for ss in [s for s in game.player.questlog.selected_quest.stages if s.complete]:
                #         label "{1} {0}".format(ss.name, "✓" if ss.complete else "◇")
                #         text ss.description
                #         null height 10
                label "Current Objective {}".format(game.player.questlog.selected_quest.get_stage().name)
                text game.player.questlog.selected_quest.get_stage().description
                null height 20
                vbox:
                    for ss in game.player.questlog.selected_quest.get_stage().substages:
                        label "{1} {0}".format(ss.name, "✓" if ss.complete else "◇")
                        text ss.description
                        null height 10

screen quests:
    zorder 2
    
    # modal True
    # size_group "menu_overlay"
    frame:
        xpadding 25
        ypadding 25
        xalign 1.0
        yalign 0.15
        
        hbox:
            vbox: 
                label "Quests!"
                null height 10
                for i, q in enumerate(game.player.questlog.get_active()):
                    textbutton "{1} {0}".format(q.name, "✓" if q.complete else "◇") action Function(game.player.questlog.set_selected_quest, q.id)
            vbox:
                label game.player.questlog.selected_quest.name
                text game.player.questlog.selected_quest.description
                null height 40
                label "Current Objective {}".format(game.player.questlog.selected_quest.get_stage().name)
                text game.player.questlog.selected_quest.get_stage().description
                null height 20
                vbox:
                    for ss in game.player.questlog.selected_quest.get_stage().substages:
                        label "{1} {0}".format(ss.name, "✓" if ss.complete else "◇")
                        text ss.description
                        null height 10

                

screen crafting:
    tag menu_overlay
    
    zorder 2
    # size_group "menu_overlay"
    frame:
        xpadding 25
        ypadding 25
        xalign 0.10
        yalign 0.15
        
        hbox:
            vbox:
                label "Crafting"
                null height 20
                label "Craftable"
                for r in game.get_craftable():
                    textbutton r.name action Function(game.craft, paint_bucket_recipe)
                null height 20
                label "Uncraftable"
                for r in game.get_uncraftable():
                    text r.name


screen inventory:
    tag menu_overlay

    zorder 2

    frame:
        xpadding 25
        ypadding 25
        xalign 0.10
        yalign 0.15
        vbox:
            label "Inventory!"
            for i in game.player.inventory.get_items():
                text "{}: {}".format(i.name, i.count)
        # vpgrid:
        #     cols 4
        #     spacing 5
        #     mousewheel True
        #     scrollbars "vertical"

        #     side_xalign 0.5

        #     for i in game.player.inventory.items.values():
        #         imagebutton auto i.icon_path:
        #             xysize (200, 200)

screen get_items:
    tag menu_overlay
    zorder 2
    # modal True
    # size_group "menu_overlay"
    frame:
        xpadding 25
        ypadding 25
        xalign 0.10
        yalign 0.15
        vbox:
            label "Items! Get your items here!"
            for i in [burger_crust, lost_fedora, empty_bucket, paint_tube]:
                textbutton i.name action Function(game.add_item, i, 1)

    