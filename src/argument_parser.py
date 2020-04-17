from pathlib import Path
from argparse import ArgumentParser
from argparse import Action

def get_argparser():
    parser = ArgumentParser("Python script base to do something in PATH")
    parser.add_argument("-p",
                        "--target_dir",
                        metavar="PATH",
                        help="Directory path which has target files to do something",
                        type=Path,
                        action=DirectoryCheckAction)
    return parser

class DirectoryCheckAction(Action):
    def __call__(self, parser, namespace, values :Path, option_string=None):
        if not values.is_dir():
            parser.error(f"{values} is not correct directory path")
        
        setattr(namespace, self.dest, values)