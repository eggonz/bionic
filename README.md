# Bionic Reading

[Bionic reading](https://bionic-reading.com/) is a method to improve focus and read faster.

I implemented a small tool for personal use to convert local files to bionic format.

Currently, it supports the following file formats:

- Markdown (md)

## Setup

Run the following command on the linux terminal to install the tool:

```bash
sh install.sh
```

The installation script will copy `bionic` and `bionic_converter/` in `~/bin`.
To uninstall the tool, just delete them from `~/bin`.
Running sh `sh install.sh` again will overwrite the existing installation.

## Use

The tool takes a path to a file and generates a bionic copy of it in the specified output path. 

Run `bionic -h` or `bionic --help` in terminal for further details.

## Example of use

A markdown example file can be found under `res/examples/`.
Run the following command in the terminal to test it:

```bash
bionic res/examples/large_markdown.md
```

---

## References

- Large markdown file for testing: https://gist.github.com/quanticle/7be19a638f20bb55686f3d154f28fd4e
