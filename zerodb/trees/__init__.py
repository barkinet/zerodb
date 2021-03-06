"""
BTrees with modified bucket sizes
"""

import BTrees


class TreeFamily32(BTrees._Family32):
    import IFBTree as IF
    import IIBTree as II
    import IOBTree as IO
    import OIBTree as OI
    import OOBTree as OO


family32 = TreeFamily32()
family32.IF.family = family32
family32.II.family = family32
family32.IO.family = family32
family32.OI.family = family32
family32.OO.family = family32
