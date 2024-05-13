import csv
import os.path

if __name__ == "__main__":

    origin_path = "./grader.txt"
    output_dir = "./grader_hierspeech"
    output_file_name = "input_list.csv"

    try:
        with open(origin_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]

    except Exception as e:
        print(f"An error occurred: {e}")
        lines = []

    input_text_list = []
    input_prompt_list = []

    unique_prompt = set([])

    for line in lines:
        title = f"""texts/{line.split("|")[0]}.txt"""
        prompt = f"""style_prompts/{line.split("|")[1]}_{line.split("|")[4]}.wav"""

        unique_prompt.add(prompt)

        text_file_path = os.path.join(output_dir, title)
        with open(text_file_path, 'w') as file:
            # 写入字符串到文件
            file.write(line.split("|")[3])

        input_text_list.append(title)
        input_prompt_list.append(prompt)

    assert len(input_text_list) == len(input_prompt_list), "Lists must be of the same length"

    # 文件名
    output_path = os.path.join(output_dir, output_file_name)

    # 打开文件，准备写入
    with open(output_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # 写入每一对 input_txt 和 input_prompt
        for text, prompt in zip(input_text_list, input_prompt_list):
            writer.writerow([text, prompt])

    print(f'Data written to {output_path}')

    print(f"unique prompts:")

    ls = sorted(list(unique_prompt))

    for i in ls:
        print(i)
