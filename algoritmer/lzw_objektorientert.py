""" 
LZW algorithm from Geekific:
https://www.youtube.com/watch?v=1KzUikIae6k&ab_channel=Geekific

Translated from Java to python by chatGPT.
"""
import os
import sys
import cv2
import chardet

class LZW:
    def __init__(self,file_path):
        self.file_path = file_path
        self.image_extensions = ["jpg","png","gif","tiff","tif"]
        self.extension = self.file_path.split(".")[-1]
        self.isImage = False
        self.isBinary = False
        if self.extension in self.image_extensions:
            self.isImage = True
        elif self.extension == "wav":
            self.isBinary = True

    def readFile(self):
        with open(self.file_path,"r") as file:
            return file.read()
    
    def readBytes(self):
        with open(self.file_path, "rb") as file:
            binary_data = file.read()
            # Convert binary data to a binary (base 2) string
            binary_string = ''.join(format(byte, '08b') for byte in binary_data)
            return binary_string


    def encode_text(self,text):
        dict_size = 256
        # Builds a dict with unicode values up to 255 (ASCII table).
        dictionary = {chr(i): i for i in range(dict_size)}
        found_chars = ""
        result = []

        for character in text:
            chars_to_add = found_chars + character
            if chars_to_add in dictionary:
                found_chars = chars_to_add
            else:
                try:
                    dictionary[found_chars]
                except:
                    print(f"{found_chars} not found in dictionary, code {ord(found_chars)}.")
                    print("")
                result.append(dictionary[found_chars])
                dictionary[chars_to_add] = dict_size
                dict_size += 1
                found_chars = character

        if found_chars:
            result.append(dictionary[found_chars])
        #print(text)
        return result,dictionary,len(text), sys.getsizeof(text)


    def encode(self):
        if self.isBinary:
            print("Binary file is encoded.")
            text = self.readBytes()
            encoded_list, dictionary, length, size_of_data = self.encode_text(text)
        elif self.isImage:
            # Read the image using OpenCV
            img = cv2.imread(self.file_path, cv2.IMREAD_GRAYSCALE)
            # Convert the image to a comma-separated string
            image_1d = ','.join(map(str, img.flatten()))
            encoded_list, dictionary, length, size_of_data = self.encode_text(image_1d)
        else:
            text = self.readFile()
            #text, charset = self.readBytes()
            #print(f"charset: {charset}")
            encoded_list, dictionary, length, size_of_data = self.encode_text(text)
        return encoded_list, dictionary, length, size_of_data

    def decode(self,encoded_list):
        dict_size = 256
        dictionary = {i: chr(i) for i in range(dict_size)}
        characters = chr(encoded_list.pop(0))
        result = [characters]

        for code in encoded_list:
            if code in dictionary:
                entry = dictionary[code]
            else:
                entry = characters + characters[0]
            result.append(entry)
            dictionary[dict_size] = characters + entry[0]
            dict_size += 1
            characters = entry

        return ''.join(result)


#filename = "lzw.py"
#filename = "the_matrix_transcript.txt"
#filename = "peppers.png"
#filename = "ultralyd.jpg"
filename = "8bitHenrik.png"
#filename = "bibelen_king_james.txt"
#filename = "440Hz_short.wav"

lzw = LZW(filename)
encoded_list, dictionary, length, size_of_data= lzw.encode()
#print(dictionary)
#print("Encoded List:", encoded_list)

decoded_text = lzw.decode(encoded_list)

#print("Decoded Text:", decoded_text[:500])
#print("Decoded Text:", decoded_text[-500:])

# Calculate sizes
size_of_encoded_list = sys.getsizeof(encoded_list)
print(f"Size of encoded_list {size_of_encoded_list} bytes")
print(f"Size of data {size_of_data} bytes")
print(f"Compression ratio: {100*float(size_of_encoded_list/size_of_data):.1f} %.")
