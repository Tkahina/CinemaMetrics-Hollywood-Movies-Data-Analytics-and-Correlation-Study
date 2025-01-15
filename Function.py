def analyze_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    




    # Display some statistics about the outliers
    print(f"\nOutlier Analysis for {column}:")
    print(f"Number of outliers: {len(outliers)}")
    print(outliers[column].describe())
    print(f"Percentage of outliers: {(len(outliers) / len(df)) * 100:.2f}%")
    #print(outliers)

    #print(f"Lower Bound: {lower_bound:.2f}")
    #print(f"Upper Bound: {upper_bound:.2f}")



    
    return outliers