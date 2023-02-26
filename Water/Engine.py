import logging

# Module Wide Variables (MWV)
logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

yes_lib = ["Y", "y", "Yes", "yes"]
no_lib = ["N", "n", "No", "no"]

BUILD_NUMBER = "Y23B2R010"
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
        def meet(statement: str) -> bool:
            """
            Gives a "Yes or No" statement with a loop to ensure a correct response
            :param statement: The statement (prompt) the user has tp say yes or no to
            :return: True or False depending on the user response
            """
            loop = True
            while loop:
                userchoice: str = input(f"\n{statement} | Y or N (Yes or No)\n")

                if userchoice in yes_lib:
                    log.debug(f"User responded to UI.Conditions.meet with ({userchoice}) statement. | Engine Module")
                    return True
                elif userchoice in no_lib:
                    log.debug(f"User responded to UI.Conditions.meet with ({userchoice}) statement. | Engine Module")
                    return False
                else:
                    print("Wrong choice, see the list for all compatible words.\n")
                    log.warning("User responded to UI.Conditions.meet however, the value was invaild. | Engine Module")


class Boneworks:
    """
    Major Release / Engine information
    """
    @staticmethod
    def buildinfo():
        """
        Gives the build number
        :return: BUILD_NUMBER
        """
        print(BUILD_NUMBER)
