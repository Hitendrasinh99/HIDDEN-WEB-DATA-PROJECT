import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


key = "mysecretkey12345"  
image_path = "static/image2.png"  
output_path = "static/encrypted_image_data.txt"


with open(image_path, 'rb') as f:
    raw = f.read()
encoded = base64.b64encode(raw).decode()
data_uri = f"data:image/png;base64,{encoded}"


cipher = AES.new(key.encode(), AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(data_uri.encode(), 16))


with open(output_path, "wb") as f:
    f.write(base64.b64encode(ciphertext))

print("Encryption complete. Encrypted image saved to:", output_path)
