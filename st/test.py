import cv2
import os

def create_mapping_dictionaries():
    d = {}
    c = {}
    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)
    return d, c

def encrypt_message(img, msg):
    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        m += 1
        z = (z + 1) % 3
    return img

def save_and_display_image(img, filename):
    cv2.imwrite(filename, img)
    try:
        os.system(f"start {filename}")
    except Exception as e:
        print(f"Error opening image: {e}")

def decrypt_message(img, msg, password):
    message = ""
    n, m, z = 0, 0, 0
    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        for i in range(len(msg)):
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
        print("Decrypted message:", message)
    else:
        print("Invalid key")

# Load image
img = cv2.imread("C:/Users/test/OneDrive/Desktop/st/mypic.jpg")

# Check if image is loaded successfully
if img is None:
    print("Error: Unable to load the image.")
else:
    # Get secret message and password
    msg = input("Enter secret message: ")
    password = input("Enter password: ")

    # Create mapping dictionaries
    d, c = create_mapping_dictionaries()

    # Encrypt message
    img = encrypt_message(img, msg)

    # Save and display the encrypted image
    save_and_display_image(img, "C:/Users/tset/OneDrive/Desktop/st/Encryptedmsg.jpg")

    # Decrypt message
    decrypt_message(img, msg, password)
