import argparse
from rich import print

from config import APP_NAME, VERSION
from utils import normalize_name, format_greeting

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="greet", description="Simple greeting CLI")
    p.add_argument("--name", default="world", help="Name to greet")
    p.add_argument("--caps", action="store_true", help="Uppercase output")
    p.add_argument("--version", action="store_true", help="Show version")
    return p.parse_args()

def main() -> None:
    args = parse_args()
    if args.version:
        print(f"[bold]{APP_NAME}[/bold] v{VERSION}")
        return

    name = normalize_name(args.name)
    print(format_greeting(name, caps=args.caps))

if __name__ == "__main__":
    main()
