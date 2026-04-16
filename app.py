import pandas as pd
import argparse
import json
import sys

def analyze_data(file_path):
    try:
        df = pd.read_csv(file_path)
        
        # Generamos un resumen técnico para la IA
        report = {
            "num_rows": int(df.shape[0]),
            "num_cols": int(df.shape[1]),
            "columns": list(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
            "data_types": {col: str(dtype) for col, dtype in df.dtypes.items()},
            "summary": "Análisis completado con éxito."
        }
        
        return json.dumps(report, indent=4)
    except Exception as e:
        return json.dumps({"error": str(e)})

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Analizador de CSV para ML")
    parser.add_argument("--file", required=True, help="Ruta al archivo CSV")
    args = parser.parse_args()
    
    result = analyze_data(args.file)
    print(result)

if __name__ == "__main__":
    main()


