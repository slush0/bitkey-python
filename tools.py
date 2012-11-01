import ecdsa
import hashlib
import binascii
import mnemonic

Hash = lambda x: hashlib.sha256(hashlib.sha256(x).digest()).digest()
addrtype = 0

# secp256k1, http://www.oid-info.com/get/1.3.132.0.10
_p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2FL
_r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141L
_b = 0x0000000000000000000000000000000000000000000000000000000000000007L
_a = 0x0000000000000000000000000000000000000000000000000000000000000000L
_Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798L
_Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8L
curve_secp256k1 = ecdsa.ellipticcurve.CurveFp( _p, _a, _b )
generator_secp256k1 = ecdsa.ellipticcurve.Point( curve_secp256k1, _Gx, _Gy, _r )
oid_secp256k1 = (1,3,132,0,10)
SECP256k1 = ecdsa.curves.Curve("SECP256k1", curve_secp256k1, generator_secp256k1, oid_secp256k1 )

__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__b58base = len(__b58chars)

def b58encode(v):
    """ encode v, which is a string of bytes, to base58."""

    long_value = 0L
    for (i, c) in enumerate(v[::-1]):
        long_value += (256**i) * ord(c)

    result = ''
    while long_value >= __b58base:
        div, mod = divmod(long_value, __b58base)
        result = __b58chars[mod] + result
        long_value = div
    result = __b58chars[long_value] + result

    # Bitcoin does a little leading-zero-compression:
    # leading 0-bytes in the input become leading-1s
    nPad = 0
    for c in v:
        if c == '\0': nPad += 1
        else: break

    return (__b58chars[0]*nPad) + result

def b58decode(v, length):
    """ decode v into a string of len bytes."""
    long_value = 0L
    for (i, c) in enumerate(v[::-1]):
        long_value += __b58chars.find(c) * (__b58base**i)

    result = ''
    while long_value >= 256:
        div, mod = divmod(long_value, 256)
        result = chr(mod) + result
        long_value = div
    result = chr(long_value) + result

    nPad = 0
    for c in v:
        if c == __b58chars[0]: nPad += 1
        else: break

    result = chr(0)*nPad + result
    if length is not None and len(result) != length:
        return None

    return result

def hash_160(public_key):
    md = hashlib.new('ripemd160')
    md.update(hashlib.sha256(public_key).digest())
    return md.digest()

def hash_160_to_bc_address(h160):
    vh160 = chr(addrtype) + h160
    h = Hash(vh160)
    addr = vh160 + h[0:4]
    return b58encode(addr)

def public_key_to_bc_address(public_key):
    h160 = hash_160(public_key)
    return hash_160_to_bc_address(h160)

def get_mnemonic(seed):
    return ' '.join(mnemonic.mn_encode(seed))

def get_seed(seed_words):
    return mnemonic.mn_decode(seed_words.split(' '))

def generate_seed():
    return "%032x" % ecdsa.util.randrange(pow(2, 128))
    
def stretch_key(seed):
    oldseed = seed
    for _ in range(100000):
        seed = hashlib.sha256(seed + oldseed).digest()
    return ecdsa.util.string_to_number(seed)

def init_master_private_key(seed):
    secexp = stretch_key(seed)
    return ecdsa.SigningKey.from_secret_exponent(secexp, curve=SECP256k1)
    
def init_master_public_key(seed):
    master_private_key = init_master_private_key(seed)
    return master_private_key.get_verifying_key().to_string()

def get_sequence(master_public_key, n):
    return ecdsa.util.string_to_number(Hash( "%d:0:" % n + master_public_key ))

def get_new_address(master_public_key, n):
    """Publickey(type,n) = Master_public_key + H(n|S|type)*point  """
    z = get_sequence(master_public_key, n)
    master_public_key = ecdsa.VerifyingKey.from_string(master_public_key, curve=SECP256k1 )
    pubkey_point = master_public_key.pubkey.point + z*SECP256k1.generator
    public_key2 = ecdsa.VerifyingKey.from_public_point( pubkey_point, curve = SECP256k1 )
    address = public_key_to_bc_address('04'.decode('hex') + public_key2.to_string() )
    print address
    return address
    