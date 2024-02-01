from pathlib import Path
import streamlit as st
from PIL import Image
import json
import webbrowser
# FILE PATHS

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "picture.jpg"
icon_pic = current_dir / "assets" / "icon.png"
sections_file = current_dir / "assets" / "01_sections.json"
header_file = current_dir / "assets" / "02_header.json"
social_media_file = current_dir / "assets" / "03_social_media.json"
skills_file = current_dir / "assets" / "04_skills.json"
work_experience_file = current_dir / "assets" / "05_work_experience.json"
education_file = current_dir / "assets" / "06_education.json"
project_file = current_dir / "assets" / "07_projects.json"
publication_file = current_dir / "assets" / "08_publications.json"
public_speaking_file = current_dir / "assets" / "09_public_speaking.json"
certificates_file = current_dir / "assets" / "10_certificates.json"
accomplishments_file = current_dir / "assets" / "11_accomplishments.json"

with open(sections_file, "r") as sections_raw:
    sections_data = json.load(sections_raw)

# HEADER SECTION

with open(header_file, "r") as header_raw:
    header_data = json.load(header_raw)
st.set_page_config(page_title=header_data["PAGE_TITLE"], page_icon=Image.open(icon_pic))
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    st.image(profile_pic)
with col2:
    st.title(header_data["NAME"])
    st.write(header_data["DESCRIPTION"])
    if st.button("📄 Download Resume"):
        # Replace 'https://your-website.com' with the actual URL you want to redirect to
        webbrowser.open_new_tab('https://github.com/sasank-sasi/vin/blob/master/resume.pdf')
st.write('\n')

# SOCIAL MEDIA SECTIONa

if sections_data.get("SOCIAL_MEDIA"):
    # Load Social Media Data from JSON File
    with open(social_media_file, "r") as social_media_raw:
        social_media_data = json.load(social_media_raw)

    # Define Icons for Each Social Media Platform
    platform_icons = {
        "Twitter": "🐦",
        "LinkedIn": "🔗",
        "GitHub": "📥",
        # Add more platforms and corresponding icons as needed
    }

    # Display Social Media Links in Columns with Icons
    if len(social_media_data.get("SOCIAL_MEDIA", {})) > social_media_data.get("MAX_SOCIAL_MEDIA_COLUMNS", 0):
        for row in range((len(social_media_data["SOCIAL_MEDIA"]) // social_media_data["MAX_SOCIAL_MEDIA_COLUMNS"]) + 1):
            cols = st.columns(social_media_data["MAX_SOCIAL_MEDIA_COLUMNS"])
            for index, (platform, link) in enumerate(social_media_data["SOCIAL_MEDIA"].items()):
                if index // social_media_data["MAX_SOCIAL_MEDIA_COLUMNS"] == row:
                    icon = platform_icons.get(platform, "📬")  # Default to a globe emoji if no specific icon
                    cols[index % social_media_data["MAX_SOCIAL_MEDIA_COLUMNS"]].write(f"{icon} [{platform}]({link})")
    else:
        cols = st.columns(len(social_media_data.get("SOCIAL_MEDIA", {})))
        for index, (platform, link) in enumerate(social_media_data["SOCIAL_MEDIA"].items()):
            icon = platform_icons.get(platform, "📬")  # Default to a globe emoji if no specific icon
            cols[index].write(f"{icon} [{platform}]({link})")

    st.write('\n')
    st.write('\n')

# SKILLS SECTION

if sections_data["SKILLS"]:
    st.subheader("📎 Skills")
    with open(skills_file, "r") as skills_raw:
        skills_data = json.load(skills_raw)
    if len(skills_data["SKILLS"]) > skills_data["MAX_SKILLS_COLUMNS"]:
        for row in range((len(skills_data["SKILLS"]) // skills_data["MAX_SKILLS_COLUMNS"]) + 1):
            cols = st.columns(skills_data["MAX_SKILLS_COLUMNS"])
            for index, skill in enumerate(skills_data["SKILLS"]):
                if index // skills_data["MAX_SKILLS_COLUMNS"] == row:
                    cols[index % skills_data["MAX_SKILLS_COLUMNS"]].write(f"🏷️ **{skill}**")
    else:
        cols = st.columns(len(skills_data["SKILLS"]))
        for index, skill in enumerate(skills_data["SKILLS"]):
            cols[index].write(f"🏷️ **{skill}**")
    st.write('\n')
    st.write('\n')

# WORK EXPERIENCE SECTION

# Check if 'EXPERIENCE' key exists in sections_data
if sections_data["WORK_EXPERIENCE"]:
    st.subheader("📎 Work Experience")
    with open(work_experience_file, "r") as work_experience_raw:
        work_experience_data = json.load(work_experience_raw)
    for description in work_experience_data["WORK_EXPERIENCE"]:
        cols = st.columns(3)
        cols[0].write(f"💼 **{description['DESIGNATION']}**")
        cols[1].write(f"⌨️ **{description['COMPANY']}**")
        cols[2].write(f"🕰️ **{description['DURATION']}**")
        for item in description['DETAILS']:
            st.write(f"📌 {item}")
        st.write('\n')
    st.write('\n')
    
# EDUCATION SECTION

if sections_data["EDUCATION"]:
    st.subheader("📎 Education")
    with open(education_file, "r") as education_raw:
        education_data = json.load(education_raw)
    for description in education_data["EDUCATION"]:
        cols = st.columns(3)
        cols[0].write(f"🎓 **{description['COURSE']}**")
        cols[1].write(f"💿 **{description['COLLEGE']}**")
        cols[2].write(f"🕰️ **{description['DURATION']}**")
        for item in description['DETAILS']:
            st.write(f"✒️ {item}")
        st.write('\n')
    st.write('\n')

# PROJECTS SECTION

if sections_data["PROJECTS"]:
    st.subheader("📎 Projects")
    with open(project_file, "r") as project_raw:
        project_data = json.load(project_raw)
    for item in project_data["PROJECTS"]:
        st.write(f"⚡️ {item}")
    st.write('\n')
    st.write('\n')


# CERTIFICATES SECTION

if sections_data["CERTIFICATES"]:
    with open(certificates_file, "r") as certificates_raw:
        certificates_data = json.load(certificates_raw)
    st.subheader("📎 Certificates")
    if len(certificates_data["CERTIFICATES"]) > certificates_data["MAX_CERTIFICATES_COLUMNS"]:
        for row in range((len(certificates_data["CERTIFICATES"]) // certificates_data["MAX_CERTIFICATES_COLUMNS"]) + 1):
            cols = st.columns(certificates_data["MAX_CERTIFICATES_COLUMNS"])
            for index, (certificate, link) in enumerate(certificates_data["CERTIFICATES"].items()):
                if index // certificates_data["MAX_CERTIFICATES_COLUMNS"] == row:
                    cols[index % certificates_data["MAX_CERTIFICATES_COLUMNS"]].write(f"📜 [{certificate}]({link})")
    else:
        cols = st.columns(len(certificates_data["CERTIFICATES"]))
        for index, (certificate, link) in enumerate(certificates_data["CERTIFICATES"].items()):
            cols[index].write(f"📝 [{certificate}]({link})")
    st.write('\n')
    st.write('\n')


# KINDLY SUPPORT THE EFFORTS

st.write('\n')
st.caption('Developed with ❤️ by [SASI](https://www.linkedin.com/in/sasank-sasi-96b34723a/). (https://github.com/sasank-sasi) 🌟.')