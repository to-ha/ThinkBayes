from thinkbayes import Suite

class Bowl(object):

    def __init__(self, cookies=None):
        """Initializes the distribution.

        cookies: dict with flavor and number of cookies in the bowl
        """
        self.d = {}

        if cookies is None:
            return

        for flavor, count in cookies.iteritems():
            self.Set(flavor, count)

        self.Normalize()

    def Set(self, x, y=0):
        """Sets the freq/prob associated with the value x.

        Args:
            x: number value
            y: number freq or prob
        """
        self.d[x] = y

    def Normalize(self, fraction=1.0):
        total = self.Total()
        if total == 0.0:
            return total

        factor = float(fraction) / total
        for x in self.d:
            self.d[x] *= factor

        return total

    def Total(self):
        """Returns the total of the frequencies/probabilities in the map."""
        total = sum(self.d.itervalues())
        return total

    def Items(self):
        """Gets an unsorted sequence of (value, freq/prob) pairs."""
        return self.d.items()


class Cookie(Suite):
    """A map from string bowl ID to probablity."""

    mixes = {
        'Bowl 1':dict(vanilla=0.75, chocolate=0.25),
        'Bowl 2':dict(vanilla=0.5, chocolate=0.5),
        }
    print mixes
    # def __init__(self, hypos, mixes):
    #     super(Cookie, self).__init__()
    #     self.mixes = mixes

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        mix = self.mixes[hypo]
        like = mix[data]
        return like


def main():
    bowl1 = Bowl(dict(vanilla=30, chocolate=10))
    bowl2 = Bowl(dict(vanilla=20, chocolate=20))
    print bowl1
    hypos = ['Bowl 1', 'Bowl 2']
    mymixes = {
        'Bowl 1':bowl1,
        'Bowl 2':bowl2,
        }
    print mymixes

    suite = Cookie(hypos)
    suite.Update('vanilla')
    suite.Print()

    print bowl1.Items()


if __name__ == '__main__':
    main()
