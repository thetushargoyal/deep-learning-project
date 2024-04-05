import gradio as gr
import soundfile as sf

css = """
h1 {
    text-align: center;
    display:block;
}

h2 {
    text-align: center;
    display:block;
}
"""

def save_audio(english, hindi):
    sf.write("audio_english.mp3", english[1], english[0])
    sf.write("audio_hindi.mp3", hindi[1], hindi[0])

def main():

    with gr.Blocks(css=css) as demo:
        gr.Markdown("""# Cross Language Speech Synthesis""")
        gr.Markdown("""## Aryaman Khandelwal, Hriday Rathi, Shreevardhan Shah, Tushar Garg, Tushar Goyal""")
        with gr.Column():
            with gr.Row():
                gr.Markdown("""# Record English""")
                gr.Markdown("""# Record Hindi""")
            with gr.Row():
                gr.Markdown("""### The sun dipped low on the horizon, casting long shadows across the deserted beach. A gentle breeze whispered through the palm trees, rustling their fronds softly. Seagulls cried out as they circled above, searching for their evening meal. The waves lapped lazily against the shore, creating a soothing rhythm that echoed in the stillness of the evening. It was a moment of tranquility, a fleeting glimpse of nature's beauty before nightfall descended.""")
                gr.Markdown("""### अरे अफहजकैफ़""")
            with gr.Row():
                eng = gr.Audio(sources=["microphone", "upload"], format="mp3", type="numpy", label="English", show_label=True)
                hin = gr.Audio(sources=["microphone", "upload"], format="mp3", type="numpy", label="Hindi", show_label=True)
        button = gr.Button("Submit")

        button.click(save_audio, inputs=[eng, hin], outputs=None)

    demo.launch()


if __name__ == '__main__':
    main()