import os

import click
from streamlit.cli import configurator_options, _apply_config_options_from_cli, _main_run


@click.group()
def main():
    pass


@main.command("run-demo")
@configurator_options
def main_streamlit(**kwargs):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'display_predictions_with_model_as_a_service.py')
    _apply_config_options_from_cli(kwargs)
    _main_run(filename)


if __name__ == "__main__":
    main()
