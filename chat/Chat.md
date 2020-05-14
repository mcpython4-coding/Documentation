***Chat.py - documentation - last updated on 14.5.2020 by uuk***
___

    class ChatInventory extends gui.Inventory.Inventory
        
        main class for chat


        function __init__(self, *args, **kwargs)

            variable self.lable

            variable self.enable_blink

            variable self.timer

            variable self.eventbus

        function update_text(self, text, underline_index)

                variable self.lable.text

                variable self.lable.text

                variable self.lable.text - 5;</span></font>"

        function on_activate(self)

            variable G.chat.text

            variable G.chat.active_index

            variable G.chat.has_entered_t

        function on_deactivate(self)

        function on_draw_background(self)

        function on_draw_overlay(self)

            variable text

                variable self.lable.text

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


            variable self.text

        function on_key_press(self, symbol, modifiers)
            
            called when an key is pressed
            :param symbol: the symbol that is pressed
            :param modifiers: the modifiers that are used


                variable self.text

                variable self.text

                variable self.active_index - begin key

                variable self.active_index

                variable self.CANCEL_INPUT

                variable self.text

                variable self.active_index

                    variable self.text

                    variable self.text

                variable self.active_index

                    variable self.active_index

                    variable self.active_index

        function print_ln(self, text: str)

        function close(self)
            
            closes the chat


            variable self.active_index

        function clear(self)

    variable G.chat