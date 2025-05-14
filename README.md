  HIDDEN-WEB-DATA PROJECT - SECURE CONTENT VIEWER

PURPOSE:
-----------
This project demonstrates how to securely present web content using encryption.
It ensures that certain sensitive or hidden parts of the page (like an image)
can only be revealed after successful AES decryption with a valid key.

This model is ideal for:
- Research-focused web archives
- Confidential content previews
- Controlled content access with cryptographic protection


PROJECT OVERVIEW:
---------------------
This project uses two separate HTML files:

1. index.html
   - Public-facing page
   - Contains general visible content (text and image)
   - Shows a Hidden and Importent Content For this Research message where the hidden content (image) would be

2. Xindex.html
   - Secure extension of index.html
   - Dynamically loads and displays content from index.html
   - Adds a secure section that prompts the user to enter an AES key
   - On correct decryption, displays the hidden image without modifying original content

This design keeps index.html completely untouched — no rewriting or duplication.


PROJECT STRUCTURE:
---------------------
- Hidden-web-data/
- index.html                # Public content with hidden image placeholder
- Xindex.html               # Secure viewer with AES decryption
- encrypt_image.py          # Python script to AES-encrypt the image
- server.py                 # Flask web server for testing/viewing
- style.css                 # Styling for both HTML pages
- static/
  ├── image2.png            # The hidden image (source)
  └── encrypted_image_data.txt  # Encrypted data generated from image2.png


ENCRYPTION INFO:
-------------------
- Encryption Method: AES (ECB mode with PKCS7 padding)
- Key used for encryption/decryption: mysecretkey12345
- The `encrypt_image.py` script reads image2.png, converts it into a base64 data URI,
  encrypts it using AES, and stores the encrypted output in encrypted_image_data.txt.
- This encrypted image is decrypted ONLY when the correct key is provided via Xindex.html


HOW TO RUN:
--------------
1. Place your image inside the `static/` folder as `image1.png`,`image2.png`
2.  Install Required Packages if required 
   ```
   pip install flask
   ```
   ```
   pip install pycryptodome
   ```
3. Run the encryption script:
   ```
    python encrypt_image.py
   ```
4. Start the local server:
   ```
   python server.py
   ```
5. Open in browser:
   ```
   - http://127.0.0.1:5000/index.html         → Normal content from index.html
   - http://127.0.0.1:5000/Xindex.html → Secure view with decryption key prompt
   ```
6. Enter AES Key:
   > mysecretkey12345
   → Reveals the hidden image

KEY FEATURES:
----------------
- No content overwrite: index.html is preserved 100% as-is
- Separation of public and encrypted content
- Simple AES integration for controlled access

