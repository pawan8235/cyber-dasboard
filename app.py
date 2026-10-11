import csv
import os
import matplotlib.pyplot as plt

def analyze_security_logs():
    file_path = "security_logs.csv"
    
    try:
        # Step 1: Agar CSV file nahi hai, toh sample data create karna
        if not os.path.exists(file_path):
            sample_data = [
                ['Scan_ID', 'Check_Type', 'Security_Score'],
                [1, 'Password', 85],
                [2, 'URL', 40],
                [3, 'Password', 95],
                [4, 'URL', 30],
                [5, 'Password', 60]
            ]
            with open(file_path, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(sample_data)
        
        # Step 2: Built-in CSV module se data read karna
        scan_ids = []
        scores = []
        
        with open(file_path, mode='r') as f:
            reader = csv.DictReader(f)
            print("--- Security Logs Loaded Successfully ---")
            for row in reader:
                print(f"Scan ID: {row['Scan_ID']} | Type: {row['Check_Type']} | Score: {row['Security_Score']}")
                scan_ids.append(int(row['Scan_ID']))
                scores.append(int(row['Security_Score']))

        # Step 3: Python built-in functions se Analytics nikalna
        avg_score = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)

        print("\n--- Analytics Summary ---")
        print(f"Average Security Score: {avg_score:.2f}")
        print(f"Highest Security Score: {max_score}")
        print(f"Lowest Security Score: {min_score}")

        # Step 4: Matplotlib se basic chart generate karna
        plt.figure(figsize=(7, 4))
        bar_colors = ['#3fb950' if s >= 60 else '#f85149' for s in scores]
        plt.bar(scan_ids, scores, color=bar_colors)
        
        plt.title('CyberTool Scan Performance Analytics')
        plt.xlabel('Scan ID')
        plt.ylabel('Security Score')
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        
        plt.savefig('security_chart.png')
        print("\nMatplotlib chart successfully generated and saved as 'security_chart.png'!")

    except Exception as e:
        # Step 5: Exception Handling - Errors ko handle karna
        print(f"An error occurred during data analytics processing: {e}")

if __name__ == "__main__":
    analyze_security_logs()