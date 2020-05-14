***Registry.py - documentation - last updated on 14.5.2020 by uuk***
___

    class IRegistryContent

        variable NAME

        variable TYPE

        static function on_register(cls, registry)

        variable INFO - can be used to display any special info in e.g. /registryinfo-command

        static function compressed_info(cls)

    class Registry

        function __init__(self, name: str, registry_type_names

        function is_valid(self, obj: IRegistryContent)

        function register(self, obj: IRegistryContent, override_existing=True)

        function lock(self)

        function unlock(self)

    class RegistryInjectionHolder

        function __init__(self, *args, **kwargs):   # todo

            variable self.args

            variable self.kwargs

            variable self.injectable

        function __call__(self, obj)

    class RegistryHandler

        function __init__(self)

            variable self.registries

        function __call__(self, *args, **kwargs)

        function get_by_name(self, name: str) -> Registry

        function register(self, *args, **kwargs)

    variable G.registry