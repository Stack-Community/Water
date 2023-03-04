<!-- Water"
 is a **modular terminal game engine,** and this page will show you how to use its UI functions. -->

!!! Info
    This documentation page assumes you've installed Water and made a project.

## Setup
We will start by importing the package by using this.
```py
from Water import Engine
```
??? Note
    Engine module is the main module that powers Water itself.

The engine module is split up into submodules with different purposes and features.
For this page, we'll focus on the UI submodule.

Let's make the UI[^1] submodule into a variable we can call on. *(For your sanity)*
```py
from Water import Engine

UI = Engine.UI # User input / interface
```

We've officially set up the foundations of the Water Engine and the submodule called UI.

## Using Water Engine
Using the foundation we've made, we can start using the engine to our needs.

Let's make a call to a function in the UI submodule. To do that, we use these lines of code.

```py
from Water import Engine

UI = Engine.UI # User input / interface

UI.prompt("What's your name?")
```

UI.prompt is the fancy version of asking a question to the user. 
There's an option to make it save the response by making it into a variable.
!!! Tip
    "prompt" function always returns the user input.

    ```py
    response = UI.prompt("What's your name?")
    ```

Let's ask the user a **Yes or No[^2]** question. 
To achieve this, we'll call a different subclass function.
```py
from Water import Engine

UI = Engine.UI # User input / interface

response = UI.prompt("What's your name?")
meet_response = UI.Conditions.meet(f"Ok, {response}. Does apples come from trees?")
```
Conditions are a subclass filled with conditional functions and methods.
So, when we call a function called meet, what we're really doing is asking a true or false statement.

!!! Note
    Conditions.meet has a builtin loop to ensure it gets the right response from a dictionary.

??? Hint
    Conditions.meet also has a configurable default value you can set.
    You can set the default value by doing this
    ```py
    UI.Conditions.meet(f"Ok, {response}. Does apples come from trees?", default_value=Yes)
    ```

Let's use our "meet_response" variable to add a response to the user's choice.
We can achieve this by doing this.

```py
from Water import Engine

UI = Engine.UI # User input / interface

response = UI.prompt("What's your name?")
meet_response = UI.Conditions.meet(f"Ok, {response}. Does apples come from trees?")

if meet_response:
    print("Correct!")
else:
    print("Interesting...")
```

We now have a short trivia quiz using Water. Congrats! 
Everything that powers water is modular so you can use and not use certain modules.

The expected output you should get is the following.
```
What's your name?
John (User input)

Ok, John. Does apples come from trees? | Y or N (Yes or No)
Y (User input)
Correct!

Process finished with exit code 0
```

[^1]: UI means User input

[^2]: "Yes or No" is basically True or false but worded differently
