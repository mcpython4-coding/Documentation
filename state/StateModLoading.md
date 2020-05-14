***StateModLoading.py - documentation - last updated on 14.5.2020 by uuk***
___

    class StateModLoading extends State.State

        variable NAME

        function __init__(self)

        function get_parts(self) -> list

        function bind_to_eventbus(self)

        function on_resize(self, w, h)

                variable part.bboxsize

        function on_draw_2d_pre(self)

                variable part.bboxsize

            variable self.parts[3].position

            variable process

                variable self.parts[3].progress

            variable self.parts[3].text

        function on_update(self, dt)

    variable modloading