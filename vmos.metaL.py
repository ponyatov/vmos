## @file
## @brief meta: Guest OS in Rust

from metaL import *

p = Project(
    title='''Guest OS in Rust''',
    about='''''') \
    | Rust()

p.sync()
