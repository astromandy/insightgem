def generate_profile(df):
    lines = []
    lines.append("Rows: %d, Columns: %d" % df.shape)
    lines.append("\nMissing Values:")
    lines.append(df.isnull().sum().to_string())
    lines.append("\nCorrelation Matrix:")
    lines.append(df.corr(numeric_only=True).to_string())
    return "\n\n".join(lines)
