import streamlit as st
from PIL import Image
# import easyocr as ocr
import numpy as np
# from text_summarization import summarizeText as ts
import text_summarization as ts
# import pytesseract
st.title("****TEXT SUMMARIZATION****")
# st.slider.markdown("CHOSE A FILE")
# st.slider.button("IMPORT IMAGE")


def load_image(image_file):
    img = Image.open(image_file)
    return img


def main():
    st.title("SUMMARIZE ANY TEXT")
    menu = ["Image", "Text"]
    choice = st.sidebar.selectbox(r"SELECT AN OPTION", menu)
    if choice == "Image":
        st.subheader("Image")

        image_file = st.file_uploader(
            "Upload Images", type=["png", "jpg", "jpeg"])

        if image_file is not None:
            # To See details
            file_details = {"filename": image_file.name, "filetype": image_file.type,
                            "filesize": image_file.size}
            st.write(file_details)
            st.image(load_image(image_file), width=250)

            st.button("CONVERT IMAGE TO TEXT")  # call ocr module

    elif choice == "Text":
        st.subheader("Text")
        text = st.text_input("ENTER YOUR TEXT HERE", "")
        text = str(text)
        if st.button("SUMMARIZE THIS TEXT"):
            ts.summarizeText(text)
            result = ts.summarizeText.result

            # ts.generate_summary()

            st.markdown(f"THE SUMMURIZED TEXT : {result}")

    # if choice == "Image":
    #     st.subheader("Image")
    #     image_file = st.file_uploader(
    #         "Upload Images", type=["png", "jpg", "jpeg"])

#     if image_file is not None:

#         # To See details
#         file_details = {"filename": image_file.name, "filetype": image_file.type,
#                         "filesize": image_file.size}
#         st.write(file_details)

# # To View Uploaded Image
#         st.image(load_image(image_file), width=250)


# load_image("test1.jpg")
main()
#     if choice == "Image":
#         st.subheader("Image")
#         image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

#         if image_file is not None:

#         # To See details
#             file_details = {"filename": image_file.name, "filetype": image_file.type,
#                         "filesize": image_file.size}
#             st.write(file_details)

#       # To View Uploaded Image
#             st.image(load_image(image_file), width=250)
