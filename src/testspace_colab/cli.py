"""Console script for testspace_colab."""
import sys
import click
import testspace_colab.client as client_module
import testspace_colab.lib as lib_module

VERSION = f"{lib_module.API.get_version()} client {client_module.Binary().version}"


@click.group()
@click.version_option(version=VERSION)
def main():
    """Console script for testspace_colab."""
    pass


@main.command()
@click.argument("args", nargs=-1)
@click.option("-v", "--version", is_flag=True)
@click.option("-h", "--help", is_flag=True)
def client(args, version, help):
    """Runs the client with the specified parameters"""
    binary = client_module.Binary()
    if version:
        binary.exec("--version")
    elif help:
        binary.exec("--help")
    else:
        exception = click.ClickException(f"'{' '.join(args)}' failed")
        exception.exit_code = binary.exec(args, return_code=None)
        if exception.exit_code:
            raise exception


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover