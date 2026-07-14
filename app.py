import streamlit as st
import pandas as pd

from ai import generate_sql, explain_sql
from database import create_database, run_query

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AI Text-to-SQL Generator",
    page_icon="🤖",
    layout="wide"
)

create_database()

# ----------------------------------
# SIDEBAR
# ----------------------------------

with st.sidebar:

    st.title("🤖 AI SQL Assistant")

    st.markdown("### Database Schema")

    st.code("""
employees

id
name
department
salary
""")

    st.divider()

    st.success("Powered by Gemini AI")

# ----------------------------------
# HEADER
# ----------------------------------

st.title("🤖 AI Text-to-SQL Generator")

st.caption(
    "Convert Natural Language into Executable SQL using Gemini AI"
)

st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "🤖 AI Model",
        "Gemini 2.5 Flash"
    )

with c2:
    st.metric(
        "🗄 Database",
        "SQLite"
    )

with c3:
    st.metric(
        "⚡ Status",
        "Ready"
    )

st.divider()

# ----------------------------------
# USER INPUT
# ----------------------------------

user_query = st.text_area(
    "Ask your database in plain English",
    placeholder="""
Examples

Show all employees

Show employees whose salary is greater than 50000

Show IT employees

Show average salary
""",
    height=180
)

generate = st.button(
    "🚀 Generate SQL",
    use_container_width=True
)

# ----------------------------------
# GENERATE SQL
# ----------------------------------

if generate:

    if user_query.strip():

        with st.spinner("🤖 Gemini is generating SQL..."):

            try:

                # Generate SQL
                sql = generate_sql(user_query)

                # Remove markdown if Gemini returns it
                sql = sql.replace("```sql", "").replace("```", "").strip()

                st.success("✅ SQL Generated Successfully!")

                st.subheader("📝 Generated SQL")

                st.code(sql, language="sql")

                # ----------------------------------
                # SQL EXPLANATION
                # ----------------------------------

                st.subheader("💡 SQL Explanation")

                explanation = explain_sql(sql)

                st.info(explanation)

                # ----------------------------------
                # EXECUTE SQL
                # ----------------------------------

                columns, rows = run_query(sql)

                st.subheader("📊 Query Results")

                if rows:

                    df = pd.DataFrame(rows, columns=columns)

                    st.dataframe(
                        df,
                        use_container_width=True
                    )

                    st.success(
                        f"✅ {len(df)} record(s) returned."
                    )

                    csv = df.to_csv(index=False)

                    st.download_button(
                        "📥 Download Results (CSV)",
                        csv,
                        file_name="query_results.csv",
                        mime="text/csv",
                        use_container_width=True
                    )

                else:

                    st.info(
                        "Query executed successfully but returned no records."
                    )

            except Exception as e:

                st.error(f"❌ {e}")

    else:

        st.warning("⚠ Please enter a question.")

# ----------------------------------
# FOOTER
# ----------------------------------

st.divider()

st.caption(
    "🚀 AI Text-to-SQL Generator | Powered by Gemini AI | Developed by Shruti Singh"
)