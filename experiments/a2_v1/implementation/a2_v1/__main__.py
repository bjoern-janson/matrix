import argparse
from .runner import validate,run_prospective
def main():
 p=argparse.ArgumentParser(); p.add_argument('command',nargs='?',default='validate',choices=('validate','run-prospective')); p.add_argument('--output',required=True); a=p.parse_args(); print((validate if a.command=='validate' else run_prospective)(a.output))
if __name__=='__main__': main()
