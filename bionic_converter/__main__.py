import argparse
import os.path

import md


def parse_args() -> tuple:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(prog='Bionic',
                                     description='Re-formats files to a bionic_converter-reading format',
                                     epilog='by github.com/eggonz')
    parser.add_argument('filepath')  # positional
    parser.add_argument('-o', '--out', type=str, required=False,
                        help='path/to/output_file.txt. the default path is out/<name>_bionic.md, '
                             'where the name and extension are the same of the input file')
    args = parser.parse_args()

    in_filename = os.path.basename(args.filepath)
    name_extension = in_filename.rsplit('.', maxsplit=1)
    if len(name_extension) == 1:
        raise TypeError("Invalid file format")
    name, ext = name_extension

    if not args.out:
        out_filename = f'{name}_bionic.{ext}'
        out_filepath = os.path.join('out', out_filename)
    else:
        out_filepath = args.out
    os.makedirs(os.path.dirname(out_filepath), exist_ok=True)

    return args.filepath, out_filepath, ext


def main() -> None:
    """Main function"""
    in_path, out_path, file_type = parse_args()

    if file_type == 'md':
        md.run(in_path, out_path)
    else:
        raise TypeError("Invalid file format")
    print('Done!')


if __name__ == '__main__':
    main()
