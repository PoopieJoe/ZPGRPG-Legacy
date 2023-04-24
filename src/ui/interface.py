"""Package for running the game ui

More text
"""

import src.core as core

class UserInterface():
    """Class describing the user interface of the game
    
    More text
    """

    def __init__(
        self,
        core : core.Core
    ):
        """Constructor

        """
        self.core = core

        return

    def launch(
        self
    ):
        """Lauches the game backend systems

        """
        if not self.core.active:
            raise Exception("""Core has not been launched""")
        return