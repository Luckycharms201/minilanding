import streamlit as st
import webbrowser

#CONFIG GENERAL
st.set_page_config(page_title="Invitación Patrocinadores", page_icon=":tada:", layout="centered")

#HEADER BANNER
custom_html = """
<div class="banner">
    <img src="https://i.ibb.co/H7v9kWr/Banner-Forms-OS24-copia.jpg" alt="Banner Image">
</div>
<style>
    .banner {
        width: 100%;
        height: 50px;
        overflow: hidden;
    }
    .banner img {
        width: 100%;
        object-fit: cover;
    }
</style>
"""
#DISPLAY BANNER
st.markdown(custom_html, unsafe_allow_html=True)

custom_bg = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://i.ibb.co/vvVSWK2/sultanesbg.png");
bacground-size: cover;
}
</style>
"""
st.markdown(custom_bg, unsafe_allow_html=True)

header = '<p style="font-family:sans-serif; color:White; font-size: 42px;">Bienvenidos</p>'
st.markdown(header, unsafe_allow_html=True)

subheader = '<p style="font-family:sans-serif; color:White; font-size: 12px;">Recapitulación de la serie pasada</p>'
st.markdown(subheader, unsafe_allow_html=True)

#VIDEO
video_url = 'https://www.youtube.com/watch?v=NIUTU0N-88E'
st.video(video_url)

subheader2 = '<p style="font-family:sans-serif; color:White; font-size: 12px;">Sultanes te invita a ti y tus amigos a disfrutar del beisbol en el Estadio Mobil Super</p>'
st.markdown(subheader2, unsafe_allow_html=True)

#PHOTO
st.markdown("[![Foo](https://i.ibb.co/L93DSSw/invitacion-SULTANES.png)](https://docs.google.com/forms/d/e/1FAIpQLSc9ncbdgbHOQbF58KiDiExVBILlRyy7uTjXWhRl_qlWY1czaw/viewform)")
