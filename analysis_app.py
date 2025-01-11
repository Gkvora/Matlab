import streamlit as st # type: ignore

# python -m streamlit run "//Sfs.net/BIA/BIA_FT/shani/project/web site/code/analysis_app.py" --server.port 8501

create_page = st.Page("doc.py", title="Documentation")
create_page1 = st.Page("streamlit_app.py", title="Reports")
create_page2 = st.Page(r"\\Sfs.net\BIA\BIA_FT\shani\project\web site\Dmand Check\Code\main.py", title="Demand Check")

# create_page2 = st.Page("testing_version_4.py", title="8501")
# create_page3 = st.Page(r"\\Sfs.net\BIA\BIA_FT\shani\project\image arrange (piyushbhai)\code\second version.py", title="8503")

pg = st.navigation([create_page1,create_page2,create_page])
# pg = st.navigation([create_page,create_page1,create_page2,create_page3])

pg.run()