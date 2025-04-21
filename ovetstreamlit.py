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

# Required Fields Indicator
st.markdown("**Fields marked with * are required**")

# Gender *
gender = st.radio("Gender *", options=["Male", "Female"], index=None, key="gender")

# Species * & Breed *
species = st.selectbox("Species *", ["None", "Dog", "Cat"], key="species")
breed_list = dog_breeds if species == "Dog" else (cat_breeds if species == "Cat" else [])
breed = st.selectbox("Breed *", ["None"] + breed_list, key="breed") if breed_list else None

st.markdown("---")

with st.form("pet_form"):
    # Breed Size *, Life Stage *, Activity Level *
    breed_size = st.selectbox("Breed Size *", ["None", "Small", "Medium", "Large"], key="breed_size")
    life_stage = st.selectbox("Life Stage *", ["None"] + life_stages, key="life_stage")
    activity_level = st.selectbox("Activity Level *", ["None"] + activity_levels, key="activity_level")

    weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1, value=0.0, key="weight")
    age = st.number_input("Age (months)", min_value=0, step=1, value=0, key="age")
    body_score = st.slider("Body Score (1-9)", min_value=1, max_value=9, step=1, key="body_score")

    # Health Conditions
    st.subheader("Health Conditions")
    main_issue = st.selectbox("Main Health Issue *", ["None"] + health_issues, key="main_issue")
    # build options excluding main
    other_opts = [issue for issue in health_issues if issue != main_issue]
    col1, col2 = st.columns(2)
    with col1:
        other_issue_1 = st.selectbox("Other Health Issue 1", ["None"] + other_opts, key="other_issue_1")
    # exclude main and other1
    other_opts2 = [issue for issue in health_issues if issue not in {main_issue, other_issue_1}]
    with col2:
        other_issue_2 = st.selectbox("Other Health Issue 2", ["None"] + other_opts2, key="other_issue_2")

    # Allergies
    has_allergy = st.radio("Allergies *", options=["Yes", "No"], index=None, key="has_allergy")
    selected_allergies = []
    if has_allergy == "Yes":
        selected_allergies = st.multiselect("Select Allergies", allergy_list, key="allergies")

    # Pregnancy / Lactation (only for Female)
    if gender == "Female":
        pregnant = st.radio("Pregnant *", options=["Yes", "No"], index=None, key="pregnant")
        lactating = st.radio("Lactating *", options=["Yes", "No"], index=None, key="lactating")
    else:
        pregnant = None
        lactating = None

    submit = st.form_submit_button("Get Recommendations")

if submit:
    errors = []
    # Validations for required
    if species == "None":
        errors.append("Species is required.")
    if breed == "None":
        errors.append("Breed is required.")
    if breed_size == "None":
        errors.append("Breed size is required.")
    if life_stage == "None":
        errors.append("Life stage is required.")
    if activity_level == "None":
        errors.append("Activity level is required.")
    if main_issue == "None":
        errors.append("Main health issue is required.")
    # enforce uniqueness
    if other_issue_1 != "None" and other_issue_1 == main_issue:
        errors.append("Other Health Issue 1 cannot match the main health issue.")
    if other_issue_2 != "None" and other_issue_2 == main_issue:
        errors.append("Other Health Issue 2 cannot match the main health issue.")
    if other_issue_1 != "None" and other_issue_2 != "None" and other_issue_1 == other_issue_2:
        errors.append("Other health issues must be different from each other.")

    if not selected_allergies and has_allergy == "Yes":
        errors.append("At least one allergy must be selected or choose 'No'.")

    if errors:
        for err in errors:
            st.error(err)
    else:
        user_input = {
            "gender": gender,
            "species": species,
            "breed": breed,
            "breed_size": breed_size,
            "life_stage": life_stage,
            "activity_level": activity_level,
            "weight": weight,
            "age": age,
            "body_score": body_score,
            "main_issue": main_issue,
            "other_issues": [oi for oi in [other_issue_1, other_issue_2] if oi != "None"],
            "allergies": selected_allergies,
            "pregnant": pregnant,
            "lactating": lactating,
        }
        st.markdown("### 🍽️ Recommended Foods:")
        for food in [
            "Hill's Metabolic + Mobility",
            "Royal Canin Hypoallergenic",
            "Rayne Clinical Nutrition RSS",
        ]:
            st.write(f"- {food}")
