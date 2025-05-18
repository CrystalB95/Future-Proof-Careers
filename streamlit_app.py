import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Future-Proof Careers", layout="wide")

# Load data
df_bls = pd.read_csv("data/bls_job_outlook.csv")
df_salary = pd.read_csv("data/levels_fyi_salaries.csv")
df_remote = pd.read_csv("data/remote_jobs.csv")
df_skills = pd.read_csv("data/job_skills.csv")

st.title("🔮 Future-Proof Careers: Remote, High-Growth, and High-Paying")
st.markdown("Explore career paths using real data from BLS, Levels.fyi, and more.")

# SECTION: Growth Chart
st.subheader("📈 Top Growing Careers (2024–2034)")
top_jobs = df_bls.sort_values(by='projected_growth_rate', ascending=False).head(10)

fig, ax = plt.subplots()
sns.barplot(data=top_jobs, x='projected_growth_rate', y='occupation', ax=ax)
ax.set_title('Top 10 Fastest Growing Careers')
ax.set_xlabel('Growth Rate (%)')
st.pyplot(fig)

# SECTION: Salary Comparison
st.subheader("💼 Salary by Career Level")
job_selected = st.selectbox("Select a job title", df_salary["job_title"].unique())
selected = df_salary[df_salary["job_title"] == job_selected]

st.write(selected.melt(id_vars="job_title", var_name="Level", value_name="Salary"))

fig2, ax2 = plt.subplots()
sns.barplot(data=selected.melt(id_vars="job_title", var_name="Level", value_name="Salary"),
            x='Level', y='Salary', ax=ax2)
ax2.set_title(f"Salary Range for {job_selected}")
st.pyplot(fig2)

# SECTION: Remote Friendliness
st.subheader("🌐 Remote-Friendly Jobs")
df_remote["remote_percent"] = (df_remote["remote_job_postings"] / df_remote["total_job_postings"]) * 100
remote_sorted = df_remote.sort_values(by="remote_percent", ascending=False)

st.dataframe(remote_sorted[["job_title", "remote_percent"]].head(10))

# SECTION: Skills Heatmap
st.subheader("🧠 Common Skills Across Roles")
skill_data = df_skills.set_index("job_title")
fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.heatmap(skill_data.T, cmap="YlGnBu", cbar=False, linewidths=.5, annot=True)
st.pyplot(fig3)

st.markdown("---")
st.caption("Built by Crystal Barrow | [GitHub](https://github.com/CrystalB95)")
