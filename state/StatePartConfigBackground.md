***StatePartConfigBackground.py - documentation - last updated on 14.5.2020 by uuk***
___

    class BackgroundHandler

        variable batch


        variable objects


        variable background_raw: PIL.Image.Image


        variable background_size


        variable background_image


        variable old_win_size

        static function recreate(cls, wx, wy)

    class StatePartConfigBackground extends state.StatePart.StatePart
        function activate(self)
        function bind_to_eventbus(self)
        function draw(self)
        function resize(self, x, y)