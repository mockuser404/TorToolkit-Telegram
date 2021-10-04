#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = "2.0.1.alpha"
__author__ = "YashDK Github@yash-dk"
#
from .database.dbhandler import TorToolkitDB, TtkTorrents, UserDB, TtkUpload
import time
from .core.varholdern import VarHolder
from tortoolkit.server.server import start_server
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("torlog.txt")]
)

logging.info("Database created")
upload_db = TtkUpload()
var_db = TorToolkitDB()
tor_db = TtkTorrents()
user_db = UserDB()
transfer = [0, 0]  # UP,DOWN

uptime = time.time()
to_del = []
SessionVars = VarHolder(var_db)
