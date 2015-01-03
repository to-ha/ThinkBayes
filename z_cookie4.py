from thinkbayes import Suite

class Cookie(Suite):
    def __init__(self, values=None, name='', mixes=None):
        super(Cookie, self).__init__(values, name)
        self.mixes = mixes

    def Likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        total = sum(mix.itervalues())
        like = float(mix[data]) / total
        mix[data] -= 1
        return like


def main():
    bowl1 = dict(vanilla=30, chocolate=10)
    bowl2 = dict(vanilla=20, chocolate=20)
    van = 0
    cho = 0

    hypos = ['Bowl 1', 'Bowl 2']
    mymixes = {
        'Bowl 1':bowl1,
        'Bowl 2':bowl2,
        }

    suite = Cookie(hypos, '', mymixes)

    print 'Before first drawing:'
    suite.Print()

    dataset = ['vanilla', 'chocolate', 'vanilla', 'chocolate', 'chocolate', 'chocolate', 'chocolate']
    for data in dataset:
        if data == 'vanilla':
            van += 1
        elif data == 'chocolate':
            cho += 1
        print('\nAfter {0} vanilla, {1} chocolate'.format(van, cho))
        suite.Update(data)
        suite.Print()


if __name__ == '__main__':
    main()