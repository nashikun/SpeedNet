import argparse
import json
from game.game import Game
import os


def resolve_default_config():
    return os.path.join(os.getcwd(), "config", "config.json")


def init_parser():
    parser = argparse.ArgumentParser(description='Runs the project')
    parser.add_argument("--config_path", type=str, default=resolve_default_config())
    return parser


if __name__ == "__main__":
    parser = init_parser()
    args = parser.parse_args()
    with open(args.config_path, 'r') as f:
        config = json.load(f)
    game = Game(**config["game_config"])
    print(config)
    game.setup(**config)
    game.run()
