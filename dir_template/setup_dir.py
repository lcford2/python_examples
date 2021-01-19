import argparse
import pathlib
import json

def parse_args():
    """Argument parsing function

    :return: namespace containing user provided arguments
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description="Setup a directory from a template."
    )

    parser.add_argument(dest="template", default=None,
                        help="Path to json file that contains template.")
    parser.add_argument(dest="target", default=None,
                        help="Path to the target directory. If it does not exist, it will be created. \
                              If it is not empty and the -F flag is not provided, the program will stop.")
    parser.add_argument("-F", "--force", dest="force", action="store_true",
                        help="Flag that forces the directory to be setup, regardless of whether the directory is empty or not.\
                              Also, if this flag is provided, non-existing parents of the target dir will be created. Use wisely.")
    
    args = parser.parse_args()
    args.template = pathlib.Path(args.template)
    args.target = pathlib.Path(args.target)
    return args

def read_template(args):
    """Reads JSON template into a python dictionary

    :param args: Namespace of user provided arguments
    :type args: argparse.Namespace
    :return: Template dictionary from json file
    :rtype: dict
    """
    with open(args.template, "r") as f:
        template = json.load(f)
    return template

def check_target_dir(args):
    """Checks the target directory to see if it exists, is it a directory or a file, and considers the force flag.
    Will raise FileExistsErrors if the directory exits, is not empty, and the force flag is not provided or if the target exists and is a file.

    :param args: Namespace of user provided arguments
    :type args: argparse.Namespace
    :raises FileExistsError: If the target directory is not empty and the force flag if not provided. 
    :raises FileExistsError: If the target directory exists as a file
    :return: True if the program should proceed
    :rtype: bool
    """
    target = args.target
    if target.exists():
        if target.is_dir():
            if len(list(target.iterdir())) == 0 or args.force:
                return True
            else:
                raise FileExistsError(
                    f"Target directory provided ['{target}'] is not empty.")
        else:
            raise FileExistsError(f"Target directory provided ['{target}'] is a file.")
    else:
        target.mkdir(parents=args.force)
        return True

def setup_dir(args):
    """Creates the directory structure and basic files.

    :param args: Namespace of user provided arguments.
    :type args: argparse.Namespace
    """
    def make_dir(key, value):
        if isinstance(value, dict):
            for key1, value1 in value.items():
                make_dir(key/key1, value1)
        else:
            key.mkdir(parents=True)
            for file in value:
                (key/file).touch()

    for key, value in  args.template.items():
        if key == ".":
            for file in value:
                (args.target/file).touch()
        else:
            cur_dir = (args.target / key)
            make_dir(cur_dir, value)
    

if __name__ == "__main__":
    from IPython import embed as II
    args = parse_args()
    args.template = read_template(args)
    check_target_dir(args)
    setup_dir(args)
