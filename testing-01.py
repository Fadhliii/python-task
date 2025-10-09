import pandas as pd

# ganti sesuai nama file pastinya (pastikan .csv)
path = r"C:\Users\Jatibening-01\Desktop\s2 - programming\student_exam_scores.csv"

# coba deteksi pemisah umum
try:
    df = pd.read_csv(path)  # default koma
except:
    # kalau pakai titik koma (sering di-export dari Excel/locale ID)
    df = pd.read_csv(path, sep=';')
    
print(df.shape)
print(df.head(3))
print(df.columns.tolist())
