import argparse
import json
from game.game import Game


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def init_parser():
    parser = argparse.ArgumentParser(description='Runs the project')
    subparsers = parser.add_subparsers(help='sub-command help', dest='command')

    file_parser = subparsers.add_parser('file', help='Reads the options from a config file')
    file_parser.add_argument("--config_path", type=str, required=True)

    manual_parser = subparsers.add_parser('manual', help='Enters the options manually')
    manual_parser.add_argument("--level_type", type=str, default="CellularAutomataLevel")
    manual_parser.add_argument("--level_path", type=str, default=None)
    manual_parser.add_argument("--level_width", type=int, default=20)
    manual_parser.add_argument("--level_height", type=int, default=20)
    manual_parser.add_argument("--screen_height", type=int, default=20)
    manual_parser.add_argument("--screen_width", type=int, default=20)
    manual_parser.add_argument("--ticks", type=int, default=1)
    manual_parser.add_argument("--max_turns", type=int, default=None)
    manual_parser.add_argument("--fps", type=int, default=60)
    manual_parser.add_argument("--render", type=str2bool, nargs='?', default=True)
    return parser


if __name__ == "__main__":
    parser = init_parser()
    args = parser.parse_args()
    if args.command == "file":
        with open(args.config_path, 'r') as f:
            config = json.load(f)
    else:
        config = vars(args)

    game_config = {"render": config["render"], "ticks": config["ticks"], "max_turns": config["max_turns"]}
    screen_config = {"screen_height": config["screen_height"], "screen_width": config["screen_width"],
                     "fps": config["fps"]}
    level_config = {"level_type": config["level_type"], "level_height": config["level_height"],
                    "level_width": config["level_width"], "level_path": config["level_path"]}
    model_config = {}
    game = Game(**game_config)
    game.init_screen(**screen_config)
    game.init_level(**level_config)
    game.init_player()
    game.run()
