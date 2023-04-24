import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization


# キーペア認証を使用する場合の処理
# 暗号化している場合は Passphase を環境変数 PRIVATE_KEY_PASSPHRASE に指定してください
passphase = os.environ.get('PRIVATE_KEY_PASSPHRASE')
password = None if passphase is None else passphase.encode()

# 秘密鍵のファイルパスを open("<path>", "rb") に指定してください
with open("/home/.ssh/rsa_key.p8", "rb") as key:
    p_key = serialization.load_pem_private_key(
        key.read(),
        password=password,
        backend=default_backend()
    )

pkb = p_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption())

# お使いの Snowflake account に合わせてください
connection_parameters = {
    "account": "xx00000.ap-northeast-1.aws",
    "user": "<you_username>",
    "private_key": pkb,
    # "password": "<your_password>", # パスワード認証を使用する場合
    "role": "<your_role>",
    "database": "<your_database>",
    "schema": "<your_schema>",
    "warehouse": "<your_warehouse>",
}
