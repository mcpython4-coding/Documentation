***mcpython.py - documentation - last updated on 8.6.2020 by uuk***
___

    variable DEFAULT_OUTPUT - where to output data - in dev environment

        variable DEFAULT_OUTPUT - when we are not in dev-environment, store them when needed in G.local

    function generate_slab(config, name, base)

    function generate_stair(config, name, base)

    function generate_wall(config, name, base)

    function generate_wooded_recipes(config: Configuration.DataGeneratorConfig, w: str)

    @G.modloader("minecraft", "special:datagen:configure")
    function generate_recipes()