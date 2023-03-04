This holds all API References used the **"Water-GM"** pip library. 

!!! Warning
    Some API References are unreliable, broken, or deprecated.

## **(UI) Module**

```py
class UI:
```

Includes the all UI (User Input) functions to collect input from the user.

=== "UI.prompt"
    This is a `#!python @staticmethod` function

    Asks the user a prompt defined in the code with the ability to return the users response.

    Developers have to define **{prompt}** with a string for example,

    ``` py
    UI.prompt("What's your name?")
    ```

### **(UI.Conditions) Module**

Includes all Conditional functions and methods to collect conditional input from the user.

=== "UI.Conditions.meet"
    This is a `#!python @staticmethod` function

    Asks the user a prompt defined in the code with the ability to return the users response as in a **True or False.**

    Developers have to define **{prompt}** with a string for example,

    ``` py
    UI.Condition.meet("What's your name?")
    ```

    Developers could also set a default value to fallback on when user provides no input. For instance,

    ``` py
    UI.Condition.meet("What's your name?", default_value=True)
    ```