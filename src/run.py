import argparse

from loaders import CSVFileLoader
from parsers import Bank1, Bank2, Bank3
from savers import CSVFilerSaver


def run():
    parser = argparse.ArgumentParser(
        description='Merge csv files'
    )
    parser.add_argument(
        'paths',
        metavar='N',
        type=str,
        nargs='+',
        help='Paths to source csv files'
    )
    parser.add_argument(
        '--dest',
        type=str,
        default='result.csv',
        help='Path to the resulting csv file')

    args = parser.parse_args()

    saver = CSVFilerSaver(
        fields=('date', 'type', 'amount', 'from', 'to'),
        sources=(
            Bank1(loader=CSVFileLoader(path=args.paths[0])),
            Bank2(loader=CSVFileLoader(path=args.paths[1])),
            Bank3(loader=CSVFileLoader(path=args.paths[2])),
        )
    )
    saver.save(path=args.dest)
    
    print('Merged files:', args.paths)
    print('Into:', args.dest)


if __name__ == '__main__':
    run()
