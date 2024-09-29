import os 
from groq import Groq 
def redundify(firmware):
    client = Groq(api_key = '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')
    stream = client.chat.completions.create(
        messages = [
            {
        'role': 'user',
        'content': f'Look at this code: \n {firmware} \n point out the specific line of codes that are redundant and can be optimised, give recommended code for the selected lines and reason they are redundant.'
    }], 
        model = 'mixtral-8x7b-32768',
        #stream = True, 
    )
    #for chunk in stream: 
        #a = chunk.choices[0].delta.content, end= ""
    stream = stream.choices[0].message.content
    return(stream)



import gradio as gr

html = """
<html>
    <body>
        <h1>Redundify: What, where and why. </h1>
    </body>
</html>
"""

for line in html:
    line = html 
with gr.Blocks() as demo:
    input_mic = gr.HTML(line)
    firmware = gr.Textbox(label="Initial firmware")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Redundi-fy")
    greet_btn.click(fn = redundify, inputs= firmware, outputs = output, api_name="greet")
    @gr.render(inputs= firmware)
    def show_split(text):
        if len(text) == 0:
            gr.Markdown("## No Input Provided")

demo.launch()




