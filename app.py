import streamlit as st

# 🌟 Set page title
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# 🎨 Stylish Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌟 Unit Converter 🌟</h1>", unsafe_allow_html=True)

# 📌 User selects conversion type
conversion_type = st.selectbox(
    "Choose a conversion type:",
    ["Length", "Temperature", "Weight", "Speed", "Time"]
)

# 📏 Length conversion
if conversion_type == "Length":
    st.subheader("📏 Length Converter")
    length = st.number_input("Enter length in meters:", min_value=0.0, format="%.2f")
    length_choice = st.radio("Convert to:", ["Kilometers", "Feet", "Miles"])

    if length_choice == "Kilometers":
        result = length / 1000
        st.success(f"✅ {length} meters = {result} kilometers")
    elif length_choice == "Feet":
        result = length * 3.28084
        st.success(f"✅ {length} meters = {result} feet")
    else:  # Miles
        result = length * 0.000621371
        st.success(f"✅ {length} meters = {result} miles")

# 🌡 Temperature conversion
elif conversion_type == "Temperature":
    st.subheader("🌡 Temperature Converter")
    temp = st.number_input("Enter temperature in Celsius:", format="%.2f")
    temp_choice = st.radio("Convert to:", ["Fahrenheit", "Kelvin"])

    if temp_choice == "Fahrenheit":
        result = (temp * 9/5) + 32
        st.info(f"ℹ️ {temp}°C = {result}°F")
    else:  # Kelvin
        result = temp + 273.15
        st.info(f"ℹ️ {temp}°C = {result} K")

# ⚖️ Weight conversion
elif conversion_type == "Weight":
    st.subheader("⚖️ Weight Converter")
    weight = st.number_input("Enter weight in kilograms:", min_value=0.0, format="%.2f")
    weight_choice = st.radio("Convert to:", ["Grams", "Pounds"])

    if weight_choice == "Grams":
        result = weight * 1000
        st.warning(f"⚠️ {weight} kg = {result} grams")
    else:  # Pounds
        result = weight * 2.20462
        st.warning(f"⚠️ {weight} kg = {result} pounds")

# 🚗 Speed conversion
elif conversion_type == "Speed":
    st.subheader("🚗 Speed Converter")
    speed = st.number_input("Enter speed in km/h:", min_value=0.0, format="%.2f")
    speed_choice = st.radio("Convert to:", ["Meters per second", "Miles per hour"])

    if speed_choice == "Meters per second":
        result = speed / 3.6
        st.success(f"✅ {speed} km/h = {result} m/s")
    else:  # Miles per hour
        result = speed * 0.621371
        st.success(f"✅ {speed} km/h = {result} mph")

# ⏳ Time conversion
elif conversion_type == "Time":
    st.subheader("⏳ Time Converter")
    time = st.number_input("Enter time in minutes:", min_value=0.0, format="%.2f")
    time_choice = st.radio("Convert to:", ["Seconds", "Hours"])

    if time_choice == "Seconds":
        result = time * 60
        st.info(f"ℹ️ {time} minutes = {result} seconds")
    else:  # Hours
        result = time / 60
        st.info(f"ℹ️ {time} minutes = {result} hours")

# 🎨 Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>🚀 Built with ❤️ by Sadia</h4>", unsafe_allow_html=True)
