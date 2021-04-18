***Chat.py - documentation - last updated on 18.4.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    @onlyInClient() class ChatInventory extends mcpython.client.gui.ContainerRenderer.ContainerRenderer
        
        main class for chat


        function __init__(self)
            
            creates an new Chat-instance


            variable self.label

            variable self.enable_blink

            variable self.timer

            variable self.eventbus

        function update_text(self, text: str, underline_index: int)
            
            updates the text displayed by the chat
            :param text: the text to use
            :param underline_index: the index where the "_" is


        function on_activate(self)
            
            called by the system on activation of the inventory


        function on_deactivate(self)
            
            called by the system on deactivation of the inventory


        function draw(self, hovering_slot=None)

    class Chat
        
        main class for chat


        function __init__(self)
            
            creates an new chat


            variable self.text: str

            variable self.history: list

            variable self.history_index

            variable self.active_index

            variable self.CANCEL_INPUT

        function enter(self, text: str)
            
            called when text is entered
            :param text: the text that is entered


        function on_key_press(self, symbol: int, modifiers: int)
            
            called when an key is pressed
            :param symbol: the symbol that is pressed
            :param modifiers: the modifiers that are used
            todo: split up into parts


                variable self.text

                variable self.active_index

                variable self.active_index

                variable self.CANCEL_INPUT

                        variable self.executing_command_info

                        variable self.executing_command_info.chat

                        variable player

                        variable self.executing_command_info.position

                        variable self.executing_command_info.dimension

                variable self.text

                variable self.active_index

                    variable self.text

                    variable self.text

                variable self.active_index

                    variable self.active_index

                    variable self.active_index

        function print_ln(self, text: str)
            
            will print an line into the chat
            :param text: the line to print
            todo: make an in-game chat an link this to there
            todo: make all commands use this as backend


        function close(self)
            
            closes the chat


        function clear(self)
            
            will clear the chat


    variable shared.chat