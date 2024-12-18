from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
private_pem_data = "xxxxx"
password_str = "REDACTED"
print(type(password_str))
p_key = serialization.load_pem_private_key(private_pem_data, password=password_str.encode(),backend=default_backend())
# p_key = serialization.load_pem_private_key(<private_key>, password=password_str.encode(),backend=default_backend())
# pkb = p_key.private_bytes(encoding=serialization.Encoding.DER,
#                              format=serialization.PrivateFormat.PKCS8,
#                           encryption_algorithm=serialization.NoEncryption())