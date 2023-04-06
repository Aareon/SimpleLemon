from pathlib import Path
import gnupg

GPG_BIN_PATH = Path(r"C:\Program Files (x86)\GnuPG\bin\gpg.exe")
DEFAULT_GPG_HOME_PATH = Path(r"%LOCALAPPDATA%").resolve()
if not DEFAULT_GPG_HOME_PATH.exists():
    print(f"Creating dir {DEFAULT_GPG_HOME_PATH}")
    DEFAULT_GPG_HOME_PATH.mkdir(parents=True)
gpg = gnupg.GPG(gpgbinary=GPG_BIN_PATH, gnupghome=DEFAULT_GPG_HOME_PATH)
gpg.encoding = "utf-8"


def get_public_key(key):
    fingerprint = str(key)
    public_key = gpg.export_keys(fingerprint)
    return public_key


def create_key(passphrase, alias=None, email=None):
    input_data = gpg.gen_key_input(
        key_type="RSA",
        key_length=1024,
        name_comment=alias,
        name_email=email,
        passphrase=passphrase,
    )
    key = gpg.gen_key(input_data)
    return key


if __name__ == "__main__":
    # test crypto functions
    test_key = create_key("SomeSuperSecurePassword123", alias="Aareon", email="askully13@gmail.com")
    test_pk = get_public_key(test_key)
    print(test_pk)
