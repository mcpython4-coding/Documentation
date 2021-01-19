***util.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    variable __all__

    @onlyInClient()
    function setup()

        variable pyglet.image.Texture.default_min_filter

        variable pyglet.image.Texture.default_mag_filter

    @onlyInClient()
    function setup_fog()

    @onlyInClient()
    function draw_line_box(vertex)

    @onlyInClient()
    function set_2d(viewport, width, height)

    @onlyInClient()
    function set_3d(viewport, width, height, rotation, trans_rotation, position)

    @onlyInClient()
    function enableAlpha()

    @onlyInClient()
    function disableAlpha()