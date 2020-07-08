***mcpython.py - documentation - last updated on 8.6.2020 by uuk***
___

    variable TWO_BY_TWO

    variable THREE_BY_THREE

    variable THREE_BY_TWO

    variable TWO_BY_THREE

    variable STAIR

    variable DOWNER_ROW

    variable SMALL_V

    variable SMALL_U

    variable AROUND_HOLLOW

    variable DEFAULT_OUTPUT - where to output data - in dev environment

        variable DEFAULT_OUTPUT - when we are not in dev-environment, store them when needed in G.local

    function generate_slab(config, name, base)

    function generate_above(config, name, base)

    function generate_stair(config, name, base)

    function generate_wall(config, name, base)

    function generate_wooded_recipes(config: Configuration.DataGeneratorConfig, w: str)

    @G.modloader("minecraft", "special:datagen:configure")
    function generate_recipes()
        
        generator for all recipes in minecraft


        variable config

        variable ARMOR

        variable chest

        variable leggings

        variable boots

        variable helmet

        variable sticks

        variable axe

        variable hoe

        variable pickaxe

            variable n

            variable m

            variable n

            variable m

        variable GOLDEN_RECOVER