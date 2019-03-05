
import hashlib

from eddsa import PrivateKey, PublicKey
from field import FQ
from utils import pprint_for_zokrates_cli

if __name__ == "__main__":

    raw_msg = b'ZoKrates rullez'
    msg = hashlib.sha512(raw_msg).digest()

    # sk = PrivateKey.from_rand()
    # Seeded for debug purpose
    key = FQ(1997011358982923168928344992199991480689546837621580239342656433234255379025)
    sk = PrivateKey(key)
    sig = sk.sign(msg)

    pk = PublicKey.from_private(sk)
    isVerified = pk.verify(sig, msg)
    print(isVerified)

    print('Arguments for ZoKrates verifyEddsa proof:')
    pprint_for_zokrates_cli(pk, sig, msg)
