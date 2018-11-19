#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading


def worker():
    print("i'm thread worker")
    st = threading.current_thread()
    print(st.getName())


t = threading.current_thread()

print(t.getName())

new_t = threading.Thread(target=worker, name="sub Thread")
new_t.start()
