#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: gilbetliu
# @Date:   2015-08-26 15:48:08
# @Last Modified by:   gilbetliu
# @Last Modified time: 2016-01-20 17:45:58
import logging, os, json, time
import subprocess


def get_errors(error_string):
    '''
    returns all lines in the error_string that start with the string "error"

    '''

    lines = error_string.splitlines()
    error_lines = tuple(line for line in lines if line.find('Error') >= 0)
    if len(error_lines) > 0:
        return '\n'.join(error_lines)
    else:
        return error_string.strip()

def cap():
    cap_command = ['/usr/bin/fswebcam', '--no-banner', '-r', '640x480', '-S', '20', './images/image-' + time.asctime(time.localtime(time.time())).replace(' ', '-').replace(':', '-') + '.jpg']
    print cap_command
    try:
        publish_proc = subprocess.Popen(cap_command,
            stderr=subprocess.PIPE, cwd=os.getcwd())
        pub_status, pub_error_string = publish_proc.wait(), publish_proc.stderr.read()
        if pub_status:
            errors = get_errors(pub_error_string)
            logging.info(errors)
        else:
            print 'cap done'
            logging.info('cap done')
    finally:
        print 'run'

def syncup():
    sync_command = ['/usr/local/bin/bypy', 'syncup']
    print sync_command
    try:
        sync_proc = subprocess.Popen(sync_command,
            stderr=subprocess.PIPE, cwd=os.getcwd() + os.sep + 'images')
        sync_status, sync_error_string = sync_proc.wait(), sync_proc.stderr.read()
        if sync_status:
            errors = get_errors(sync_error_string)
            logging.info(errors)
        else:
            print 'cap done'
            logging.info('cap done')
    finally:
        print 'run'

def main():
    logging.basicConfig(filename = os.path.join(os.getcwd(), 'run.log'),
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='[%(asctime)s %(levelname)s %(filename)s] %(message)s'
    )
    cap()
    syncup()

    

if __name__ == "__main__":
    main()
