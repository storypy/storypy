Using StoryPy
=============

First of all, to use the StoryPy module in your project, you need to include it::

    import storypy

After the module is included, all its objects will be available.

The ``declare`` function
------------------------

You can use the ``storypy.declare()`` function to declare variables in the caller's global namespace (scope selection is not yet supported, but planned).

    Note that if the specified entity already exists, the ``declare`` function will override it without confirmation.

Usage
^^^^^

The ``declare`` function needs three inputs: ``category``, ``name``, and ``value``, as shown below::

    storypy.declare(category: str, name: str, value: Any)

The ``category`` input specifies the category of the entity you are declaring (e.g. "variable", "function"). Must be a string.

    For now, only the "variable" category can be entered, meaning you can only declare variables with the ``declare`` function. Other categories are planned to be added in the future.

The ``name`` input specifies the name of the entity you are declaring. If the "variable" category is set, this will be the name of the created variable. Must be a string.

The ``value`` input specifies the value of the entity you are declaring. If the "variable" category is set, this will be the value of the created variable. Can have any type.

Examples
^^^^^^^^

So we'd like to create a variable called "one", with the integer value of 1. We can do this by running::

    storypy.declare("variable", "one", 1)

And that's it. Now, the ``one`` variable will be available in our program's globals.
