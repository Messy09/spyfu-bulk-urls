from typing import List, Optional

from src.runner import main_from_cli

def main(argv: Optional[List[str]] = None) -> None:
    """
    Console script entry point.
    """
    main_from_cli(argv)

if __name__ == "__main__":
    main()