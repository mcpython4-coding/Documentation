***StatePartConfigBackground.py - documentation - last updated on 8.6.2020 by uuk***
___

    class BackgroundHandler

        variable batch

        variable objects

        variable background_raw: PIL.Image.Image

        variable background_size

        variable background_image

        variable old_win_size

        static
        function recreate(cls, wx, wy)

    class StatePartConfigBackground extends mcpython.state.StatePart.StatePart

        function activate(self)

        function bind_to_eventbus(self)

        function draw(self): BackgroundHandler.batch.draw()
                
                def resize(self, x, y): BackgroundHandler.recreate(x, y)
                
                

        function resize(self, x, y): BackgroundHandler.recreate(x, y)
                
                