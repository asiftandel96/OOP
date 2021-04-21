"""Now, you add the AsDictionaryMixin class:"""


class AsDictionaryMixin:

    def to_dict(self):
        return {
            prop: self._represent(value)
            for prop, value in self.__dict__.items()
            if not self._is_internal(prop)
        }

    def _represent(self, value):

        if isinstance(value, object):
            if hasattr(value, 'to_dict'):
                return value.to_dict()
            else:
                return str(value)
        else:
            return value

    def _is_internal(self, prop):
        return prop.startswith('_')


"""The AsDictionaryMixin class exposes a .to_dict() method that returns the representation of itself as a dictionary. The method is implemented as a dict comprehension that says, “Create a dictionary mapping prop to value for each item in self.__dict__.items() if the prop is not internal.”

Note: This is why we made the role and payroll attributes internal in the Employee class, because we don’t want to represent them in the dictionary.

As you saw at the beginning, creating a class inherits some members from object, and one of those members is __dict__, which is basically a mapping of all the attributes in an object to their value.

You iterate through all the items in __dict__ and filter out the ones that have a name that starts with an underscore using ._is_internal().

._represent() checks the specified value. If the value is an object, then it looks to see if it also has a .to_dict() member and uses it to represent the object. Otherwise, it returns a string representation. If the value is not an object, then it simply returns the value.

You can modify the Employee class to support this mixin:"""
