***StateModLoading.py - documentation - last updated on 19.1.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under MIT-licence
    authors: uuk, xkcdjerry (inactive)
    based on the game of fogleman (https://github.com/fogleman/Minecraft) licenced under MIT-licence
    original game "minecraft" by Mojang Studios (www.minecraft.net)
    mod loader inspired by "minecraft forge" (https://github.com/MinecraftForge/MinecraftForge)
    blocks based on 20w51a.jar of minecraft, representing snapshot 20w51a
    (https://www.minecraft.net/en-us/article/minecraft-snapshot-20w51a)
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class StateModLoading extends State.State

        variable NAME

        function __init__(self)

        function get_parts(self) -> list

        function bind_to_eventbus(self)

        function on_resize(self, w, h)

        function on_draw_2d_pre(self)

        function on_update(self, dt)

    variable modloading