from pathlib import Path
import gnupg

GPG_PATH = Path(r"C:\Program Files (x86)\GnuPG\bin")
gpg = gnupg.GPG(gnupghome=GPG_PATH)
gpg.encoding = "utf-8"


if __name__ == "__main__":
    # test crypto functions
    input_data = gpg.gen_key_input(key_type="RSA", key_length=1024)
    key = gpg.gen_key(input_data)
    fingerprint = str(key)
    ascii_armored_public_keys = gpg.export_keys(fingerprint)
