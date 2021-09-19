***InGameHotKeysManager.py - documentation - last updated on 19.9.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class HotKeyDefinitions extends enum.Enum

        variable RELOAD_CHUNKS

        variable GAME_CRASH

        variable GET_PLAYER_POSITION

        variable CLEAR_CHAT

        variable COPY_BLOCK_OR_ENTITY_DATA

        variable TOGGLE_GAMEMODE_1_3

        variable RELOAD_TEXTURES

        function __init__(self, keys, event, min_press=0)

            variable self.keys

            variable self.event

            variable self.active

            variable self.min_press

            variable self.press_start

        function check(self)

        function blocks(self, symbol, mods) -> bool

    variable ALL_KEY_COMBOS