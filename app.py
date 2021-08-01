from urllib.parse import urlencode, parse_qs
import streamlit as st

initial_query_params = st.session_state.get("initial_query_params")
query_params = {k: v[0] for k, v in st.experimental_get_query_params().items()}
if not initial_query_params:
    initial_query_params = query_params.copy()
    st.session_state["initial_query_params"] = initial_query_params.copy()

st.write("Initial query params of the session:", initial_query_params)
st.write("Query params before setting new ones:", query_params)

new_query_string = st.text_area("New query params string (like 'a=b&c=d')", value=urlencode(initial_query_params))
if st.button("Set new query params without starting new session"):
    st.experimental_set_query_params(**parse_qs(new_query_string))
