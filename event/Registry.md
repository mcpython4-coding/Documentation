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

            variable self.name

            variable self.registry_type_names

            variable self.injection_function

            variable self.allow_argumented_injection

            variable self.registered_object_map

            variable self.locked

            variable self.class_based

            variable self.CANCEL_REGISTRATION

        function is_valid(self, obj: IRegistryContent)

        function register(self, obj: IRegistryContent, override_existing=True)

            variable self.CANCEL_REGISTRATION

            variable self.registered_object_map[obj.NAME]

        function lock(self)

        function unlock(self)

    class RegistryInjectionHolder

        function __init__(self, *args, **kwargs):   # todo

            variable self.args

            variable self.kwargs

            variable self.injectable

        function __call__(self, obj)

            variable self.injectable

    class RegistryHandler

        function __init__(self)

            variable self.registries

        function __call__(self, *args, **kwargs)

        function get_by_name(self, name: str) -> Registry

        function register(self, *args, **kwargs)

    variable G.registry