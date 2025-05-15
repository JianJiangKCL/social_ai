import json
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def extract_emotion(text):
    """Extract emotion from the text using regex."""
    match = re.search(r"Emotion: (\w+)", text)
    if match:
        return match.group(1)
    return None

def load_jsonl(file_path):
    """Load and parse JSONL file."""
    predictions = []
    ground_truth = []
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            try:
                # Handle potential truncated JSON
                if line.endswith('{"re'):
                    line = line[:-5]
                
                data = json.loads(line)
                
                # Extract predicted and ground truth emotions
                pred_emotion = extract_emotion(data["response"])
                true_emotion = extract_emotion(data["labels"])
                
                if pred_emotion and true_emotion:
                    predictions.append(pred_emotion)
                    ground_truth.append(true_emotion)
            except json.JSONDecodeError:
                print(f"Error parsing JSON: {line[:50]}...")
                continue
    
    return predictions, ground_truth

def plot_confusion_matrix(y_true, y_pred, labels=None):
    """Plot confusion matrix using seaborn."""
    if not labels:
        # Get unique emotions maintaining order of appearance
        labels = sorted(list(set(y_true) | set(y_pred)))
    
    # Calculate confusion matrix
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    
    # Calculate percentages
    cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
    
    # Create figure
    plt.figure(figsize=(10, 8))
    
    # Plot heatmap
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    
    # Add labels
    plt.ylabel('True Emotion')
    plt.xlabel('Predicted Emotion')
    plt.title('Confusion Matrix')
    
    # Save the figure
    plt.tight_layout()
    plt.savefig('confusion_matrix.png')
    print("Confusion matrix saved as 'confusion_matrix.png'")
    
    # Also plot percentage confusion matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm_percent, annot=True, fmt='.1f', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.ylabel('True Emotion')
    plt.xlabel('Predicted Emotion')
    plt.title('Confusion Matrix (Percentages)')
    plt.tight_layout()
    plt.savefig('confusion_matrix_percent.png')
    print("Percentage confusion matrix saved as 'confusion_matrix_percent.png'")

def main():
    input_file = 'test_output.jsonl'
    
    # Load and parse data
    print(f"Analyzing results from {input_file}...")
    predictions, ground_truth = load_jsonl(input_file)
    
    # Print basic stats
    print(f"Total samples analyzed: {len(predictions)}")
    
    # Calculate and print accuracy
    accuracy = accuracy_score(ground_truth, predictions)
    print(f"Overall accuracy: {accuracy:.2%}")
    
    # Print classification report
    print("\nClassification Report:")
    print(classification_report(ground_truth, predictions))
    
    # All possible emotions
    emotion_labels = ["Happy", "Sad", "Neutral", "Angry", "Surprise", "Disgust", "Fear"]
    
    # Plot confusion matrix
    plot_confusion_matrix(ground_truth, predictions, emotion_labels)
    
    # Count by emotion
    emotion_counts = {}
    for emotion in ground_truth:
        emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
    
    print("\nGround Truth Emotion Distribution:")
    for emotion, count in emotion_counts.items():
        print(f"{emotion}: {count} samples")

if __name__ == "__main__":
    main() 