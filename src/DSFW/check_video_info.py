import json
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def analyze_video_data(json_path):
    """
    Analyzes video data from a JSON file.

    Args:
        json_path (str): Path to the JSON file containing video information.
    """
    try:
        with open(json_path, 'r') as f:
            video_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_path}")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {json_path}")
        return

    existing_video_durations = []
    non_existent_videos = []

    total_videos = len(video_data)
    print(f"Found {total_videos} video entries in the JSON file.")

    for i, item in enumerate(video_data):
        video_path = item.get("video_path")
        if not video_path:
            print(f"Warning: Entry {i} is missing 'video_path'. Skipping.")
            continue

        if os.path.exists(video_path):
            try:
                cap = cv2.VideoCapture(video_path)
                if not cap.isOpened():
                    print(f"Warning: Could not open video file: {video_path}. Skipping.")
                    non_existent_videos.append(video_path + " (could not open)")
                    continue

                fps = cap.get(cv2.CAP_PROP_FPS)
                frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

                if fps > 0 and frame_count > 0:
                    duration = frame_count / fps
                    existing_video_durations.append(duration)
                else:
                    print(f"Warning: Could not get valid FPS ({fps}) or frame count ({frame_count}) for video: {video_path}. Skipping.")
                    non_existent_videos.append(video_path + " (invalid metadata)")
                cap.release()
            except Exception as e:
                print(f"Error processing video {video_path}: {e}")
                non_existent_videos.append(video_path + f" (processing error: {e})")
        else:
            non_existent_videos.append(video_path)
        
        if (i + 1) % 100 == 0:
            print(f"Processed {i + 1}/{total_videos} videos...")

    print(f"\n--- Analysis Complete ---")

    if non_existent_videos:
        print(f"\nFound {len(non_existent_videos)} non-existent or problematic videos:")
        for video_path in non_existent_videos:
            print(f"  - {video_path}")
    else:
        print("\nAll video paths checked exist and were processed (or skipped if metadata was invalid).")

    if existing_video_durations:
        print(f"\n--- Duration Analysis for {len(existing_video_durations)} Existing Videos ---")
        durations_np = np.array(existing_video_durations)
        print(f"Min duration: {np.min(durations_np):.2f} seconds")
        print(f"Max duration: {np.max(durations_np):.2f} seconds")
        print(f"Mean duration: {np.mean(durations_np):.2f} seconds")
        print(f"Median duration: {np.median(durations_np):.2f} seconds")
        print(f"Standard deviation: {np.std(durations_np):.2f} seconds")

        # Plotting duration distribution
        plt.figure(figsize=(10, 6))
        plt.hist(durations_np, bins=30, edgecolor='black')
        plt.title('Video Duration Distribution')
        plt.xlabel('Duration (seconds)')
        plt.ylabel('Number of Videos')
        plt.grid(True)
        
        plot_filename = "video_duration_distribution.png"
        try:
            plt.savefig(plot_filename)
            print(f"\nDuration distribution plot saved as {plot_filename}")
        except Exception as e:
            print(f"Error saving plot: {e}")
        plt.show()
        
        # Print common durations
        print("\n--- Common Durations (Top 10) ---")
        rounded_durations = [round(d, 1) for d in existing_video_durations] # Round to 1 decimal place
        duration_counts = Counter(rounded_durations)
        most_common_durations = duration_counts.most_common(10)
        for duration, count in most_common_durations:
            print(f"  - {duration:.1f} seconds: {count} videos")

    else:
        print("\nNo valid video durations found to analyze.")

if __name__ == "__main__":
    json_file_path = "/data/jj/proj/AFF/data/train_set_1.json"
    analyze_video_data(json_file_path)
    print("\nScript finished.") 