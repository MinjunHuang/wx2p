#!usr/bin/env python
#-*- coding:utf-8 -*-

import time
import redis
import logging
import tornado.web

from lib.wechat_sdk import WeChatEnterprise


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        super(BaseHandler,self).initialize()
        
        self._redis = self.settings.get('_redis')
        self.wcep = self.settings.get('wcep')
        self.access_token = self.wcep.get_access_token()


    def prepare(self):
        self.add_header("Content-Security-Policy", "default-src 'self'; script-src 'self' 'unsafe-eval'; "
                            "connect-src 'self'; img-src 'self' data:; style-src 'self'; "
                            "font-src 'self'; frame-src 'self'; ")
        self.add_header("X-Frame-Options", "deny")
        self.add_header("X-XSS-Protection", "1; mode=block")
        self.add_header("X-Content-Type-Options", "nosniff")
        self.add_header("x-ua-compatible:", "IE=edge,chrome=1")
        self.clear_header("Server")