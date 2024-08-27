
import streamlit as st
import whisper


st.title("Whisper App")

# upload audio file with streamlit
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

def get_transcription():
    model = whisper.load_model("base")
    result = model.transcribe(audio_file.name)
    return result["text"]
    

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing Audio")
        transcription = get_transcription()
        st.sidebar.success("Transcription Complete")
        st.markdown(transcription)
    else:
        st.sidebar.error("Please upload an audio file")


st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)