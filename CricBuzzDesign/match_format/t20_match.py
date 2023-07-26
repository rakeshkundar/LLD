from match_type import MatchType

class T20Match(MatchType):

    def no_of_overs(self):
        return 20

    def max_overs_bolwer_allowed(self):
        return 4