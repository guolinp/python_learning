#!/usr/bin/python -tt

from app_base import AppBase


class Music(AppBase):

    def start(self, name):
        print 'play %s' % name

    def stop(self, name):
        print 'stop %s' % name
