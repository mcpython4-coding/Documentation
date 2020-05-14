***OpenGLSetupFile.py - documentation - last updated on 14.5.2020 by uuk***
___

    variable FILES

    function execute_file_by_name(name, **kwargs)

    class OpenGLSetupFile
        
        Base class for an OpenGL-parse-able file


        static function from_name(cls, name: str)

        static function from_file(cls, file: str)

        function __init__(self, data: str)

            variable self.data

        function execute(self, **kwargs)

                    variable gl_command

                    variable gl_function

                    variable param_raw

                    variable glu_command

                    variable glu_function

                    variable param_raw

                    variable raw

                    variable invoke

        function _transform_value(self, name: str, **kwargs)

                variable t

                variable raw

                variable raw

                variable raw

        function _set_value(self, address, value)

                variable trace

                variable trace