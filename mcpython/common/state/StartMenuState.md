***StartMenuState.py - documentation - last updated on 10.1.2022 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    class StartMenu extends mcpython.common.state.AbstractState.AbstractState

        variable NAME

        variable CONFIG_LOCATION

        function __init__(self)

        function bind_to_eventbus(self)

            variable shared.world.world_loaded

            variable shared.ENABLE_ANIMATED_TEXTURES

    variable start_menu

        variable start_menu