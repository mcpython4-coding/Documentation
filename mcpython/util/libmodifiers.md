***libmodifiers.py - documentation - last updated on 30.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    function applyPillowPatches()

        variable method

        variable method.code_string[27] - LOAD_GLOBAL BICUBIC -> NEAREST

    function removeLaunchWrapperPyVersionCheck()
        
        Util method to be invoked by the launcher to disable the python version checker on launch.
        This is needed as the launcher may decide to use a newer python version than we have support for.


        variable method

        variable method.code_string[0] - LOAD_CONST

        variable method.code_string[1] - None

        variable method.code_string[2] - return value

        variable method.code_string[3]