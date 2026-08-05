import pandas as pd
import numpy as np

print("📂 Reading data...")
xl = pd.ExcelFile('HR_Workforce_Analytics.xlsx')
df_emp = pd.read_excel(xl, sheet_name='Employees')
df_att = pd.read_excel(xl, sheet_name='Attrition')
df_rec = pd.read_excel(xl, sheet_name='Recruitment')
df_kpi = pd.read_excel(xl, sheet_name='Summary_KPIs')

print(f"✅ Loaded {len(df_emp)} employees")

# ── 1. Basic cleaning ──────────────────────────────────────
print("\n🔧 Cleaning data...")

# Clean text columns
for col in ['full_name', 'department', 'job_title', 'nationality', 'gender', 'city', 'status']:
    df_emp[col] = df_emp[col].str.strip()

# Convert date
df_emp['hire_date'] = pd.to_datetime(df_emp['hire_date'])

# Round years_of_service to 2 decimal places
df_emp['years_of_service'] = df_emp['years_of_service'].round(2)

# ── 2. Add new columns ────────────────────────────────
print("➕ Adding calculated columns...")

# Age group
def age_group(age):
    if age < 30:
        return 'Under 30'
    elif age < 40:
        return '30-39'
    elif age < 50:
        return '40-49'
    else:
        return '50+'

df_emp['age_group'] = df_emp['age'].apply(age_group)

# Salary band
def salary_band(sal):
    if sal < 10000:
        return 'Below 10K'
    elif sal < 15000:
        return '10K - 15K'
    elif sal < 20000:
        return '15K - 20K'
    else:
        return 'Above 20K'

df_emp['salary_band'] = df_emp['salary_sar'].apply(salary_band)

# Performance level
def perf_label(score):
    if score >= 4.5:
        return 'Excellent'
    elif score >= 3.5:
        return 'Good'
    elif score >= 3.0:
        return 'Acceptable'
    else:
        return 'Poor'

df_emp['performance_label'] = df_emp['performance_score'].apply(perf_label)

# Training category
def training_cat(hours):
    if hours < 20:
        return 'Low'
    elif hours < 50:
        return 'Medium'
    else:
        return 'High'

df_emp['training_category'] = df_emp['training_hours'].apply(training_cat)

# Saudi / non-Saudi
df_emp['is_saudi'] = df_emp['nationality'].apply(lambda x: 1 if x == 'Saudi' else 0)

# Experience category
def experience_cat(years):
    if years < 2:
        return 'New'
    elif years < 5:
        return 'Intermediate'
    elif years < 10:
        return 'Expert'
    else:
        return 'Veteran'

df_emp['experience_category'] = df_emp['years_of_service'].apply(experience_cat)

# ── 3. Saudization percentage by department ──────────────────────────────
print("📊 Calculating Saudization percentage per department...")

saudization = (
    df_emp.groupby('department')['is_saudi']
    .agg(total='count', saudis='sum')
    .assign(saudization_pct=lambda x: (x['saudis'] / x['total'] * 100).round(1))
    .reset_index()
)

# Merge Saudization percentage into the main table
df_emp = df_emp.merge(
    saudization[['department', 'saudization_pct']],
    on='department',
    how='left'
)

# ── 4. Clean Attrition table ─────────────────────────────
df_att['exit_date'] = pd.to_datetime(df_att['exit_date'])
df_att['exit_reason'] = df_att['exit_reason'].str.strip()
df_att['exit_type'] = df_att['exit_type'].str.strip()

# ── 5. Export cleaned file ───────────────────────────────
print("\n💾 Exporting file...")

output_path = 'HR_Cleaned.xlsx'
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df_emp.to_excel(writer, sheet_name='Employees_Cleaned', index=False)
    df_att.to_excel(writer, sheet_name='Attrition', index=False)
    df_rec.to_excel(writer, sheet_name='Recruitment', index=False)
    saudization.to_excel(writer, sheet_name='Saudization_By_Dept', index=False)
    df_kpi.to_excel(writer, sheet_name='Summary_KPIs', index=False)

print(f"✅ Exported: {output_path}")

# ── 6. Summary ─────────────────────────────────────────────
print("\n📋 Data summary:")
print(f"   Total employees: {len(df_emp)}")
print(f"   Saudi employees: {df_emp['is_saudi'].sum()} ({df_emp['is_saudi'].mean()*100:.1f}%)")
print(f"\n   Saudization percentage by department:")
print(saudization.to_string(index=False))
print(f"\n   New columns: age_group, salary_band, performance_label, training_category, is_saudi, experience_category, saudization_pct")
print("\n✅ Script completed successfully!")