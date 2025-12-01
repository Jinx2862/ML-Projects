import streamlit as st
import pickle

# Load the pre-trained machine learning model
try:
    with open('kmeans.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Error: Model file 'kmeans.pkl' not found.")
    st.stop()

# Mapping for Education
education_mapping = {'Undergraduate': 0, 'Graduate': 1, 'Postgraduate': 2}

# Mapping for Living With
living_with_mapping = {'Alone': 0, 'Partner': 1}

st.set_page_config(
    page_title="Customer Segmentation Prediction",
    page_icon=":bar_chart:",
    layout="wide",  # Wide layout for better spacing
    initial_sidebar_state="expanded",  # Expanded sidebar by default
)
custom_css = """
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #ffffff;
    }
    .st-dcuhf.st-dcvKpV.st-dcuhf.st-cUjEP.st-ekZUXy.st-elOvoR.st-dcuhf.st-dcvKpV.st-dcuhf.st-dcvKpV {
        color: yellow !important;  
   }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Define the main function for the Streamlit app
def main():
    
    st.title('Customer Segmentation Prediction')
    st.header('Enter Customer Features')
    # Input form for user to enter features
    col1, col2 = st.columns(2)

    with col1:
        education = st.selectbox('Education', list(education_mapping.keys()), key='education_selectbox')

    with col2:
        living_with = st.selectbox('Living With', list(living_with_mapping.keys()), key='living_with_selectbox')
    income = st.number_input('Income', value=0.0)
    amount_spent = st.number_input('Amount Spent', value=0.0)
    children = st.number_input('Children', value=0)
    family_size = st.number_input('Family Size', value=1)
    customer_age = st.number_input('Customer Age', value=0)
    total_purchases = st.number_input('Total Purchases', value=0)
    total_accepted_cmp = st.number_input('Total Accepted Cmp', value=0)

    # Convert selected category names to integer labels
    education_label = education_mapping.get(education, -1)
    living_with_label = living_with_mapping.get(living_with, -1)

    # Predict button to trigger prediction
    if st.button('Predict'):
        # Perform prediction using the loaded model
        features = [education_label, income, amount_spent, living_with_label, children, family_size, customer_age, total_purchases, total_accepted_cmp]
        prediction = model.predict([features])[0]

        # Display prediction result
        st.header('Prediction Result')
        if prediction == 1:
            st.write("Customers comes under Cluster 1, have the following attributes:")
            st.write("- Higher income")
            st.write("- Higher amount spent")
            st.write("- Single or parent of less than 3 kids")
            st.write("- Higher amount of purchases")
            
        elif prediction == 0:
            st.write("Customer comes under Cluster 0, have the following attributes:")
            st.write("- Lower income")
            st.write("- Lower amount spent")
            st.write("- Married and parent of more than 3 kids")
            st.write("- Lower amount of purchases")

if __name__ == '__main__':
    main()
