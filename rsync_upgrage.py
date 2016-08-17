#!/usr/bin/env python

import sys
import time
import subprocess

source = "/tmp/blabla_dir/"  #WARN!!!NEED trailing /
target = "/tmp/blabla_dir1"
rsync = "rsync"
arguments = "-av"
cmd = "%s %s %s %s" % (rsync, arguments, source, target)

def sync():
    while True:
        ret = subprocess.call(cmd, shell=True)
        if ret != 0:
            print "resubmitting rsync"
            time.sleep(30)
        else:
            print "rsync was succesful"
            subprocess.call("mail  s 'jobs done' mail@domain.aa",
                            shell=True)
            sys.exit(0)
sync()
