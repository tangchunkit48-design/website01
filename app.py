import streamlit as st

st.set_page_config(page_title="Talent Career Hub - UC-006", layout="centered")

# Session state initialization
if "page" not in st.session_state:
    st.session_state.page = "login"
if "post_data" not in st.session_state:
    st.session_state.post_data = {}
if "errors" not in st.session_state:
    st.session_state.errors = []

def go_to(page):
    st.session_state.page = page
    st.rerun()

# ---------- 1. LOGIN (IUC-002) ----------
if st.session_state.page == "login":
    st.title("Manager Login")
    st.caption("Step 1: Include IUC-002 log in as manager")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username and password:
            go_to("dashboard")
        else:
            st.error("Please enter username and password")

# ---------- 2. DASHBOARD ----------
elif st.session_state.page == "dashboard":
    st.title("Career Opportunity Post Page")
    st.caption("Step 2: Manager selects the “Create post” option")
    st.write("Welcome, Manager")
    if st.button("Create post", type="primary"):
        go_to("create_form")
    if st.button("Log out"):
        go_to("login")

# ---------- 4-8. CREATE FORM ----------
elif st.session_state.page == "create_form":
    st.title("Career Opportunity Post Creation Form")
    st.caption("Steps 4–8: System displays form → Manager enters data")

    # Show previous errors if any
    if st.session_state.errors:
        for err in st.session_state.errors:
            st.error(err)
        st.session_state.errors = []

    fields = st.multiselect(
        "AI / Cybersecurity Fields",
        ["Artificial Intelligence", "Cybersecurity", "Machine Learning", "Cloud Security", "Data Privacy"]
    )
    job_title = st.text_input("Job Title")
    job_role = st.text_input("Job Role")
    job_description = st.text_area("Job Description")
    skill_profile = st.text_area("Target Skill Profile")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Confirm", type="primary"):
            # Step 9-10: Check required fields
            missing = []
            if not fields:
                missing.append("AI / Cybersecurity Fields")
            if not job_title:
                missing.append("Job Title")
            if not job_role:
                missing.append("Job Role")
            if not job_description:
                missing.append("Job Description")
            if not skill_profile:
                missing.append("Target Skill Profile")

            if missing:
                st.session_state.errors = [f"Missing required field: {f}" for f in missing]
                st.rerun()
            else:
                # Steps 11, 13-16: Confirm and store
                st.session_state.post_data = {
                    "fields": fields,
                    "title": job_title,
                    "role": job_role,
                    "description": job_description,
                    "skill_profile": skill_profile,
                    "status": "Confirmed"
                }
                go_to("success")

    with col2:
        if st.button("Save as Draft"):
            st.info("Draft saved (EUC-004 – status set to Saved)")

    with col3:
        if st.button("Cancel"):
            # Step 12: Cancel
            st.session_state.post_data = {}
            go_to("dashboard")

    if st.button("Back to Dashboard"):
        go_to("dashboard")

# ---------- 15-16. SUCCESS ----------
elif st.session_state.page == "success":
    st.title("Post Created Successfully")
    st.caption("Steps 15–16: System displays the post and shows completion message")
    st.success("Career opportunity post has been created and stored with status “Confirmed”.")

    if st.session_state.post_data:
        st.subheader("Created Post")
        st.write(f"**Fields:** {', '.join(st.session_state.post_data['fields'])}")
        st.write(f"**Title:** {st.session_state.post_data['title']}")
        st.write(f"**Role:** {st.session_state.post_data['role']}")
        st.write(f"**Description:** {st.session_state.post_data['description']}")
        st.write(f"**Skill Profile:** {st.session_state.post_data['skill_profile']}")
        st.write(f"**Status:** {st.session_state.post_data['status']}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Dashboard"):
            go_to("dashboard")
    with col2:
        if st.button("Create Another Post"):
            st.session_state.post_data = {}
            go_to("create_form")
