#!/usr/bin/env python3
import datetime
import time
import readline
import signal
import sys
import argparse as ap
from os import path as op


PROMPT = "> "


def signal_handler(signal, frame):
    print("\nDon't Ctrl-C me!\n"+PROMPT, end='')


def confirm(default=False):
    while True:
        r = input("You sure? [y/n] " + PROMPT)
        if r.lower()[0] == "y":
            return True
        elif r.lower()[0] == "n":
            return False
        elif r == "":
            return default


def loop(logfh):
    starttime = None
    while True:
        while starttime is None:
            r = input("type 'start' to start experiment\n" + PROMPT).strip()
            if r.lower() == "start":
                starttime = time.time()
                print("event", "unixtime", "elapsed", sep="\t", file=logfh)
                print("start", starttime, 0, sep="\t", file=logfh)
                break
        r = ""
        try:
            r = input(PROMPT)
            if r == "":
                print()
            r = r.strip()
        except EOFError:
            pass
        if r == "":
            continue
        t = time.time()
        rt = t - starttime
        if r.lower() in {"quit", "exit"}:
            if confirm():
                print("end", t, rt, sep="\t", file=logfh)
                break
            continue
        print(r, "@", int(rt), "secs")
        print(r, t, rt, sep="\t", file=logfh)
        logfh.flush()


def main():
    signal.signal(signal.SIGINT, signal_handler)

    A = ap.ArgumentParser()
    A.add_argument("-o", "--output", required=True, help="Output filename")
    args = A.parse_args()

    if op.exists(args.output):
        print("Error -- Output file exists. Use a different filename")
        sys.exit(1)

    with open(args.output, "w") as fh:
        loop(fh)
