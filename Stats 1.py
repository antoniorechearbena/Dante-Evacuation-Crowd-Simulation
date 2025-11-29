import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

FILE_PATH = r'C:\Users\nicol\Downloads\final_pressure_30.csv'
OUTPUT_FILE = 'clean_data.csv'
GRAPH_OUTPUT_FILE = 'average_duration_plot.png'

HEADER_ROW_INDEX = 6 
PRIMARY_KEYS = ['[run number]', 'number-people']

REDUNDANT_COLUMNS = [
    '[step]',
    'main-exit', 
    'northeast-exit', 
    'southeast-exit', 
    'north-exit', 
    'south-exit', 
    'staircase-exit', 
    'panic-backwards',
    'floor0-percent',
    'imaginary-walls?'
]

def load_and_clean_data(file_path):
    print(f"1. Loading data from {file_path}...")
    
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None

    try:
        df = pd.read_csv(file_path, header=HEADER_ROW_INDEX)
        print(f"Data loaded successfully. Initial shape: {df.shape}")

        df_cleaned = df.drop(columns=REDUNDANT_COLUMNS, errors='ignore')
        print(f"2. Removed redundant columns.")

        df_cleaned.dropna(subset=PRIMARY_KEYS + ['ticks', 'count people'], inplace=True)
        
        for col in PRIMARY_KEYS:
            if col not in df_cleaned.columns and col + ' ' in df_cleaned.columns:
                 df_cleaned.rename(columns={col + ' ': col}, inplace=True)

            if col in df_cleaned.columns:
                df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce').astype('Int64')
        
        if 'ticks' in df_cleaned.columns:
            df_cleaned['ticks'] = pd.to_numeric(df_cleaned['ticks'], errors='coerce')
            
            print("3. Sorting data...")
            df_cleaned.sort_values(by=PRIMARY_KEYS + ['ticks'], ascending=True, inplace=True)
        
        return df_cleaned
    except Exception as e:
        print(f"An error occurred during loading or cleaning: {e}")
        return None

def group_data(df_cleaned):
    print("\n5. Grouping data...")
    
    if not all(key in df_cleaned.columns for key in PRIMARY_KEYS):
        print("Error: Primary key columns are missing.")
        print(f"Available columns: {list(df_cleaned.columns)}")
        return None

    grouped_data = df_cleaned.groupby(PRIMARY_KEYS)
    
    print(f"Data grouped into {len(grouped_data)} unique run configurations.")
    
    return grouped_data

def plot_average_duration(df_cleaned):
    print("\n6. Calculating and plotting average run durations...")
    
    run_durations = df_cleaned.groupby(['[run number]', 'number-people'])['ticks'].max().reset_index()
    
    avg_duration_by_pop = run_durations.groupby('number-people')['ticks'].mean()
    
    print("Summary of Average Durations (Ticks):")
    print(avg_duration_by_pop)
    
    n_bars = len(avg_duration_by_pop)
    colors = plt.cm.viridis(np.linspace(0.2, 0.8, n_bars))
    
    ax = avg_duration_by_pop.plot(
        kind='bar', 
        figsize=(10, 6), 
        color=colors,
        edgecolor='none',
        rot=0 
    )
    
    ax.set_xlabel('Number of People')
    ax.set_ylabel('Average Duration (Ticks)')
    ax.set_title('Average Time to Complete Run by Population Size')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    
    plt.savefig(GRAPH_OUTPUT_FILE)
    print(f"Graph saved to {GRAPH_OUTPUT_FILE}")
    
    plt.show()

if __name__ == "__main__":
    
    cleaned_df = load_and_clean_data(FILE_PATH)

    print(f"\n4. Saving cleaned data to {OUTPUT_FILE}...")
    try:
        cleaned_df.to_csv(OUTPUT_FILE, index=False, mode='w') 
        print("File saved successfully.")
    except PermissionError:
        print(f"ERROR: Could not save to '{OUTPUT_FILE}'. File likely open in Excel.")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

    grouped_results = group_data(cleaned_df)
    
    plot_average_duration(cleaned_df)