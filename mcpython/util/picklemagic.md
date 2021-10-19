***picklemagic.py - documentation - last updated on 19.10.2021 by uuk***
___

    mcpython - a minecraft clone written in python licenced under the MIT-licence 
    (https://github.com/mcpython4-coding/core)
    Contributors: uuk, xkcdjerry (inactive)
    Based on the game of fogleman (https://github.com/fogleman/Minecraft), licenced under the MIT-licence
    Original game "minecraft" by Mojang Studios (www.minecraft.net), licenced under the EULA
    (https://account.mojang.com/documents/minecraft_eula)
    Mod loader inspired by "Minecraft Forge" (https://github.com/MinecraftForge/MinecraftForge) and similar
    This project is not official by mojang and does not relate to it.


    variable __all__

    class FakeClassType extends type
        
        The metaclass used to create fake classes. To support comparisons between
        fake classes and :class:`FakeModule` instances custom behaviour is defined
        here which follows this logic:
        If the other object does not have ``other.__name__`` set, they are not equal.
        Else if it does not have ``other.__module__`` set, they are equal if
        ``self.__module__ + "." + self.__name__ == other.__name__``.
        Else, they are equal if
        ``self.__module__ == other.__module__ and self.__name__ == other.__name__``
        Using this behaviour, ``==``, ``!=``, ``hash()``, ``isinstance()`` and ``issubclass()``
        are implemented allowing comparison between :class:`FakeClassType` instances
        and :class:`FakeModule` instances to succeed if they are pretending to be in the same
        place in the python module hierarchy.
        To create a fake class using this metaclass, you can either use this metaclass directly or
        inherit from the fake class base instances given below. When doing this, the module that
        this fake class is pretending to be in should be specified using the *module* argument
        when the metaclass is called directly or a :attr:``__module__`` class attribute in a class statement.
        This is a subclass of :class:`type`.


        function __new__(cls, name, bases, attributes, module=None)

                variable attributes["__module__"]

        function __init__(self, name, bases, attributes, module=None)

        function __eq__(self, other)

        function __ne__(self, other)

        function __hash__(self)

        function __instancecheck__(self, instance)

        function __subclasscheck__(self, subclass)

    variable FakeClass
        PY2 doesn't like the PY3 way of metaclasses and PY3 doesn't support the PY2 way
        so we call the metaclass directly
    
    A barebones instance of :class:`FakeClassType`. Inherit from this to create fake classes.


    class FakeStrict extends FakeClass,  object

        function __new__(cls, *args, **kwargs)

        function __setstate__(self, state)

    class FakeWarning extends FakeClass,  object

        function __new__(cls, *args, **kwargs)

        function __setstate__(self, state)

                    variable self._setstate_args

    class FakeIgnore extends FakeClass,  object

        function __new__(cls, *args, **kwargs)

        function __setstate__(self, state)

                    variable self._setstate_args

    class FakeClassFactory extends object
        
        Factory of fake classses. It will create fake class definitions on demand
        based on the passed arguments.


        function __init__(self, special_cases=(), default_class=FakeStrict)
            
            *special_cases* should be an iterable containing fake classes which should be treated
            as special cases during the fake unpickling process. This way you can specify custom methods
            and attributes on these classes as they're used during unpickling.
            *default_class* should be a FakeClassType instance which will be subclassed to create the
            necessary non-special case fake classes during unpickling. This should usually be set to
            :class:`FakeStrict`, :class:`FakeWarning` or :class:`FakeIgnore`. These classes have
            :meth:`__new__` and :meth:`__setstate__` methods which extract data from the pickle stream
            and provide means of inspecting the stream when it is not clear how the data should be interpreted.
            As an example, we can define the fake class generated for definition bar in module foo,
            which has a :meth:`__str__` method which returns ``"baz"``::
            class bar(FakeStrict, object):
                def __str__(self):
                    return "baz"
            special_cases = [bar]
            Alternatively they can also be instantiated using :class:`FakeClassType` directly::
            special_cases = [FakeClassType(c.__name__, c.__bases__, c.__dict__, c.__module__)]


            variable self.class_cache

        function __call__(self, name, module)
            
            Return the right class for the specified *module* and *name*.
            This class will either be one of the special cases in case the name and module match,
            or a subclass of *default_class* will be created with the correct name and module.
            Created class definitions are cached per factory instance.


            variable klass

                variable klass
                    generate a new class def which inherits from the default fake class

    class FakeModule extends types.ModuleType
        
        An object which pretends to be a module.
        *name* is the name of the module and should be a ``"."`` separated
        alphanumeric string.
        On initialization the module is added to sys.modules so it can be
        imported properly. Further if *name* is a submodule and if its parent
        does not exist, it will automatically create a parent :class:`FakeModule`.
        This operates recursively until the parent is a top-level module or
        when the parent is an existing module.
        If any fake submodules are removed from this module they will
        automatically be removed from :data:`sys.modules`.
        Just as :class:`FakeClassType`, it supports comparison with
        :class:`FakeClassType` instances, using the following logic:
        If the object does not have ``other.__name__`` set, they are not equal.
        Else if the other object does not have ``other.__module__`` set, they are equal if:
        ``self.__name__ == other.__name__``
        Else, they are equal if:
        ``self.__name__ == other.__module__ + "." + other.__name__``
        Using this behaviour, ``==``, ``!=``, ``hash()``, ``isinstance()`` and ``issubclass()``
        are implemented allowing comparison between :class:`FakeClassType` instances
        and :class:`FakeModule` instances to succeed if they are pretending to bein the same
        place in the python module hierarchy.
        It inherits from :class:`types.ModuleType`.


        function __init__(self, name)

            variable sys.modules[name]

                    variable parent

                    variable parent

        function __repr__(self)

        function __str__(self)

        function __setattr__(self, name, value)

        function __delattr__(self, name)

        function _remove(self)
            
            Removes this module from :data:`sys.modules` and calls :meth:`_remove` on any
            sub-FakeModules.


        function __eq__(self, other)

        function __ne__(self, other)

        function __hash__(self)

        function __instancecheck__(self, instance)

        function __subclasscheck__(self, subclass)

    class FakePackage extends FakeModule
        
        A :class:`FakeModule` subclass which lazily creates :class:`FakePackage`
        instances on its attributes when they're requested.
        This ensures that any attribute of this module is a valid FakeModule
        which can be used to compare against fake classes.


        variable __path__

        function __call__(self, *args, **kwargs)

        function __getattr__(self, name)

    class FakePackageLoader extends object
        
        A :term:`loader` of :class:`FakePackage` modules. When added to
        :data:`sys.meta_path` it will ensure that any attempt to import
        module *root* or its submodules results in a FakePackage.
        Together with the attribute creation from :class:`FakePackage`
        this ensures that any attempt to get a submodule from module *root*
        results in a FakePackage, creating the illusion that *root* is an
        actual package tree.


        function __init__(self, root)

            variable self.root

        function find_module(self, fullname, path=None)

        function load_module(self, fullname)

    class FakeUnpicklingError extends pickle.UnpicklingError
        
        Error raised when there is not enough information to perform the fake
        unpickling process completely. It inherits from :exc:`pickle.UnpicklingError`.


    class FakeUnpickler extends pickle._Unpickler
        
        A forgiving unpickler. On uncountering references to class definitions
        in the pickle stream which it cannot locate, it will create fake classes
        and if necessary fake modules to house them in. Since it still allows access
        to all modules and builtins, it should only be used to unpickle trusted data.
        *file* is the :term:`binary file` to unserialize.
        The optional keyword arguments are *class_factory*, *encoding and *errors*.
        *class_factory* can be used to control how the missing class definitions are
        created. If set to ``None``, ``FakeClassFactory((), FakeStrict)`` will be used.
        In Python 3, the optional keyword arguments *encoding* and *errors* can be used
        to indicate how the unpickler should deal with pickle streams generated in python
        2, specifically how to deal with 8-bit string instances. If set to "bytes" it will
        load them as bytes objects, otherwise it will attempt to decode them into unicode
        using the given *encoding* and *errors* arguments.
        It inherits from :class:`pickle.Unpickler`. (In Python 3 this is actually
        ``pickle._Unpickler``)


        function __init__(self, file, class_factory=None, encoding="bytes", errors="strict")

            variable self.class_factory

        function find_class(self, module, name)

            variable klass

                variable klass

    class SafeUnpickler extends FakeUnpickler
        
        A safe unpickler. It will create fake classes for any references to class
        definitions in the pickle stream. Further it can block access to the extension
        registry making this unpickler safe to use on untrusted data.
        *file* is the :term:`binary file` to unserialize.
        The optional keyword arguments are *class_factory*, *safe_modules*, *use_copyreg*,
        *encoding* and *errors*. *class_factory* can be used to control how the missing class
        definitions are created. If set to ``None``, ``FakeClassFactory((), FakeStrict)`` will be
        used. *safe_modules* can be set to a set of strings of module names, which will be
        regarded as safe by the unpickling process, meaning that it will import objects
        from that module instead of generating fake classes (this does not apply to objects
        in submodules). *use_copyreg* is a boolean value indicating if it's allowed to
        use extensions from the pickle extension registry (documented in the :mod:`copyreg`
        module).
        In Python 3, the optional keyword arguments *encoding* and *errors* can be used
        to indicate how the unpickler should deal with pickle streams generated in python
        2, specifically how to deal with 8-bit string instances. If set to "bytes" it will
        load them as bytes objects, otherwise it will attempt to decode them into unicode
        using the given *encoding* and *errors* arguments.
        This function can be used to unpickle untrusted data safely with the default
        class_factory when *safe_modules* is empty and *use_copyreg* is False.
        It inherits from :class:`pickle.Unpickler`. (In Python 3 this is actually
        ``pickle._Unpickler``)
        It should be noted though that when the unpickler tries to get a nonexistent
        attribute of a safe module, an :exc:`AttributeError` will be raised.
        This inherits from :class:`FakeUnpickler`


        function __init__(
                self,
                file,
                class_factory=None,
                safe_modules=(),
                use_copyreg=False,
                encoding="bytes",
                errors="strict",
                ):

            variable self.safe_modules
                A set of modules which are safe to load

            variable self.use_copyreg

        function find_class(self, module, name)

        function get_extension(self, code)

    class SafePickler extends pickle._Pickler
        
        A pickler which can repickle object hierarchies containing objects created by SafeUnpickler.
        Due to reasons unknown, pythons pickle implementation will normally check if a given class
        actually matches with the object specified at the __module__ and __name__ of the class. Since
        this check is performed with object identity instead of object equality we cannot fake this from
        the classes themselves, and we need to override the method used for normally saving classes.


        function save_global(self, obj, name=None, pack=struct.pack)

    function load(file, class_factory=None, encoding="bytes", errors="errors")
        
        Read a pickled object representation from the open binary :term:`file object` *file*
        and return the reconstitutded object hierarchy specified therein, generating
        any missing class definitions at runtime. This is equivalent to
        ``FakeUnpickler(file).load()``.
        The optional keyword arguments are *class_factory*, *encoding* and *errors*.
        *class_factory* can be used to control how the missing class definitions are
        created. If set to ``None``, ``FakeClassFactory({}, 'strict')`` will be used.
        In Python 3, the optional keyword arguments *encoding* and *errors* can be used
        to indicate how the unpickler should deal with pickle streams generated in python
        2, specifically how to deal with 8-bit string instances. If set to "bytes" it will
        load them as bytes objects, otherwise it will attempt to decode them into unicode
        using the given *encoding* and *errors* arguments.
        This function should only be used to unpickle trusted data.


    function loads(string, class_factory=None, encoding="bytes", errors="errors")
        
        Simjilar to :func:`load`, but takes an 8-bit string (bytes in Python 3, str in Python 2)
        as its first argument instead of a binary :term:`file object`.


    function safe_load(
            file,
            class_factory=None,
            safe_modules=(),
            use_copyreg=False,
            encoding="bytes",
            errors="errors",
            ):
        
        Read a pickled object representation from the open binary :term:`file object` *file*
        and return the reconstitutded object hierarchy specified therein, substituting any
        class definitions by fake classes, ensuring safety in the unpickling process.
        This is equivalent to ``SafeUnpickler(file).load()``.
        The optional keyword arguments are *class_factory*, *safe_modules*, *use_copyreg*,
        *encoding* and *errors*. *class_factory* can be used to control how the missing class
        definitions are created. If set to ``None``, ``FakeClassFactory({}, 'strict')`` will be
        used. *safe_modules* can be set to a set of strings of module names, which will be
        regarded as safe by the unpickling process, meaning that it will import objects
        from that module instead of generating fake classes (this does not apply to objects
        in submodules). *use_copyreg* is a boolean value indicating if it's allowed to
        use extensions from the pickle extension registry (documented in the :mod:`copyreg`
        module).
        In Python 3, the optional keyword arguments *encoding* and *errors* can be used
        to indicate how the unpickler should deal with pickle streams generated in python
        2, specifically how to deal with 8-bit string instances. If set to "bytes" it will
        load them as bytes objects, otherwise it will attempt to decode them into unicode
        using the given *encoding* and *errors* arguments.
        This function can be used to unpickle untrusted data safely with the default
        class_factory when *safe_modules* is empty and *use_copyreg* is False.


    function safe_loads(
            string,
            class_factory=None,
            safe_modules=(),
            use_copyreg=False,
            encoding="bytes",
            errors="errors",
            ):
        
        Similar to :func:`safe_load`, but takes an 8-bit string (bytes in Python 3, str in Python 2)
        as its first argument instead of a binary :term:`file object`.


    function safe_dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)
        
        A convenience function wrapping SafePickler. It functions similarly to pickle.dump


    function safe_dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
        
        A convenience function wrapping SafePickler. It functions similarly to pickle.dumps


    function fake_package(name)
        
        Mounts a fake package tree with the name *name*. This causes any attempt to import
        module *name*, attributes of the module or submodules will return a :class:`FakePackage`
        instance which implements the same behaviour. These :class:`FakePackage` instances compare
        properly with :class:`FakeClassType` instances allowing you to code using FakePackages as
        if the modules and their attributes actually existed.
        This is implemented by creating a :class:`FakePackageLoader` instance with root *name*
        and inserting it in the first spot in :data:`sys.meta_path`. This ensures that importing the
        module and submodules will work properly. Further the :class:`FakePackage` instances take
        care of generating submodules as attributes on request.
        If a fake package tree with the same *name* is already registered, no new fake package
        tree will be mounted.
        This returns the :class:`FakePackage` instance *name*.


    function remove_fake_package(name)
        
        Removes the fake package tree mounted at *name*.
        This works by first looking for any FakePackageLoaders in :data:`sys.path`
        with their root set to *name* and removing them from sys.path. Next it will
        find the top-level :class:`FakePackage` instance *name* and from this point
        traverse the tree of created submodules, removing them from :data:`sys.path`
        and removing their attributes. After this the modules are not registered
        anymore and if they are not referenced from user code anymore they will be
        garbage collected.
        If no fake package tree *name* exists a :exc:`ValueError` will be raised.


        variable package
            Get the package entry via its entry in sys.modules

        variable loaders