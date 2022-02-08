from pathlib import Path

PATH_CONFIG = Path(__file__).parent
PATH_SRC = PATH_CONFIG.parent  # optionally, change this to reflect the name of the 'importname' directory
PATH_PROJECT_ROOT = PATH_SRC.parent
PATH_TESTS = PATH_PROJECT_ROOT / "tests"

if __name__ == "__main__":
    try:
        print(PATH_CONFIG)
        print(PATH_SRC)
        print(PATH_PROJECT_ROOT)
        print(PATH_TESTS)
    except FileNotFoundError:
        print("\nOne or more paths not configured properly - look in definitions.py in the config folder")
    else:
        print("\nPaths configured correctly!")
