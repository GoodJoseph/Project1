class Vote:
    """Class for voting for candidates"""
    def __init__(self):
        """Initializing the Vote Class"""
        self.cameron = 0
        self.allison = 0
        self.diego = 0
        self.total = 0

    def vote_cameron(self):
        """Puts a vote down for Cameron"""
        self.cameron += 1
        self.total += 1

    def vote_allison(self):
        """Puts a vote down for Allison"""
        self.allison += 1
        self.total += 1

    def vote_diego(self):
        """Puts a vote down for Diego"""
        self.diego += 1
        self.total += 1

    def get_totals(self):
        """Returns the total votes for each candidate"""
        return {
            "Cameron": self.cameron,
            "Allison": self.allison,
            "Diego": self.diego,
            "Total": self.total
        }

    def reset_votes(self):
        """Resets all vote counts to zero"""
        self.cameron = 0
        self.allison = 0
        self.diego = 0
        self.total = 0