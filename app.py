import streamlit as st
from ai_agent_utility import weather_agent


# set page configuration
st.set_page_config(page_title="AI Weather Agent", page_icon="🌤️")

# Title
st.title("🌤️ AI Weather Agent")
st.markdown("Ask me about the weather in any city 🌍")

# input widget to get user query
user_query = st.text_area("Type your question here...", placeholder="e.g. What's the weather in Mumbai?")

if st.button("Get Weather"):
    if not user_query.strip():
        st.warning("⚠️ Please enter a question.")
    else:
        with st.spinner("Fetching weather... ⏳"):
            try:
                response = weather_agent.run_sync(user_prompt=user_query)

                if response and response.output:
                    st.success("✅ Response:")
                    st.markdown(f"**{response.output}**")
                else:
                    st.error("❌ No response received. Try again.")
            except Exception as e:
                st.error(f"🚨 Error: {str(e)}")