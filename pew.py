#!/usr/bin/env python3
"""
Pew - A simple CLI tool
"""
import sys
import argparse


def stop_command(args):
    """Handle the stop subcommand"""
    if args.when:
        print(f"Stopping pew {args.when}")
    else:
        print("Stopping pew")
    return 0


def main():
    """Main entry point for the pew CLI"""
    parser = argparse.ArgumentParser(
        prog='pew',
        description='Pew CLI tool'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Stop subcommand
    stop_parser = subparsers.add_parser('stop', help='Stop pew')
    stop_parser.add_argument('when', nargs='?', default=None, 
                            help='When to stop (e.g., "now")')
    stop_parser.set_defaults(func=stop_command)
    
    args = parser.parse_args()
    
    if hasattr(args, 'func'):
        return args.func(args)
    else:
        parser.print_help()
        return 1


if __name__ == '__main__':
    sys.exit(main())
