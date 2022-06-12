screen inventory_screen():
    tag example
    zorder 1
    modal False
    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5
        xfill True
        yfill True
        margin (20, 20)
        size_group "full"
        hbox:
            spacing 20
            at transform:
                align (0.5, 0.5) alpha 0.0
                linear 0.5 alpha 1.0
            vbox:
                label "Items!"
                for i, item in inventory.get_items():
                    textbutton i action Function(inventory.set_current_item, item)
            
            vbox:
                label "Current Item"
                vbox:
                    label inventory.current_item.name
                    text inventory.current_item.description

            vbox:
                label "Craftable Recipes!"
                for r in inventory.get_craftable():
                    vbox:
                        textbutton r.name action Function(inventory.craft, r)
                        text "Requirements"
                        for ir, c in r.requirements.items():
                            text "{} x{}".format(ir.name, c)
                label "Uncraftable Recipes"
                for r in inventory.get_uncraftable():
                    vbox:
                        textbutton r.name
                        text "Requirements"
                        for ir, c in r.requirements.items():
                            text "{} x{} ({})".format(ir.name, c, inventory.get_item_count(ir))
            vbox:
                textbutton "Test" action Jump("test")