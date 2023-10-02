import os
import sys

from registry import RegistryClient


def main():
    client = RegistryClient(".")
    for name, version in client.get_all_module_versions():
        print(client.get_source(name, version)["url"])


if __name__ == "__main__":
    # Under 'bazel run' we want to run within the source folder instead of the execroot.
    if os.getenv("BUILD_WORKSPACE_DIRECTORY"):
        os.chdir(os.getenv("BUILD_WORKSPACE_DIRECTORY"))
    sys.exit(main())
