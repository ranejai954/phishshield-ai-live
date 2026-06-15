import streamlit as st
from datetime import datetime

from ai.groq_engine import analyze_phishing
from reports.pdf_generator import generate_pdf

st.set_page_config(
    page_title="PhishShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ PhishShield AI")

st.subheader(
    "AI-Powered Phishing Detection & Threat Analysis"
)

st.markdown("""
Analyze suspicious emails, SMS messages, and phishing attempts using AI.
""")

st.markdown("---")

message = st.text_area(
    "Paste suspicious email, SMS, or message:"
)

if st.button("Analyze"):

    if message.strip():

        with st.spinner("Analyzing..."):

            result = analyze_phishing(message)

        analysis_id = (
            "PH-" +
            datetime.now().strftime("%Y%m%d%H%M%S")
        )

        pdf_filename = (
            f"{analysis_id}.pdf"
        )

        generate_pdf(
            filename=pdf_filename,
            analysis_id=analysis_id,
            risk_score=result["risk_score"],
            threat_level=result["threat_level"],
            explanation=result["explanation"],
            recommendations=", ".join(
                result["recommendations"]
            )
        )

        st.success("Analysis Complete")

        st.metric(
            "Risk Score",
            f"{result['risk_score']}%"
        )

        if result["threat_level"] == "CRITICAL":

            st.error(
                f"Threat Level: {result['threat_level']}"
            )

        elif result["threat_level"] == "HIGH":

            st.warning(
                f"Threat Level: {result['threat_level']}"
            )

        else:

            st.info(
                f"Threat Level: {result['threat_level']}"
            )

        st.write("### Indicators")

        for indicator in result["indicators"]:
            st.write(f"• {indicator}")

        st.write("### Explanation")
        st.write(result["explanation"])

        st.write("### Recommendations")

        for recommendation in result["recommendations"]:
            st.write(f"• {recommendation}")

        with open(pdf_filename, "rb") as pdf_file:

            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_file,
                file_name=pdf_filename,
                mime="application/pdf"
            )

    else:

        st.warning(
            "Please enter a message."
        )