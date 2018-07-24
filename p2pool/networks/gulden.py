from p2pool.bitcoin import networks

PARENT = networks.nets['gulden']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 12*60*60//30 # shares
REAL_CHAIN_LENGTH = 12*60*60//30 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 20 # blocks
IDENTIFIER = '4bf8f9010c257730'.decode('hex')
PREFIX = '4117d50801b85bfb'.decode('hex')
P2P_PORT = 27000
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 27100
BOOTSTRAP_ADDRS = 'node1.guldenpool.nl'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-gulden'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: None
KNOWN_RULES = set([u'PoW\xb2 - phase 2'])
SOFTFORKS_REQUIRED = set(['bip65', 'bip66', 'csv', u'PoW\xb2 - phase 2'])
MINIMUM_PROTOCOL_VERSION = 1700
NEW_MINIMUM_PROTOCOL_VERSION = 1700
POW2_ACTIVATION_VERSION = 17 # From this p2pool share version onwards, p2pool share info contains pow2 data
