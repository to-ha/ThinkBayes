from thinkbayes import Hist, Suite


class Cookie(Suite):
    """A map from string bowl ID to probablity."""

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        like = hypo[data] / hypo.Total()
        if like:
            hypo[data] -= 1
        return like

class Hist2(Hist):

    def Normalize(self):
        total = self.Total()

        for item in self.d:
            self.d[item] /= total


def main():
    bowl1 = Hist2(dict(vanilla=30, chocolate=10))
    bowl2 = Hist2(dict(vanilla=20, chocolate=20))
    pmf = Cookie([bowl1, bowl2])

    print('After 1 vanilla')
    pmf.Update('vanilla')
    for hypo, prob in pmf.Items():
        print(hypo, prob)

    print('\nAfter 1 vanilla, 1 chocolate')
    pmf.Update('chocolate')
    for hypo, prob in pmf.Items():
        print(hypo, prob)


if __name__ == '__main__':
    main()
