import logging

# Module Wide Variables (MWV)
logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

yes_lib = ["y", "yes"]
no_lib = ["n", "no"]

log = logging


class UI:
    """
    Collection of User Inputs developers can use to add User Input into their project(s).
    """

    @staticmethod
    def prompt(prompt: str) -> str:
        """
        Gives the user a prompt to reply to
        :param prompt: The question (prompt) the user has to reply to
        :return: The users input (answer)
        """
        response: str = input(f"{prompt}\n")
        log.debug(f"User responded to UI.prompt with ({response}) | Engine Module")
        return response

    class Conditions:
        """
        A collection of conditions developers can use to implement into their project(s).
        """
        @staticmethod
        def meet(statement: str, default_value: bool = None) -> bool:
            """
            Gives a "Yes or No" statement with a loop to ensure a correct response
            :param statement: The statement (prompt) the user has tp say yes or no to
            :param default_value: If user value returns nothing, this default value will replace it. (Bool)
            :return: True or False depending on the user response
            """
            loop = True
            while loop:
                userchoice: str = input(f"\n{statement} | Y or N (Yes or No)\n").lower()

                if userchoice in yes_lib:
                    log.debug(f"User responded to UI.Conditions.meet with `{userchoice}` statement. | Engine Module")
                    return True
                elif userchoice in no_lib:
                    log.debug(f"User responded to UI.Conditions.meet with `{userchoice}` statement. | Engine Module")
                    return False
                else:
                    if default_value is not None:
                        log.debug(
                            f"User responded to UI.Conditions.meet was unrecognized but default value of `{default_value}` was provided. | Engine Module")
                        return default_value
                    log.warning(
                        f"User responded to UI.Conditions.meet, but the response was `{userchoice}`. | Engine Module")
                    print("Wrong choice, see the list for all compatible words.\n")

