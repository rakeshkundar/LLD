from match_type import MatchType

class OneDayMatch(MatchType):

    def no_of_overs(self):
        return 50

    def max_overs_bolwer_allowed(self):
        return 10