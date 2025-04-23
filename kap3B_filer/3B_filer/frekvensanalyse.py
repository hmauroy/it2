import matplotlib.pyplot as plt
import pandas as pd
import sys
from collections import Counter
import re

def analyze_character_frequency(file_path):
    # Try different encodings
    encodings = ['iso-8859-1', 'latin-1', 'cp1252', 'utf-8']
    
    for encoding in encodings:
        try:
            # Read the text file with specified encoding
            with open(file_path, 'r', encoding=encoding) as file:
                text = file.read()
            
            # Count total characters (excluding whitespace)
            total_chars = len(re.sub(r'\s', '', text))
            
            # Count occurrences of each character
            char_counts = Counter(text.lower())
            
            # Filter out only whitespace, calculate percentages for everything else
            letters_dict = {}
            for char, count in char_counts.items():
                if not char.isspace():  # Exclude whitespace
                    percentage = (count / total_chars) * 100
                    letters_dict[char] = percentage
            
            print(f"Successfully read file using {encoding} encoding.")
            print(f"Found {len(letters_dict)} unique non-whitespace characters.")
            
            # Create dataframe directly from dictionary
            df = pd.DataFrame(list(letters_dict.items()), columns=['Character', 'Percentage'])
            
            # Sort by percentage in descending order
            df = df.sort_values('Percentage', ascending=False)
            
            return df
            
        except UnicodeDecodeError:
            print(f"Failed to decode with {encoding}, trying next encoding...")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)
    
    print("Error: Could not decode the file with any of the attempted encodings.")
    sys.exit(1)

def plot_character_frequency(df):
    # Set a larger figure for better visibility with many characters
    plt.figure(figsize=(16, 10))
    
    # Create the plot - use the index as x to ensure proper spacing
    bars = plt.bar(range(len(df)), df['Percentage'], color='skyblue', edgecolor='black')
    
    # Add percentage labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                 f'{height:.2f}%', ha='center', va='bottom', fontsize=9)
    
    # Add the character labels
    plt.xticks(range(len(df)), df['Character'], rotation=45)
    
    # Add labels and title
    plt.xlabel('Characters')
    plt.ylabel('Frequency (%)')
    plt.title('Character Frequency Distribution (Descending Order)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add a legend showing each character and its actual representation
    for idx, char in enumerate(df['Character']):
        plt.annotate(f"'{char}'", 
                     xy=(idx, -1), 
                     xycoords='data', 
                     ha='center', 
                     va='top',
                     fontsize=8,
                     color='darkblue')
    
    # Adjust layout and save
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)  # Make room for character annotations
    plt.savefig('character_frequency.png', dpi=300)
    plt.show()
    
    # Also save the data to CSV for reference
    df.to_csv('character_frequency.csv', index=False)
    print("Frequency data also saved to 'character_frequency.csv'")

def main():
    if len(sys.argv) < 2:
        print("Usage: python char_frequency.py <file_path>")
        file_path = input("Enter the file path: ")
    else:
        file_path = sys.argv[1]
    
    df = analyze_character_frequency(file_path)
    
    # Print all characters found for verification
    print("\nCharacters found in the text (in descending frequency order):")
    for idx, row in df.iterrows():
        char = row['Character']
        percentage = row['Percentage']
        print(f"'{char}': {percentage:.2f}%", end="  ")
        if (idx + 1) % 5 == 0:  # Line break every 5 characters for readability
            print()
    print("\n")
    
    plot_character_frequency(df)
    print("Analysis complete. Results saved as 'character_frequency.png'")

if __name__ == "__main__":
    main()