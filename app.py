'''
streamlit -> module used to write python code on the web
qrcode -> takes some data e.g., a link and returns an image 
'''
import streamlit as st
import io
import qrcode


#Function to generate the qrcode.
#The qrcode library only functions when put inside a function,
#it did not work when inside the main program
def generate_qr_code(url, fill_color, bg_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=bg_color)
    return img


# Main program 
st.title("Welcome to QR code generator! 🔗 🌐")

url_input = st.text_input("_Type or paste in your link..._", placeholder="https://yummycoffee.co.uk")

bg_color = st.color_picker("**Pick a background colour**")
fg_color = st.color_picker("**Pick a foreground colour**", value="#ffffff")

if url_input:
    submit_button = st.button("Generate QR Code")


    # Code to execute when the user presses the generate button
    if submit_button and url_input:
        try:
            # fill_color, bg_color = color_pairs[color_pair]
            qr_img = generate_qr_code(url_input, fg_color, bg_color)
            
            # Save the PIL Image to a BytesIO buffer and convert it to bytes
            img_buffer = io.BytesIO()
            qr_img.save(img_buffer, format="PNG")
            img_bytes = img_buffer.getvalue()
        

            st.image(img_bytes)

            # Add a download button
            st.download_button(
                label="Download QR Code",
                data=img_bytes,
                key="qr_code_download",
                file_name="qr_code.png",
                mime="image/png",
            )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")