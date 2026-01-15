import streamlit as st


def main():
    st.title("Rule based smart home air conditioner controller")


    facts = {
        "temp": 22,
        "humidity": 46,
        "occupancy": "OCCUPIED",
        "time": "NIGHT",
        "windows_open": False
    }

    # Rule Logic 
    if facts["windows_open"]:
        result = "OFF | Reason: Windows are open (100)"
    elif facts["temp"] <= 22:
        result = "OFF | Reason: Too cold (85)"
    elif facts["occupancy"] == "EMPTY":
        result = "ECO | Reason: No one home (90)"
    else:
        result = "COOL | Reason: Standard Cooling"

    st.write(f"**Current Status:** {facts}")
    st.success(f"**Action:** {result}")

if __name__ == "__main__":
    main()