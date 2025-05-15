import csv
import json
import os
import argparse

def convert_csv_to_json(csv_file_path, json_file_path, video_base_path):
    emotion_mapping = {
        "1": "Happy",
        "2": "Sad",
        "3": "Neutral",
        "4": "Angry",
        "5": "Surprise",
        "6": "Disgust",
        "7": "Fear"
    }

    try:
        all_records = []
        with open(csv_file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if reader.fieldnames != ['video_name', 'label']:
                print(f"Warning: Expected CSV headers 'video_name,label', but got {reader.fieldnames}")
                # Attempt to proceed if possible, assuming first col is video_name and second is label
                # This might need adjustment if the actual column names are different and critical

            for row in reader:
                video_name = row.get('video_name')
                label_num = row.get('label')

                if video_name is None or label_num is None:
                    print(f"Warning: Skipping row due to missing 'video_name' or 'label': {row}")
                    continue

                emotion_str = emotion_mapping.get(label_num)

                if emotion_str is None:
                    print(f"Warning: Unknown label '{label_num}' for video_name '{video_name}'. Skipping.")
                    continue

                video_file_name = f"{int(video_name):05d}.avi" # Assuming .avi extension
                full_video_path = os.path.join(video_base_path, video_file_name)

                json_record = {
                    "video_name": video_name,
                    "label": emotion_str,
                    "video_path": full_video_path
                }
                all_records.append(json_record)

        with open(json_file_path, 'w') as jsonfile:
            json.dump(all_records, jsonfile, indent=4) # Added indent for readability

        print(f"Successfully converted '{csv_file_path}' to '{json_file_path}'")

    except FileNotFoundError:
        print(f"Error: Input CSV file not found at '{csv_file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Determine the directory of the script for relative path construction
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the new default parent directory for the output JSON file
    default_output_json_parent_dir = "/data/jj/proj/AFF/data/DSFW"

    # --- Define default for CSV input ---
    # Primary default CSV: relative to script (e.g., "set_1.csv")
    primary_default_csv_filename = "set_1.csv"
    primary_default_csv_path = os.path.join(script_dir, primary_default_csv_filename)
    
    # Fallback default CSV: a specific absolute path
    fallback_default_csv_path = "/data/datasets/affective/DFEW/data_in_use/train_set_1.csv"

    # Determine the effective default CSV path that will be used
    effective_default_csv_path = primary_default_csv_path
    if not os.path.exists(primary_default_csv_path) and os.path.exists(fallback_default_csv_path):
        print(f"Note: Defaulting CSV input to absolute path: {fallback_default_csv_path} as relative one ({primary_default_csv_path}) was not found.")
        effective_default_csv_path = fallback_default_csv_path
    # If primary_default_csv_path doesn't exist and fallback_default_csv_path also doesn't exist,
    # effective_default_csv_path will be primary_default_csv_path.
    # The check `if not os.path.exists(args.csv_file_path):` later will catch this if needed.

    # --- Define default for JSON output ---
    # The JSON filename is derived from the basename of the *effective_default_csv_path*.
    csv_basename_for_json = os.path.basename(effective_default_csv_path) 
    json_filename_default = os.path.splitext(csv_basename_for_json)[0] + ".json"

    # Construct the default JSON file path using the new parent directory and derived filename.
    effective_default_json_path = os.path.join(default_output_json_parent_dir, json_filename_default)

    # --- Define default for video base path ---
    default_video_base_path = "/data/datasets/affective/DFEW/Clip/clip_224x224_avi/"

    parser = argparse.ArgumentParser(description="Convert a CSV file to JSON format, adding video paths.")
    parser.add_argument(
        "--csv_file_path",
        type=str,
        default="/data/jj/proj/AFF/data/DSFW/train_set_1.csv",
        help=f"Path to the input CSV file. Default is intelligently chosen, currently: '{effective_default_csv_path}'."
    )
    parser.add_argument(
        "--json_file_path",
        type=str,
        default=effective_default_json_path,
        help=f"Path for the output JSON file. Default is intelligently chosen (output dir: '{default_output_json_parent_dir}'), currently: '{effective_default_json_path}'."
    )
    parser.add_argument(
        "--video_base_path",
        type=str,
        default=default_video_base_path,
        help="Base path for the video files."
    )

    args = parser.parse_args()

    # Ensure the input CSV file exists before proceeding
    if not os.path.exists(args.csv_file_path):
        print(f"Error: Input CSV file not found at the specified or default path: '{args.csv_file_path}'")
        print("Please ensure the CSV file exists or provide the correct path using --csv_file_path.")
        exit(1)
            
    convert_csv_to_json(args.csv_file_path, args.json_file_path, args.video_base_path) 