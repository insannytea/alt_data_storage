# Decodes video of black and white pixels into text

from PIL import Image, ImageDraw
import imageio
import numpy as np

class VideoDecode:
    '''
    To initialise, input file location and output file location needs to be
    provided (ex. 'folder\input_folder\input.mp4', 'folder\output_folder\output.txt')
    '''
    def __init__(self, input_location, output_location):
        self.video = self.open_video(input_location)
        self.output_location = output_location
    
    def open_video(self, location):
        video = imageio.get_reader(location, 'ffmpeg')
        return video

    def bin_to_char(self, bin_str):
        # decodes binary string in UTF-8 into a single char
        byte_data = int(bin_str, 2).to_bytes((len(bin_str) + 7) // 8, byteorder='big')
        char = byte_data.decode('UTF-8')
        return char
    
    def text_generate(self):
        decoded_text = self.video_decode()
        with open(self.output_location, 'w', encoding='utf-8') as f:
            f.write(decoded_text)

    def video_decode(self):
        # decode video into bin str
        bin_str = ""
        i = 1
        for frame in self.video:
            print(f"frame {i}")
            i += 1
            frame_pil = Image.fromarray(frame)
            # check for black frames
            if not frame_pil.getbbox():
                continue

            frame_data = self.frame_read(frame_pil)
            decoded_data = self.frame_decode(frame_data)
            bin_str += decoded_data
        return bin_str

    def frame_read(self, image):
        # reads frame pixels and transforms into binary string
        bin_str = ""
        pixel_len = 2
        width, height = 1920, 1072
        x, y = 0, 0
        # converts the image into greyscale for easier pixel color recognition
        image = image.convert('L')

        for i in range(int(width*height/(pixel_len**2))):
            if x >= width:
                y+= 2
                x=0

            # checks pixel colour, assigns value depending on threshold
            if image.getpixel((x, y)) < 128:
                bin_str += "0"
            else:
                bin_str += "1"
            x+= 2

        return bin_str

    def frame_decode(self, bin_str):
        # decodes binary string into string of chars
        decoded_str = ""
        for i in range(0, len(bin_str), 8):
            # takes bin string, iterates every 8 bits, finds num of bytes per char, converts to char
            if bin_str[i:i+2] == "10":
                continue
            if bin_str[i:i+8] == "0"*8:
                # QUICK BODGE - NEEDS A MORE RIGOROUS METHOD ON THE IMG ITSELF
                break
            elif bin_str[i] == "1":
                # decodes chars that are represented by more than 1 byte of data in unicode
                byte_len = self.str_to_sum(bin_str[i:i+4])
                str_upperbound = byte_len * 8
                decoded_str += self.bin_to_char(bin_str[i:i+str_upperbound])
            else:
                # decodes ascii chars a.k.a. chars that are represented by 1 byte of data
                decoded_str += self.bin_to_char(bin_str[i:i+8])
        return decoded_str

    def str_to_sum(self, u):
        # counts bytes of byte representation of char
        total_num = 0
        for item in u:
            if item == "0":
                return total_num
            total_num += int(item)
        return total_num
    
if __name__ == "__main__":
    video_decoder = VideoDecode('input_data\\input_video\\input.mp4')
    decoded_text = video_decoder.video_decode()
    with open('output_data\\output_text\\output.txt', 'w', encoding='utf-8') as f:
        f.write(decoded_text)