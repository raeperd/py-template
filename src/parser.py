from pathlib import Path
from argparse import ArgumentParser
from argparse import Action


def get_argparser():
    parser = ArgumentParser()
    parser.add_argument("target_directory_path",
                        help="directoy path which has object files in it",
                        type=Path,
                        action=DirectoryCheckAction)
    return parser


class DirectoryCheckAction(Action):

    def __call__(self, parser, namespace, values :Path, option_string=None):
        if not values.is_dir():
            parser.error(f"{values} is not correct directory path")
        
        setattr(namespace, self.dest, values)