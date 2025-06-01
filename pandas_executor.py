def safe_pandas_eval(code: str, df):
    allowed_builtins = {"len": len, "sum": sum, "min": min, "max": max, "round": round, "sorted": sorted}
    globals_dict = {"__builtins__": allowed_builtins}
    locals_dict = {"df": df.copy()}
    exec(code, globals_dict, locals_dict)
    for k in locals_dict:
        if k not in ["df"]:
            return locals_dict[k]
    return "Code executed but no result returned."
