# save as decode.py and run: python3 decode.py
import requests

# Get the text
text = """T​h‌e​ ​M‌a​n‌u‌s‌c‌r‌i‌p​t‌ ​o‌f​ ‌S‌h​a​d​o‌w​s​

I‌n​ ‌t​h​e‌ ‌q​u‌i​e‌t​ ‌h​a​l​l‌s​ ‌o​f‌ ​t‌h​e‌ ‌f‌o‌r​g‌o‌t​t‌e‌n​ ‌l​i​b​r​a‌r‌y‌,​ ​w​h‌e​r‌e‌ ​d​u‌s​t​ ​s‌e‌t​t​l‌e​s​ ​u​p‌o‌n​ ​a‌n‌c​i‌e‌n​t‌ ‌t‌o​m‌e‌s​
a‌n‌d‌ ‌m‌o​o‌n‌l‌i​g‌h​t​ ​f‌i‌l‌t​e​r‌s​ ​t‌h‌r‌o​u‌g​h‌ ​c‌r‌a‌c​k‌e​d​ ​w‌i‌n​d‌o​w​s​,​ ‌t​h‌e‌r‌e‌ ‌e​x‌i‌s​t​s​ ‌a​ ​p​e‌c‌u​l​i‌a‌r​ ‌d‌o‌c​u‌m​e​n​t‌.‌
W‌r​i‌t‌t‌e​n​ ‌b‌y​ ​a‌n‌ ​u​n‌k‌n​o​w‌n‌ ​s‌c‌h​o‌l‌a‌r​ ​c‌e‌n‌t‌u‌r​i‌es ago, it speaks of hidden knowledge."""

# Extract zero-width characters
hidden = []
for char in text:
    if ord(char) in [8203, 8204, 8205, 8206, 8207, 8236, 8237, 65279]:
        hidden.append(char)

print(f"Found {len(hidden)} hidden characters")

# Map to binary
mapping = {
    '\u200b': '0',  # zero-width space
    '\u200c': '1',  # zero-width non-joiner
    '\u200d': ' ',  # zero-width joiner
}

binary = ''
for h in hidden:
    if h in mapping:
        binary += mapping[h]

print(f"Binary: {binary}")

# Convert to text
result = ''
for i in range(0, len(binary), 8):
    byte = binary[i:i+8]
    if len(byte) == 8:
        result += chr(int(byte, 2))

print(f"Flag: {result}")