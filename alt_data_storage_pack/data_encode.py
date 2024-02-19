# Encodes text to video of white and black pixels

from PIL import Image, ImageDraw
import imageio
import numpy as np

class VideoEncode:
    '''
    To initialise, input file location and output file location needs to be
    provided (ex. 'folder\input_folder\input.txt', 'folder\output_folder\output.mp4')
    '''
    def __init__(self, input_location, output_location):
        self.text = self.open_text(input_location)
        self.output_location = output_location

    def open_text(self, location):
        with open(location, 'r') as f:
            text = f.readlines()
        return text
    
    def char_to_bin(self, char):
        # encodes a single char to UTF-8 binary string
        return ''.join([f'{i:08b}' for i in char.encode('UTF-8')])

    def text_to_bin(self):
        # encodes str text to UTF-8 binary string
        return ''.join([self.char_to_bin(item) for item in self.text])
    
    def frame_generate(self, text):
        # generates a frame from binary string
        pixel_len = 2
        width, height = 1920, 1072
        x, y = 0, 0
        image = Image.new("RGB", (width, height), "black")
        draw = ImageDraw.Draw(image)

        for i in text:
            if x >= width:
                y+= pixel_len
                x=0
            if i == "1":
                draw.rectangle([x, y, x + pixel_len-1, y + pixel_len-1], fill="white")
            x+= pixel_len
        
        return image

    def video_generate(self):
        # generates video from binary string
        pixel_len = 2
        width, height = 1920, 1072
        # max_char_per_frame is amount of bin chars that fit in 1 image
        max_char_per_frame = int(width * height / (pixel_len**2))
        frames = []
        bin_str = self.text_to_bin()

        i = 0
        # creates frames, fills with data
        while len(bin_str[i*max_char_per_frame:]) > max_char_per_frame:
            str_chunk = bin_str[i*max_char_per_frame : (i+1)*max_char_per_frame]
            frames.append(np.array(self.frame_generate(str_chunk)))
            i+=1
        # create numpy array of frames
        frames.append(np.array(self.frame_generate(bin_str[i*max_char_per_frame:])))
        # write video
        with imageio.get_writer(self.output_location, fps=1) as writer:
            i = 1
            for frame in frames:
                writer.append_data(frame)
                print(f"frame {i}")
                i+= 1

        print("\nconversion done\n")


if __name__ == "__main__":
    # just various testing FOR NOW

    with open('input_data\\input_text\\altoriu_sesely.txt', 'r') as f:
        sample_text = f.readlines()
    print("\nreading input text done\n")

    video = VideoEncode(sample_text)
    video.video_generate()