import inspect
import makefun
from pydantic.main import ModelMetaclass
from functools import wraps
try:
    from .base_api import BaseAPI
except:
    from base_api import BaseAPI


class API(ModelMetaclass):
    """
        API is a metaclass that `replace` `class` by a `function` (same `__signature__` as `class` has)
        that will instantiate from `class` and then return the result(s) of calls its `run()`
    """
    generic_instantiate_and_call_run = lambda _class: lambda **kwargs: _class(**kwargs).run()

    @staticmethod
    def convert__init__to_instantiate_and_call_run(_class):
        return makefun.create_function(
            func_signature=inspect.signature(_class),
            func_impl=API.generic_instantiate_and_call_run(_class),
            func_name=_class.__name__)

    def __new__(cls, _, bases, dct):
        if BaseAPI not in bases:
            bases = (*bases, BaseAPI)
        class_ = super().__new__(cls, _, bases, dct)
        return cls.convert__init__to_instantiate_and_call_run(class_)

    @classmethod
    def classic(cls, class_):
        return  cls.convert__init__to_instantiate_and_call_run(class_)
