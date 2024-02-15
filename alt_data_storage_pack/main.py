import os
from data_encode import VideoEncode
from data_decode import VideoDecode

def welcome_greet():
    # Greets user when launching app
    with open('assets\\welcome.txt', 'r') as f:
        welcome = f.read()
    print(welcome)

def files_list(target_folder):
    # Returns dict of file names in target_folder
    script_dir = os.path.dirname(__file__)
    project_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
    folder_path = os.path.join(project_dir, target_folder)

    if os.path.isdir(folder_path):
        file = os.listdir(folder_path)
        files = {}

        for file_name in enumerate(file, 1):
            files[file_name[0]] = file_name[1]
    else:
        print("No such directory.")
        return
    return files

def text_to_vid(input_name, output_name):
    # converts text to video
    video_encoder = VideoEncode(f'input_data\\input_text\\{input_name}', f'output_data\\output_video\\{output_name}')
    video_encoder.video_generate()
    print(f"Text successfully converted!\n")

def vid_to_text(input_name, output_name):
    # converts video to text
    video_decoder = VideoDecode(f'input_data\\input_video\\{input_name}', f'output_data\\output_text\\{output_name}')
    video_decoder.text_generate()
    print(f"Video successfully converted!\n")

# Error handling funcs
def choose_input(target_dir):
    # handles errors when user chooses files to be converted
    files = files_list(f"input_data\\{target_dir}")
    if not files:
        print(f"\nNo files in \'{target_dir}\'\n")
        return 'b'
    print(files)
    while True:
        choice = input("Choose file to convert or 'b' to return to menu: ")
        if choice == 'b':
            return 'b'
        try:
            choice_num = int(choice)
        except ValueError:
            print(f"\n\'{choice}\' is not a valid file number. Try again")
            continue
        if choice_num < 1 or choice_num > len(files):
            print(f"\nNo such file with index \'{choice_num}\'. Try again")
            continue
        break
    input_name = files[choice_num]
    return input_name #returns str of file name

# Main Logic
if __name__ == "__main__":
    pass

welcome_greet()

while True:
    menu = "e - encode(convert .txt into .mp4)\nd - decode(convert .mp4 into .txt)\nq - quit"
    print(menu)
    choice = input()

    if choice == "e":
        input_name = choose_input("input_text")
        if input_name == 'b':
            continue
        output_name = input("Name your new file: ") + ".mp4"

        text_to_vid(input_name, output_name)
        print("\ndone\n")

    elif choice == "d":
        input_name = choose_input("input_video")
        if input_name == 'b':
            continue
        output_name = input("Name your new file: ") + ".txt"

        vid_to_text(input_name, output_name)
        print("\ndone\n")

    elif choice == "q":
        print("\nBye!\n")
        quit()

    else:
        print(f"{choice} is NOT an option.\nTry again\n")