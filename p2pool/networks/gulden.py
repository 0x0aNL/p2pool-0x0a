<<<<<<< HEAD
from p2pool.bitcoin import networks

PARENT = networks.nets['gulden']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 12*60*60//30 # shares
REAL_CHAIN_LENGTH = 12*60*60//30 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 20 # blocks
IDENTIFIER = '3bf8f9010c257730'.decode('hex')
PREFIX = '3117d50801b85bfb'.decode('hex')
P2P_PORT = 27000
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 27100
BOOTSTRAP_ADDRS = 'node1.guldenpool.nl node2.guldenpool.nl'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-gulden'
VERSION_CHECK = lambda v: True
||||||| merged common ancestors
=======
from p2pool.bitcoin import networks

PARENT = networks.nets['guldencoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 12*60*60//30 # shares
REAL_CHAIN_LENGTH = 12*60*60//30 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 20 # blocks
IDENTIFIER = '2ea11f4990dd6b23'.decode('hex')
PREFIX = '6d5b3d32dccade21'.decode('hex')
P2P_PORT = 27000
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 27100
BOOTSTRAP_ADDRS = 'node1.guldenpool.nl node2.guldenpool.nl'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-guldencoin'
VERSION_CHECK = lambda v: True
>>>>>>> Add altcoins
