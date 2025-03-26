import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import io

def apply_filters(image, brightness, contrast, sharpness, blur):
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Apply filters with stronger effects for visible changes
    image = ImageEnhance.Brightness(image).enhance(brightness * 1.5)
    image = ImageEnhance.Contrast(image).enhance(contrast * 1.5)
    image = ImageEnhance.Sharpness(image).enhance(sharpness * 2.0)

    if blur > 0:
        image = image.filter(ImageFilter.GaussianBlur(radius=blur * 2))

    return image

def main():
    st.set_page_config(page_title="📷 Photo Manipulation Tool 🎨", layout="centered")

    st.title("📷 Photo Manipulation Tool 🎨")
    st.write("Upload an image and adjust filters to enhance it!")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="🖼️ Original Image", use_container_width=True)

        st.sidebar.header("⚙️ Adjustments")
        brightness = st.sidebar.slider("🌞 Brightness", 0.1, 3.0, 1.0, 0.1)
        contrast = st.sidebar.slider("🌓 Contrast", 0.1, 3.0, 1.0, 0.1)
        sharpness = st.sidebar.slider("🔍 Sharpness", 0.1, 5.0, 1.0, 0.1)
        blur = st.sidebar.slider("🌫️ Blur", 0.0, 10.0, 0.0, 0.5)

        if st.sidebar.button("✨ Apply Filters ✨"):
            edited_image = apply_filters(image, brightness, contrast, sharpness, blur)
            st.image(edited_image, caption="🎨 Edited Image", use_container_width=True)

            buf = io.BytesIO()
            edited_image.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.download_button(
                label="💾 Download Edited Image",
                data=byte_im,
                file_name="edited_image.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()

#Ye project ek image editing tool hai jo Streamlit aur PIL (Python Imaging Library) ka use karta hai. Aap ek image upload kar sakte hain aur us par brightness, contrast, sharpness, aur blur jaise filters apply kar sakte hain. 🚀

