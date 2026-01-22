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
st.caption("A curated collection of applied GenAI products - built end-to-end, deployed, and production-minded.")

st.divider()

apps = [
    {
        "title": "🎨 AI Story Generator",
        "description": (
            "A multimodal generative storytelling system that transforms user-uploaded images into "
            "coherent, genre-aware short stories. The app intelligently evaluates user intent, grounds "
            "the narrative in visual context using Gemini Vision, and produces expressive voice narration "
            "using a local neural TTS pipeline. Designed with robustness, state management, and deployment "
            "constraints in mind."
        ),
        "tags": ["Multimodal", "Gemini Vision", "Prompt Evaluation", "Neural TTS", "Streamlit"],
        "link": "https://ai-story-generator-samyak.streamlit.app/"
    },
    {
        "title": "🧠 AI Daily Briefing Agent",
        "description": (
            "An agentic AI assistant that reasons over real-time tools to generate a fully actionable daily plan. "
            "It dynamically retrieves live weather data, top news headlines, and verified local events, then "
            "synthesizes them into a structured, time-aware schedule. Built with strict constraints to avoid "
            "hallucinations, vague recommendations, or fabricated venues - prioritizing correctness over fluff."
        ),
        "tags": ["Agentic AI", "Tool Use", "LangChain", "Real-time APIs", "Planning"],
        "link": "https://ai-assistant-samyak-jain.streamlit.app/"
    },
    {
        "title": "🔮 Upcoming AI Project",
        "description": (
            "A forthcoming AI application exploring deeper reasoning, personalization, or automation. "
            "This project will continue the theme of building production-ready GenAI systems with a strong "
            "emphasis on real-world utility, evaluation, and system design. Stay tuned."
        ),
        "tags": ["Coming Soon", "Advanced Reasoning", "Applied AI"],
        "link": "#"
    }
]

cols = st.columns(3)

for col, app in zip(cols, apps):
    with col:
        st.markdown(f"### {app['title']}")

        tags_html = "".join(
            [f"<span class='tag'>{tag}</span>" for tag in app["tags"]]
        )
        st.markdown(f"<div>{tags_html}</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"<p>{app['description']}</p>", unsafe_allow_html=True)
        st.markdown(f"🔗 <a href='{app['link']}' target='_blank'>View App</a>", unsafe_allow_html=True)


st.divider()

st.markdown(
    "**About the developer**  \n"
    "I design and build applied AI systems that go beyond demos - focusing on grounding, evaluation, "
    "tool-augmented reasoning, and deployment-ready engineering. These projects reflect my interest in "
    "production-grade Data Science, GenAI, multimodal systems, and agentic workflows."
)
