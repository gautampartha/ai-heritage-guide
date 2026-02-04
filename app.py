import streamlit as st

# -------------------------------
# Local Monument Knowledge Base
# -------------------------------
MONUMENT_DATA = {
    "Taj Mahal": {
        "info": "The Taj Mahal is an ivory-white marble mausoleum located in Agra, India. It was built by Mughal emperor Shah Jahan in memory of his wife Mumtaz Mahal and is a UNESCO World Heritage Site.",
        "status": "The monument is well-maintained but faces threats from air pollution, marble discoloration, and overcrowding due to tourism."
    },
    "Qutub Minar": {
        "info": "Qutub Minar is a UNESCO World Heritage Site in Delhi and the tallest brick minaret in the world, built in the early 13th century.",
        "status": "The monument is structurally stable with restricted public access to upper levels for safety."
    },
    "Red Fort": {
        "info": "The Red Fort is a historic fortification in Delhi built by Mughal emperor Shah Jahan and served as the main residence of Mughal emperors.",
        "status": "The monument is preserved with continuous restoration and security monitoring."
    },
    "India Gate": {
        "info": "India Gate is a war memorial in New Delhi dedicated to Indian soldiers who died during World War I.",
        "status": "The monument is well-preserved and regularly maintained."
    },
    "Gateway of India": {
        "info": "The Gateway of India is an arch monument built during the 20th century in Mumbai to commemorate the landing of King George V.",
        "status": "The monument is structurally sound but affected by coastal weathering."
    }
}

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🏛️ AI Heritage Guide")
st.write("Upload an image of a monument to explore its history, sustainability insights, and current condition.")

uploaded_image = st.file_uploader(
    "Upload a monument image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    st.success("Image uploaded successfully!")

    # -------------------------------
    # Monument Identification (MVP)
    # -------------------------------
    st.subheader("🧠 Monument Identification (MVP)")

    possible_monuments = list(MONUMENT_DATA.keys())

    monument_name = st.selectbox(
        "AI-suggested monuments (select one):",
        options=possible_monuments
    )

    # -------------------------------
    # Monument Information
    # -------------------------------
    st.subheader("📜 Monument Information")

    if monument_name in MONUMENT_DATA:
        st.write(MONUMENT_DATA[monument_name]["info"])
    else:
        st.warning("Monument information not available in the MVP database.")

    # -------------------------------
    # Sustainability Insights
    # -------------------------------
    st.subheader("🌱 Sustainability & Preservation Insights")

    sustainability_points = [
        "Limit daily tourist footfall to reduce structural stress.",
        "Promote eco-friendly transport near the monument.",
        "Use non-invasive restoration techniques.",
        "Educate visitors about heritage conservation.",
        "Involve local communities in preservation efforts."
    ]

    for point in sustainability_points:
        st.write("•", point)

    # -------------------------------
    # Current Status / Damage
    # -------------------------------
    st.subheader("⚠️ Current Status / Preservation Condition")

    if monument_name in MONUMENT_DATA:
        st.write(MONUMENT_DATA[monument_name]["status"])
    else:
        st.write("Status information not available.")