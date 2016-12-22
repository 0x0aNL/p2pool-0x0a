from p2pool.bitcoin import networks

PARENT = networks.nets['gulden_testnet']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 12*60*60//30 # shares
REAL_CHAIN_LENGTH = 12*60*60//30 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 20 # blocks
IDENTIFIER = '1bf8f9010c257730'.decode('hex')
PREFIX = '1117d50801b85bfb'.decode('hex')
P2P_PORT = 26000
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 26100
BOOTSTRAP_ADDRS = 'node1.guldenpool.nl node2.guldenpool.nl'.split(' ')
#ANNOUNCE_CHANNEL = '#p2pool-gulden-testnet'
VERSION_CHECK = lambda v: True
