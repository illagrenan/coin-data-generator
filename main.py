# coding=utf-8
import argparse
import random


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(u'-coin-count', u'-c', type=int, help=u"Kolik minci pouzit? Vychozi je nahodne cislo.",
                        default=random.randint(10, 100))

    parser.add_argument(u'-amount-count', u'-a', type=int,
                        help=u"Maximalni pocet castek, ktere vygenerovat? Vychozi je nahodne cislo.",
                        default=random.randint(10, 10000))

    parser.add_argument(u'-max-amount', u'-m', type=int, help=u"Maximalni pripustna castka. Vychozi je nahodne cislo.",
                        default=random.randint(100, 10000))

    args_from_console = parser.parse_args()

    print (args_from_console)

    list_of_random_integers = random.sample(range(1, args_from_console.max_amount, 1),
                                            args_from_console.amount_count)
    list_of_random_integers.sort()

    result = str(args_from_console.coin_count) + u" " + u" ".join(str(x) for x in list_of_random_integers)

    for one_random_number in list_of_random_integers:
        result += u" " + str(one_random_number)

    result_filename = u'data/result.txt'

    with open(result_filename, u'a') as the_file:
        the_file.truncate()
        the_file.write(result + u"\n")

    print (u"Ulozeno do " + result_filename)


if __name__ == u"__main__":
    main()