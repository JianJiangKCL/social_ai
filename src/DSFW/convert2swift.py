import json
import argparse
import os

def convert_to_jsonl(input_json_path, output_jsonl_path):
    """
    Converts a JSON file to a JSONL file with a specific format.

    Args:
        input_json_path (str): Path to the input JSON file.
        output_jsonl_path (str): Path to the output JSONL file.
    """
    try:
        with open(input_json_path, 'r', encoding='utf-8') as infile:
            data = json.load(infile)
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_json_path}")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {input_json_path}")
        return

    with open(output_jsonl_path, 'w', encoding='utf-8') as outfile:
        for item in data:
            video_path = item.get("video_path")
            label = item.get("label")

            if not video_path or not label:
                print(f"Warning: Skipping item due to missing 'video_path' or 'label': {item}")
                continue

            output_data = {
                "messages": [
                    {
                        "role": "system",
                        "content": "you are a expert in video analysis, given the video, you will answer the question"
                    },
                    {
                        "role": "user",
                        "content": "<video> What is the person's emotion? Choose from the following options: Happy, Sad, Neutral, Angry, Surprise, Disgust, Fear. Please provide your answer in the format: 'Emotion: [emotion]'"
                    },
                    {
                        "role": "assistant",
                        "content": f"Emotion: {label}"
                    }
                ],
                "videos": [video_path]
            }
            outfile.write(json.dumps(output_data) + '\n')
    print(f"Successfully converted {input_json_path} to {output_jsonl_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a JSON file to JSONL format.")
    parser.add_argument("--input_file", default="/data/jj/proj/AFF/data/DSFW/test_set_1.json", help="Path to the input JSON file.")
    args = parser.parse_args()

    input_file = args.input_file
    # Determine output file path
    base, ext = os.path.splitext(input_file)
    output_file = base + ".jsonl"

    convert_to_jsonl(input_file, output_file) 