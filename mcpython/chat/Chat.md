***Chat.py - documentation - last updated on 8.6.2020 by uuk***
___

    class ChatInventory extends mcpython.gui.Inventory.Inventory
        
        main class for chat


        function __init__(self)
            
            creates an new Chat-instance


            variable self.lable

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


        function on_draw_background(self)
            
            called to draw the background of the inventory


        function on_draw_overlay(self)
            
            called to draw the overlay of the inventory


    class Chat
        
        main class for chat


        function __init__(self)
            
            creates an new chat


            variable self.text: str

            variable self.history: list

            variable self.historyindex

            variable self.active_index

            variable self.CANCEL_INPUT

        function enter(self, text: str)
            
            called when text is entered
            :param text: the text that is entered


        function on_key_press(self, symbol, modifiers)
            
            called when an key is pressed
            :param symbol: the symbol that is pressed
            :param modifiers: the modifiers that are used
            todo: split up into parts


        function print_ln(self, text: str)
            
            will print an line into the chat
            :param text: the line to print
            todo: make an in-game chat an link this to there
            todo: make all commands use this as backend


        function close(self)
            
            closes the chat


        function clear(self)
            
            will clear the chat


    variable G.chat