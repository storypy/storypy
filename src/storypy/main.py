#!/usr/bin/python3

import keyword
import sys
from typing import Any, Literal

class StoryPy_Core:
    @staticmethod
    def declare(category: Literal["variable"], name: str, value: Any) -> None:
        """
        Declare a new entity inside the caller's global namespace.

        Currently only ``"variable"`` declarations are supported.

        Args:
            category (Literal["variable"]):
                The type of entity to declare.
            name (str):
                The name of the variable to create.
            value (Any):
                The value assigned to the declared variable.

        Raises:
            SyntaxError:
                If ``name`` is not a valid Python identifier or is a reserved keyword.
            ValueError:
                If an unsupported ``category`` is provided.

        Example:
            >>> StoryPy_Core.declare("variable", "x", 42)
            >>> x
            42

        See Also:
            :mod:`sys`
            :func:`keyword.iskeyword`
        """
        if category.strip().lower() == "variable":
            global valid
            valid = lambda s: s.isidentifier() and not keyword.iskeyword(s) and all(c.isascii() for c in s)

            if valid(name):
                _caller = sys.modules["__main__"]
                _caller.__dict__[name] = value
            
            else:
                raise SyntaxError(f"Illegal variable name {name}")
            
        else:
            raise ValueError(f"Unrecognized category {category}")

declare = StoryPy_Core.declare

if __name__ == "__main__":
    print("The StoryPy module is not intended to be run standalone.")
    print("Try importing StoryPy in your project.")

