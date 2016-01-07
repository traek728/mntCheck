#

import argparse


def main():

    parser = argparse.ArgumentParser(description='Check remotely mounted filesystems in /etc/fstab against /etc/mtab')
    parser.add_argument('--remote-host', help='--remote-host dest-ip', nargs=1)
    args = parser.parse_args()

    if args.remote-host:
            print remote-host

if __name__ == "__main__":
    main()

