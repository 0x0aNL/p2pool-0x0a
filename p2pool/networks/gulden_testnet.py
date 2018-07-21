from p2pool.bitcoin import networks

PARENT = networks.nets['gulden_testnet']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 12*60*60//30 # shares
REAL_CHAIN_LENGTH = 12*60*60//30 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 20 # blocks
IDENTIFIER = '3bf8f9010c257730'.decode('hex')
PREFIX = '3117d50801b85bfb'.decode('hex')
P2P_PORT = 27072
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 27172
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-gulden'
VERSION_CHECK = lambda v: None
VERSION_WARNING = lambda v: None
KNOWN_RULES = set([u'PoW\xb2 - phase 2', u'testdummy'])
SOFTFORKS_REQUIRED = set(['bip65', 'bip66', 'csv', u'PoW\xb2 - phase 2'])
MINIMUM_PROTOCOL_VERSION = 1600
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
