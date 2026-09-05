"""CLI: validation is the default; unresolved execution must be named explicitly."""
import argparse
import json
import sys
from . import runner


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', nargs='?', default='validate',
                        choices=('validate', 'run-unresolved'))
    parser.add_argument('--output', required=True,
                        help='New output directory; existing records are never overwritten')
    args = parser.parse_args()
    try:
        run = runner.validate if args.command == 'validate' else runner.run_unresolved
        result = run(args.output)
    except Exception as exc:
        print(json.dumps({'status': getattr(exc, 'status', 'INVALID_NO_SCIENTIFIC_RESULT'),
                          'reason': str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps({key: result[key] for key in
                     ('mode', 'status', 'unresolved_units_executed', 'source_digest')}, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
