import streamlit as st
from PIL import Image
import random
import requests
from io import BytesIO

# Function to set the background color
def set_background():
    st.markdown(
        """
        <style>
        body {
            background-color: #f5f5f5; /* Light gray */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# Introduction Section
def introduction():
    st.title("🌍 Global Plastic Waste Overview")
    st.markdown("""
## 🌍 Understanding Plastic Waste

Plastic waste refers to discarded plastic materials that persist in the environment for centuries due to their **non-biodegradable** nature. These range from everyday items like **plastic bags and bottles** to **microplastics**—tiny fragments resulting from the breakdown of larger plastics.

### 🔥 Key Impacts of Plastic Waste:

- **🌊 Environmental Pollution:**  
  Plastics account for **14% of the solid waste stream** in regions like New York State, highlighting their widespread presence and persistence.  

- **⚠️ Human Health Risks:**  
  Microplastics have been found in **food, water, and household items**, raising concerns about potential links to **cancer and dementia**.

- **💰 Economic Costs:**  
  Pollution threatens industries like **tourism and fishing**, leading to declining fish populations and damaged coastal economies.

- **🌡️ Climate Change Contribution:**  
  Plastic production and degradation release **greenhouse gases**, accelerating **global warming** and extreme weather events.

### 🚨 The Urgent Need for Action:

- Only **5-6% of plastic waste** is currently recycled in the United States.
- If current trends persist, **plastic pollution is projected to triple by 2060**.
  
🔎 **The solution?** A **global commitment** to sustainable practices, innovative solutions, and responsible waste management. The future of our planet depends on it!
""")


def visual_content():
    st.title("📸 Visual Impact of Plastic Waste")
    st.markdown("Explore images showcasing the effects of plastic waste on our environment.")

    # List of Google Drive image links 
    image_links = [
        "https://drive.google.com/uc?export=view&id=1RoZh_9D88BQ-MKafHKkLwVagF5N48Om2",
        "https://drive.google.com/uc?export=view&id=1L2fVVQdZ5j54L6qwr0kU78kARnKNG0bT",
        "https://drive.google.com/uc?export=view&id=1SgBixQ1l3h0VmAcB-InzoZDcTtz1GgzY"
    ]   

    # Display images from Google Drive
    for img_url in image_links:
        response = requests.get(img_url)
        
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            st.image(image, use_container_width=True)
        else:
            st.error(f"Failed to load image: {img_url}")


def fetch_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except Exception as e:
        st.error(f"Failed to load image: {e}")
        return None

def inspiring_stories():
    st.title("🌟 Inspiring Stories of Plastic Waste Reduction")

    stories = {
        "Seven Clean Seas": {
            "image": "https://drive.google.com/uc?export=view&id=1GVt3WuKzUrkQxsxDU6IaR7m0125pqQWC",
            "text": (
                "Seven Clean Seas is an ocean impact organization founded in 2018 by Tom Peacock-Nazil, dedicated to combating marine plastic pollution. "
                "Their ambitious mission is to remove 10 million kilograms of plastic from the oceans by the end of 2025.\n\n"
                "As of now, they have successfully extracted over 4.9 million kilograms of plastic waste from marine environments, creating 91 formal jobs in the process.\n\n"
                "### Impact and Achievements:\n"
                "- **Plastic Removal:** Successfully extracted over 4.9 million kilograms of plastic waste from marine environments. \n"
                "- **Job Creation:** Created 91 formal jobs as collection crew members, contributing to local economies.\n"
                "- **Innovative Projects:** Implemented the HIPPO project in Thailand, aiming to remove up to 1.4 million kilograms of plastic from the Chao Phraya River annually.\n\n"
                "[Learn More](https://www.sevencleanseas.com/)"
            )
        },
        "Founders of Bye Bye Plastic Bags": {
            "image": "https://drive.google.com/uc?export=view&id=1FHojwHI-sfNSKeRYRffQxHBkh406bzfo",
            "text": (
            "**Bye Bye Plastic Bags (BBPB)** is a youth-driven organization founded in 2013 by Indonesian sisters Melati and Isabel Wijsen, "
            "who were just 12 and 10 years old at the time, aiming to reduce plastic waste in Bali.\n\n"
            "### Impact and Achievements:\n"
            "- **Policy Change:** BBPB's advocacy led to Bali's 2018 ban on single-use plastic bags, straws, and Styrofoam, significantly reducing plastic waste on the island.\n"
            "- **Global Expansion:** The initiative has expanded to over 60 locations worldwide, empowering youth to lead plastic waste reduction campaigns in their communities.\n"
            "- **Educational Outreach:** BBPB conducts workshops and educational programs to raise awareness about plastic pollution, fostering a generation of environmentally conscious individuals.\n\n"
            "[Learn More](https://www.byebyeplasticbags.org/)"
        )
    },
    "Break Free From Plastic Movement": {
        "image": "https://drive.google.com/uc?export=view&id=1nj3HqG4x8lHWVDofzKSuk9da-cB_07YX",
        "text": (
            "Launched in 2016, the **Break Free From Plastic (BFFP)** movement is a global coalition of over 13,000 organizations and individual supporters "
            "united in their vision for a future free from plastic pollution.\n\n"
            "### Impact and Achievements:\n"
            "- **Global Advocacy:** BFFP has been instrumental in pushing for international policies aimed at reducing plastic production and consumption. "
            "A 2024 survey across ten countries revealed that 84% of respondents support cuts to plastic production, underscoring global backing for BFFP's initiatives.\n"
            "- **Corporate Accountability:** The movement actively campaigns against major polluters, holding corporations accountable for their roles in plastic pollution. "
            "Their annual Brand Audit reports have identified top plastic polluters, pressuring companies to adopt sustainable practices.\n"
            "- **Community Engagement:** BFFP supports local communities in combating plastic pollution through education, clean-up drives, and policy advocacy, "
            "fostering a global network of informed and active citizens.\n\n"
            "[Learn More](https://www.breakfreefromplastic.org/)"
            )
        }
    }

    tabs = st.tabs(list(stories.keys()))

    # Loop through each story and display content
    for tab, (title, content) in zip(tabs, stories.items()):
        with tab:
            img = fetch_image(content["image"])  # Fetch image using requests
            if img:
                st.image(img, use_container_width=True)  # Display image
            else:
                st.error("Image could not be loaded.")

            st.markdown(content["text"], unsafe_allow_html=True)


# Reycling ideas
def recycling_ideas():
    st.title("♻️ Innovative Plastic Recycling Ideas")
    st.markdown("Explore practical and creative ways to reduce plastic waste—from simple household tips to artistic upcycling and community initiatives.")

    ideas = {
        "Household Recycling & Upcycling 🏠": (
            "- **Home Recycling Station:** Set up designated bins for plastics, paper, and organic waste with clear labels.\n"
            "- **Repurpose Containers:** Use cleaned plastic containers for storage, DIY planters, or organizing craft materials.\n"
            "- **Avoid Single-Use Plastics:** Opt for reusable bags, water bottles, and food containers to reduce waste at the source."
        ),
        "Creative Art & DIY Projects 🎨": (
            "- **Plastic Sculptures:** Transform discarded plastic into captivating sculptures or decorative installations.\n"
            "- **DIY Wall Art:** Create mosaic art or collages using pieces of plastic waste, adding a creative touch to your space.\n"
            "- **Upcycled Crafts:** Experiment with art projects that reuse plastic, inspiring creativity while cutting down on waste."
        ),
        "Fashion & Accessories Upcycling 👗": (
            "- **Eco-Friendly Accessories:** Craft jewelry, bags, or other accessories from recycled plastics.\n"
            "- **DIY Footwear:** Explore tutorials to create simple, stylish shoes or sandals from repurposed plastic materials."
        ),
        "DIY Building Projects 🧱": (
            "- **Create Ecobricks:** Fill used plastic bottles with clean, dry plastic to create durable building blocks.\n"
            "- **Build Furniture:** Use ecobricks or other recycled materials to construct small furniture pieces like benches or planters."
        ),
        "Community & Environmental Action 🌍": (
            "- **Join Local Clean-Ups:** Participate in community events to collect and recycle plastic waste.\n"
            "- **Educate and Advocate:** Share recycling tips with neighbors and support local sustainability initiatives.\n"
            "- **Support Recycled Products:** Choose items made from recycled materials to promote a circular economy."
        )
    }

    for title, description in ideas.items():
        with st.expander(title):
            st.markdown(description)
    
    st.markdown("By integrating these practices into your daily routine, you can help reduce plastic waste and support a healthier environment for all.")

# Main function to run the app
def storytelling_app():
    st.sidebar.title("Navigation")
    options = ["Introduction", "Visual Content", "Inspiring Stories", "Recycling_Ideas"]
    choice = st.sidebar.radio("Go to", options)
    
    if choice == "Introduction":
        introduction()
    elif choice == "Visual Content":
        visual_content()
    elif choice == "Inspiring Stories":
        inspiring_stories()
    elif choice == "Recycling_Ideas":
        recycling_ideas()

if __name__ == "__main__":
    storytelling_app()