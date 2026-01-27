import streamlit as st

st.set_page_config(page_title="Samyak Jain | AI Systems Showcase", layout="wide")

st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.card {
    background-color: #161b22;
    padding: 1.5rem;
    border-radius: 14px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.25);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    height: 100%;
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}
.card h3 {
    margin-top: 0;
}
.card a {
    text-decoration: none;
    color: #4da3ff;
    font-weight: 600;
}
.tag {
    display: inline-block;
    background: #21262d;
    color: #9da7b3;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 0.75rem;
    margin-right: 6px;
    margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 AI Systems Showcase")
st.caption(
    "A curated collection of applied GenAI systems — built end-to-end, deployed, and engineered with production constraints in mind."
)

st.divider()

apps = [
    {
        "title": "🎨 AI Story Generator",
        "description": (
            "A multimodal generative storytelling system that transforms user-uploaded images into "
            "coherent, genre-aware short stories using Groq-hosted multimodal LLMs. "
            "The system evaluates user intent, grounds narratives in visual context, and produces "
            "expressive audio narration via a fully offline neural TTS pipeline. "
            "Designed with careful state management, robustness, and free-tier deployment constraints."
        ),
        "tags": ["Multimodal", "Groq", "Vision-Language", "Prompt Evaluation", "Offline Neural TTS"],
        "link": "https://ai-story-generator-samyak.streamlit.app/"
    },
    {
        "title": "🧠 AI Daily Briefing Agent",
        "description": (
            "An agentic AI assistant that reasons over real-time tools to generate a complete, "
            "actionable daily plan. Powered by Groq (LLaMA 3.3 70B) and LangChain Agents, "
            "it dynamically retrieves live weather, recent news, and verified local events, "
            "then synthesizes them into a structured schedule while strictly avoiding hallucinations "
            "or vague recommendations."
        ),
        "tags": ["Agentic AI", "Groq", "LangChain Agents", "Tool Use", "Real-time APIs"],
        "link": "https://ai-assistant-samyak-jain.streamlit.app/"
    }
]

cols = st.columns(2)

for col, app in zip(cols, apps):
    with col:
        st.markdown(f"### {app['title']}")

        tags_html = "".join(
            [f"<span class='tag'>{tag}</span>" for tag in app["tags"]]
        )
        st.markdown(f"<div>{tags_html}</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"<p>{app['description']}</p>", unsafe_allow_html=True)
        st.markdown(
            f"🔗 <a href='{app['link']}' target='_blank'>View App</a>",
            unsafe_allow_html=True
        )

st.divider()

st.markdown(
    "About the developer  \n"
    "I design and build applied AI systems that go beyond demos — focusing on grounding, "
    "agentic reasoning, multimodal understanding, and deployment-ready engineering. "
    "These projects reflect my interest in production-grade Data Science, Generative AI, "
    "and real-world system design."
)