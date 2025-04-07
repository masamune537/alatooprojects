import pandas as pd
import statsmodels.api as sm

# Примерные данные
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Exam_Score': [50, 51, 53, 54, 58, 60, 62, 65, 69, 72]
}

df = pd.DataFrame(data)

# Независимая переменная (X) и зависимая (y)
X = df['Hours_Studied']
y = df['Exam_Score']

# Добавим константу (перехват)
X = sm.add_constant(X)

# Создаём модель
model = sm.OLS(y, X).fit()

# 1. Таблица регрессии
print("Full Regression Table:\n")
print(model.summary())

# 2. Информация о регрессии
print("\nRegression Info:")
print(f"R-squared: {model.rsquared}")
print(f"Adjusted R-squared: {model.rsquared_adj}")

# 3. Коэффициенты
print("\nRegression Coefficients:")
print(model.params)

# 4. P-значения
print("\nP-Values:")
print(model.pvalues)

# 5. R² отдельно
print("\nR-squared value:")
print(model.rsquared)