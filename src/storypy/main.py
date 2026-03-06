import inspect
import keyword
import sys
from typing import Any, Literal

class StoryPy_Core:
    @staticmethod
    def declare(category: Literal["variable"], name: str, value: Any) -> None:
        """
        Declare a new entity inside the caller's global namespace.
        """
        if category.strip().lower() == "variable":
            global valid
            valid = lambda s: s.isidentifier() and not keyword.iskeyword(s) and all(c.isascii() for c in s)

            if valid(name):
                _caller_frame = inspect.stack()[1]
                _caller_globals = _caller_frame.frame.f_globals
                _caller_globals[name] = value
            
            else:
                raise SyntaxError(f"Illegal variable name {name}")
            
        else:
            raise ValueError(f"Unrecognized category {category}")

declare = StoryPy_Core.declare

if __name__ == "__main__":
    print("The StoryPy module is not intended to be run standalone.")
    print("Try importing StoryPy in your project.")

