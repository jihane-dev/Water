from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# === Directories and file paths ===
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "water.json"

# === Load Lottie animation ===
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# === Water animation effect ===
def run_water_animation():
    rain(emoji="💧", font_size=20, falling_speed=5, animation_length="infinite")

# === Get user name from URL ===
def get_person_name():
    query_params = st.query_params  # Updated to use `st.query_params`
    return query_params.get("name", ["Invité"])[0]

# === Page configuration ===
st.set_page_config(page_title="Journée de l’eau", page_icon="💧")

# === Start water animation ===
run_water_animation()

# === Load and apply CSS ===
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# === Personalized greeting ===
PERSON_NAME = get_person_name()
st.markdown(f"<h1 style='text-align: center;'>💧 Journée de l’eau 💧</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>👤 Bienvenue, {PERSON_NAME} !</h3>", unsafe_allow_html=True)

# === Lottie animation display ===
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-water", height=300)

# === Inspirational References Section ===
st.markdown("---")
st.markdown(
    """
    ### 💧 Pour s’inspirer
    > 💬 *"L'eau est la force motrice de toute la nature."* — Léonard de Vinci  
    > 💬 *"Chaque goutte compte. Sauvons l’eau, sauvons la vie."*  
    > 💬 *"L’accès à l’eau potable est un droit, pas un privilège."*

    ---
    
    📚 Références Bibliographiques: 
         1-www.agrimaroc.ma 
         2- www.agriculture.men.gov.ma 
         3-L'Organisation des Nations Unies pour l'alimentation et l'agriculture (FAO),
         4-Institut Royal des Études Stratégiques, Rapport "L’avenir de l’eau au Maroc", 2021
         5-Office National de l’Eau Potable (ONEE), via SNRTNews, 2023
         6-Programme National d’Économie d’Eau, Ministère de l’Équipement et de l’Eau, 2022
         7-Conseil Economique, Social et Environnemental (C.E.S.E.), (2014) : « Gouvernance par la gestion intégrée des ressources en eau au Maroc : levier fondamental de développement 
         durable » ; Synthèse ; 5 pages. Consultable in : www.ces.ma
         8-Conseil Economique, Social et Environnemental (Septembre 2019) : « Le droit à l’eau et la sécurité hydrique, gravement menacés par un usage intensif : le C.E.S.E. tire la sonnette 
         d’alarme et appelle à entreprendre des mesures urgentes ». Consultable in : www.ces.ma 
 
    **Partagé par [Professeur stagiaires SVT - Jihane.J- Mustapha.A- Hicham.A- Saida.R- Jamal.B 💙]**
    
    
    
    © all rights reserved
    """,
    unsafe_allow_html=True
)
