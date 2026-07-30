import streamlit as st

st.set_page_config(page_title="Para Marquitos", page_icon="❤️")

st.title('❤️ Para Marquitos')
st.subheader('Abrir cuando...')
st.write('Elegí una opción segùn cómo te sientas:')

def abrir_carta(titulo, mensaje):
    st.success(f"### {titulo}\n{mensaje}")

# --- Botones y Mensajes ---
if st.button('😢 Me extrañes mucho'):
    abrir_carta("Te extraño", "Yo también te extraño un montón. ¡Acordate que ya falta menos para vernos! Te amo.")

if st.button('🧠 Estés muy estresado'):
    abrir_carta("Respirá", "Cerrá los ojos, tomá agua y alejate de la pantalla 5 minutos. Vos podés con todo, estoy súper orgullosa de vos.")

if st.button('😴 No puedas dormir'):
    abrir_carta("A descansar", "Tratá de dejar el celu. Imaginate que estoy ahí haciéndote mimos en la cabeza hasta que te duermas.")

if st.button('🎂 Sea tu cumpleaños'):
    abrir_carta("¡Feliz Cumple!", "¡Que tengas el mejor día del mundo! Te merecés todo lo lindo que te pasa.")

st.markdown("---")
st.caption("Hecho con amor para Marquitos")
