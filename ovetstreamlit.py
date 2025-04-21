import streamlit as st

# ------------------ Hardcoded Lists ------------------
health_issues = [
    "Diabetes",
    "Hypothyroidism",
    "Hyperthyroidism",
    "Cushings Syndrome",
    "Addisons Disease",
    "Hyperlipidemia",
    "Obesity",
    "Underweight",
    "Adrenal Disorders",
    "Hyperglycemia",
    "Pancreatitis",
    "Inflammatory Bowel Disease",
    "Gastroenteritis",
    "Food Sensitivity",
    "Diarrhea",
    "Constipation",
    "Hairballs",
    "Protein Losing Enteropathy",
    "Megaesophagus",
    "Hepatic Lipidosis",
    "Lymphangiectasia",
    "Hepatitis",
    "Dehydration",
    "Gallbladder Disease",
    "Kindney Disease",
    "Feline Luts",
    "Urinary Tract Infection",
    "Bladder Stones",
    "Proteinuria",
    "Urinary Problems",
    "Struvite",
    "Oxalate Stones",
    "Atopic Dermatitis",
    "Flea Allergy Dermatitis",
    "Skin Rash",
    "Hot Spots",
    "Ear Infections",
    "Ringworm",
    "Heart Murmur",
    "Hypertrophic Cardiomypathy",
    "Mitral Valve Disease",
    "Congestive Heart Failure",
    "Hypertenstion (High Blood Pressure)",
    "Lymphoma",
    "Mast Cell Tumor",
    "Osteosarcoma",
    "Osteoarthritis",
    "Hip Dysplasia",
    "Intervertebral Disc Disease",
    "Cruiciate Ligament Tear",
    "Arthritis",
    "Epilepsy",
    "Cognitive Dysfunction",
    "Vestibular Disease",
    "Degenerative Myelopathy",
    "Mental Health Disorder",
    "Seizure",
    "Anxiety",
    "Feline Asthma",
    "Canine Parvovirus",
    "Brachycephalic Syndrome",
    "Aging",
    "Surgery",
    "Vision Problem",
    "Dental Issue",
    "Periodontal Disease",
    "Inflammatory Mediators",
    "Catabolic States",
    "Debilitation",
    "Autoimmune Diseases",
    "Chronic Infections",
    "Weak Immunity",
]

dog_breeds = sorted([
    "Beagle", "Boxer", "Bulldog", "Dachshund", "German Shepherd",
    "Golden Retriever", "Labrador Retriever", "Poodle", "Shih Tzu", "Yorkshire Terrier"
])

cat_breeds = sorted([
    "Domestic Shorthair", "American Shorthair", "Domestic Longhair", "Ragdoll",
    "Siamese", "Bengal", "Maine Coon", "British Shorthair", "Persian", "Russian Blue",
    "Sphynx", "Scottish Fold", "Exotic Shorthair", "Oriental Shorthair", "Burmese",
    "Devon Rex", "Himalayan", "Abyssinian", "Birman", "Norwegian Forest Cat"
])

allergy_list = sorted([
    "Barley", "Beef", "Carrot", "Chicken", "Corn", "Dairy", "Duck", "Egg", "Fish", "Flaxseed",
    "Lamb", "Oat", "Pea", "Pork", "Potato", "Pumpkin", "Rice", "Salmon", "Soy", "Sweet Potato",
    "Tomato", "Turkey", "Wheat", "Brown Rice", "Coconut", "Chickpea", "Fava Beans", "Quinoa", "Sorghum", "Tapioca",
    "Black Beans", "Broccoli", "Algae", "Millet", "Venison", "Kangaroo", "Duck Liver", "Liver",
    "Rabbit", "Spinach", "Milk"
])

activity_levels = ["Active", "Not Active"]
life_stages = ["Growth", "Adult", "Senior"]

# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="Pet Nutrition Recommender", layout="centered")
st.title("🐾 Pet Nutrition Recommendation Tool")

# Custom CSS for scrollbar and error styling
st.markdown("""
    <style>
    /* Global vertical scrollbar styling for page */
    html, body {
        overflow-y: scroll;
    }
    /* Wider scrollbar track and thumb */
    ::-webkit-scrollbar {
        width: 16px;
    }
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    ::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 8px;
        border: 3px solid #f1f1f1;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #555;
    }

    /* Alert box styling for Streamlit errors */
    div[role="alert"] {
        background-color: #ffe6e6 !important;
        border-left: 4px solid #ff4d4d !important;
        padding: 12px 16px !important;
        margin-bottom: 8px !important;
        border-radius: 4px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    /* Error message text color */
    div[role="alert"] p {
        color: #800000 !important;
        margin: 0;
    }
    </style>
""", unsafe_allow_html=True)

# Required fields note
st.markdown("**Fields marked with * are required**")

gender = st.radio("Gender *", ["Male", "Female"], index=None, key="gender")

# Species *
species = st.selectbox("Species *", ["-- Select Species --", "Dog", "Cat"], key="species")
# Breed *
breed_list = dog_breeds if species == "Dog" else (cat_breeds if species == "Cat" else [])
breed = st.selectbox("Breed *", ["-- Select Breed --"] + breed_list, key="breed") if breed_list else None

# Breed Size *, Life Stage *, Activity Level *
breed_size = st.selectbox("Breed Size *", ["-- Select Breed Size --", "Small", "Medium", "Large"], key="breed_size")
life_stage = st.selectbox("Life Stage *", ["-- Select Life Stage --"] + life_stages, key="life_stage")
activity_level = st.selectbox("Activity Level *", ["-- Select Activity Level --"] + activity_levels, key="activity_level")

# Weight, Age, Body Score
weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1, key="weight")
age = st.number_input("Age (months)", min_value=0, step=1, key="age")
body_score = st.slider("Body Score (1-9)", min_value=1, max_value=9, key="body_score")

st.markdown("---")

# --- Health Conditions (dynamic filtering) ---
st.subheader("Health Conditions")
# Main Health Issue *
main_issue = st.selectbox(
    "Main Health Issue *",
    ["-- None --"] + health_issues,
    key="main_issue"
)
# Other Health Issue 1 (exclude main)
other_opts1 = [h for h in health_issues if h != main_issue]
other_issue_1 = st.selectbox(
    "Other Health Issue 1",
    ["-- None --"] + other_opts1,
    key="other_issue_1"
)
# Other Health Issue 2 (exclude main and issue 1)
other_opts2 = [h for h in health_issues if h not in {main_issue, other_issue_1}]
other_issue_2 = st.selectbox(
    "Other Health Issue 2",
    ["-- None --"] + other_opts2,
    key="other_issue_2"
)

st.markdown("---")

# Allergies *
has_allergy = st.radio("Allergies *", ["Yes", "No"], index=None, key="has_allergy")
selected_allergies = st.multiselect("Select Allergies", allergy_list, key="allergies") if has_allergy == "Yes" else []

# Pregnancy/Lactation (Female only)
if gender == "Female":
    pregnant = st.radio("Pregnant *", ["Yes", "No"], index=None, key="pregnant")
    lactating = st.radio("Lactating *", ["Yes", "No"], index=None, key="lactating")
else:
    pregnant = None
    lactating = None

st.markdown("---")

# Submit button
if st.button("Get Recommendations"):
    errors = []
    # Validate required fields
    if species.startswith("--"): errors.append("Species is required.")
    if breed is None or breed.startswith("--"): errors.append("Breed is required.")
    if breed_size.startswith("--"): errors.append("Breed size is required.")
    if life_stage.startswith("--"): errors.append("Life stage is required.")
    if activity_level.startswith("--"): errors.append("Activity level is required.")
    if main_issue.startswith("--"): errors.append("Main health issue is required.")
    # Enforce uniqueness
    if other_issue_1 != "-- None --" and other_issue_1 == main_issue:
        errors.append("Other Health Issue 1 cannot equal the main issue.")
    if other_issue_2 != "-- None --" and (other_issue_2 == main_issue or other_issue_2 == other_issue_1):
        errors.append("Other Health Issue 2 must be different from main and issue 1.")
    if has_allergy == "Yes" and not selected_allergies:
        errors.append("At least one allergy must be selected.")

    if errors:
        for e in errors:
            st.error(e)
    else:
        st.markdown("### 🍽️ Recommended Foods:")
        for food in [
            "Hill's Metabolic + Mobility",
            "Royal Canin Hypoallergenic",
            "Rayne Clinical Nutrition RSS",
        ]:
            st.write(f"- {food}")
