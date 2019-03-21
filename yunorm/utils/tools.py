import hashlib


def get_md5(s):
    sig_md5 = hashlib.md5()
    sig_md5.update(s.encode("utf-8"))
    return sig_md5.hexdigest()
